#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
import re
import xml.etree.ElementTree as et

import lsst.ts.xml as ts_xml
import pytest
from lxml import etree

INDEX_ENUM_CHECK = re.compile(r"[^,= \w]+")

# These are the "languages" we need to build libraries for.
# Note: SalObj CSCs use Python as the RuntimeLanguage. They
# used to define IDL as the RuntimeLanguage.
VALID_RUNTIME_LANGUAGES = {"CPP", "Java", "LabVIEW", "Python"}


def get_salsubsystems_file() -> pathlib.Path:
    datadir = ts_xml.get_data_dir()
    sal_subsystems_file = datadir / "sal_interfaces/SALSubsystems.xml"
    return sal_subsystems_file


def skip_if_known_issue(test: str, csc: str) -> None:
    jira = ""
    if jira:
        pytest.skip(jira + f": {csc}")


def get_file_root_element() -> et.Element:
    sal_subsystems_file = get_salsubsystems_file()
    with open(str(sal_subsystems_file), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    return root


def get_csc_attr_content(attribute: str) -> list[tuple[et.Element, str, str]]:
    root = get_file_root_element()
    arguments: list[tuple[et.Element, str, str]] = []
    for csc in ts_xml.subsystems:
        found = root.find(f"./SALSubsystem/[Name='{csc}']/{attribute}")
        assert found is not None
        content = found.text
        assert content is not None
        arguments.append((root, csc, content))
    return arguments


def whitespace_checks(content: str | None, attribute: str, csc: str) -> None:
    assert content is not None, f"{csc} <{attribute}> text must not be empty"
    assert not content.isspace(), f"{csc} <{attribute}> text must not be all whitespace"


# ==================
# Tests
# ==================


def test_salsubsystems_xml_valid() -> None:
    """Test that the SALSubsystems.xml conforms to its schema."""
    datadir = ts_xml.get_data_dir()
    xmlschema_doc = etree.parse(f"{datadir}/schema/SALSubsystemSet.xsd")
    xmlschema = etree.XMLSchema(xmlschema_doc)
    sal_subsystems_file = get_salsubsystems_file()
    tree = etree.parse(str(sal_subsystems_file))
    try:
        xmlschema.assertValid(tree)
    except etree.DocumentInvalid as err:
        assert False, f"{sal_subsystems_file.name}: {err}"


def test_salsubsystems_count() -> None:
    """Test that SALSubsystems.xml defines the expected number of CSCs."""
    # Check for known issues.
    skip_if_known_issue("count", "none")
    # Test SALGenerics.xml contains the expected commands.
    root = get_file_root_element()
    assert len(root.findall("./SALSubsystem/Name")) == len(
        ts_xml.subsystems
    ), "There is an unexpected number of CSCs."


def test_salsubsystems_uniq_cscs() -> None:
    """Test that SALSubsystems.xml does not contain duplicate CSCs."""
    # Check for known issues.
    skip_if_known_issue("uniq", "none")
    # Test SALGenerics.xml contains unique CSCs.
    root = get_file_root_element()
    assert len(root.findall("./SALSubsystem/Name")) == len(
        set(root.findall("./SALSubsystem/Name"))
    ) and len(ts_xml.subsystems) == len(
        set(ts_xml.subsystems)
    ), "SALSubsystems.xml or testutils.subsystems contains duplicate entries"


def test_each_csc_defined() -> None:
    """Test that SALSubsystems.xml defines the expected set of CSCs."""
    # Check for known issues.
    skip_if_known_issue("defined", "none")
    # Verify each CSC is explicitly defined.
    root = get_file_root_element()
    subsystems = ts_xml.subsystems
    subsystems.sort()
    cscs: list[str] = []
    for csc in root.findall("./SALSubsystem/Name"):
        assert csc.text is not None
        cscs.append(csc.text)
    cscs.sort()
    assert ts_xml.subsystems == cscs, "There is a duplicate CSC."


@pytest.mark.parametrize("root,csc,description", get_csc_attr_content("Description"))
def test_description_tag(root: et.Element, csc: str, description: str) -> None:
    """Test that the <Description> tag is correctly defined for each
       CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    description : `str`
        Value of the <Description> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("description", csc)
    # Verify the <Description> tag is properly defined.
    whitespace_checks(description, "Description", csc)
    assert (
        description.isprintable()
    ), f"{csc} <Description> must have a name associated!"


@pytest.mark.parametrize(
    "root,csc,index_enumeration", get_csc_attr_content("IndexEnumeration")
)
def test_index_enumeration_tag(
    root: et.Element, csc: str, index_enumeration: str
) -> None:
    """Test that the <IndexEnumeration> tag is correctly defined for each
       CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    index_enumeration : `str`
        Value of the <IndexEnumeration> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("index_enumeration", csc)
    # Verify the <IndexEnumeration> tag is properly defined.
    whitespace_checks(index_enumeration, "IndexEnumeration", csc)
    content_checks = index_enumeration in ["no", "any"]
    no_zero = index_enumeration != "0"
    format_valid = INDEX_ENUM_CHECK.search(index_enumeration) is None
    name_valid = True
    kv_pair_valid = True
    if format_valid:
        for value in index_enumeration.split(","):
            if "=" not in value:
                name_valid = name_valid and value.isalnum()
            else:
                k, v = value.split("=")
                kv_pair_valid = kv_pair_valid and k.isalnum() and v.isnumeric()
    else:
        name_valid = False
        kv_pair_valid = False

    message = [
        f"{csc} <IndexEnumeration> must be 'no', 'any',",
        "a possible comma-separated list of names,",
        "a possible comma-separated list of key=value pairs and never ever 0!",
    ]
    assert no_zero and (
        content_checks or format_valid or name_valid or kv_pair_valid
    ), " ".join(message)


@pytest.mark.parametrize(
    "root,csc,added_generics", get_csc_attr_content("AddedGenerics")
)
def test_generics_tag(root: et.Element, csc: str, added_generics: str) -> None:
    """Test that the <AddedGenerics> tag is correctly defined for each CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    added_generics : `str`
        Value of the <AddedGenerics> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("added_generics", csc)
    if added_generics is None:
        return
    generics_set = set(val.strip() for val in added_generics.split(","))
    for generic_name in generics_set:
        assert (
            " " not in generic_name
        ), f"csc {csc} <AddedGenerics> tag '{generic_name}' need a comma"
    no_mandatory_topics = generics_set.intersection(
        ts_xml.added_generics_mandatory_topics
    )
    assert no_mandatory_topics == set(), (
        f"The <AddedGenerics> tag for csc {csc} contains mandatory topics: "
        f"{no_mandatory_topics}. It is not necessary to specify these."
    )
    invalid_topics = generics_set - ts_xml.added_generics_items
    assert invalid_topics == set(), (
        f"The <AddedGenerics> tag for csc {csc} has one or more non-generic topics: "
        f"{sorted(invalid_topics)}"
    )


@pytest.mark.parametrize(
    "root,csc,active_developers", get_csc_attr_content("ActiveDevelopers")
)
def test_active_developers_tag(
    root: et.Element, csc: str, active_developers: str
) -> None:
    """Test that the <ActiveDevelopers> tag is correctly defined for each
       CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    active_developers : `str`
        Value of the <ActiveDevelopers> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("active_developers", csc)
    # Verify the <ActiveDevelopers> tag is properly defined.
    whitespace_checks(active_developers, "ActiveDevelopers", csc)
    assert (
        active_developers.isprintable()
    ), f"{csc} <ActiveDevelopers> must have a name associated!"


@pytest.mark.parametrize("root,csc,github", get_csc_attr_content("Github"))
def test_github_tag(root: et.Element, csc: str, github: str) -> None:
    """Test that the <Github> tag is correctly defined for each
       CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    github : `str`
        Value of the <Github> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("github", csc)
    # Verify the <Github> tag is properly defined.
    whitespace_checks(github, "Github", csc)
    assert (
        "http" in github or github.isprintable()
    ), f"{csc} <Github> must have a URL associated or informative text!"


@pytest.mark.parametrize("root,csc,languages", get_csc_attr_content("RuntimeLanguages"))
def test_runtimelanguages_tag(root: et.Element, csc: str, languages: str) -> None:
    """Test that the <RuntimeLanguages> tag is correctly defined for each CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    languages : `str`
        Value of the <RuntimeLanguages> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("languages", csc)
    # Verify each CSC is explicitly defined.
    for language in languages.split(","):
        assert (
            language in VALID_RUNTIME_LANGUAGES
        ), f"{csc}: {language} is not a valid value for <RuntimeLanguages>."


@pytest.mark.parametrize(
    "root,csc,jenkins_test_results", get_csc_attr_content("JenkinsTestResults")
)
def test_jenkins_test_results_tag(
    root: et.Element, csc: str, jenkins_test_results: str
) -> None:
    """Test that the <JenkinsTestResults> tag is correctly defined for each
       CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    jenkins_test_results : `str`
        Value of the <JenkinsTestResults> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("jenkins_test_results", csc)
    # Verify the <JenkinsTestResults> tag is properly defined.
    whitespace_checks(jenkins_test_results, "JenkinsTestResults", csc)
    assert (
        jenkins_test_results == "Not Available" or "http" in jenkins_test_results
    ), f"{csc} <JenkinsTestResults> must have a URL or Not Available as content"


@pytest.mark.parametrize("root,csc,product_owner", get_csc_attr_content("ProductOwner"))
def test_product_owner_tag(root: et.Element, csc: str, product_owner: str) -> None:
    """Test that the <ProductOwner> tag is correctly defined for each
       CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    product_owner : `str`
        Value of the <ProductOwner> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("product_owner", csc)
    # Verify the <ProductOwner> tag is properly defined.
    whitespace_checks(product_owner, "ProductOwner", csc)
    assert (
        product_owner.isprintable()
    ), f"{csc} <ProductOwner> must have a name associated!"


@pytest.mark.parametrize(
    "root,csc,rubin_obs_contact", get_csc_attr_content("RubinObsContact")
)
def test_rubin_obs_contact_tag(
    root: et.Element, csc: str, rubin_obs_contact: str
) -> None:
    """Test that the <RubinObsContact> tag is correctly defined for each CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    rubin_obs_contact : `str`
        Value of the <RubinObsContact> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("rubin_obs_contact", csc)
    # Verify the <RubinObsContact> tag is properly defined.
    whitespace_checks(rubin_obs_contact, "RubinObsContact", csc)
    assert (
        rubin_obs_contact.isprintable()
    ), f"{csc} <RubinObsContact> must have a name (string) associated!"


@pytest.mark.parametrize(
    "root,csc,vendor_contact", get_csc_attr_content("VendorContact")
)
def test_vendor_contact_tag(root: et.Element, csc: str, vendor_contact: str) -> None:
    """Test that the <VendorContact> tag is correctly defined for each CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    vendor_contact : `str`
        Value of the <VendorContact> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("vendor_contact", csc)
    # Verify the <VendorContact> tag is properly defined.
    whitespace_checks(vendor_contact, "VendorContact", csc)
    assert (
        vendor_contact == "Not Applicable" or vendor_contact.isprintable()
    ), f"{csc} <VendorContact> must have a name (string) or Not Applicable as content"


@pytest.mark.parametrize("root,csc,simulator", get_csc_attr_content("Simulator"))
def test_simulator_tag(root: et.Element, csc: str, simulator: str) -> None:
    """Test that the <Simulator> tag is correctly defined for each CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    simulator : `str`
        Value of the <Simulator> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("simulator", csc)
    # Verify each CSC is explicitly defined.
    assert (
        type(root.find(f"./SALSubsystem/[Name='{csc}']/Simulator")) is et.Element
    ), f"{csc} <Simulator> tag is NOT defined."
    whitespace_checks(simulator, "Simulator", csc)
    content_checks = ["Internal to CSC", "Not Required", "Not Provided"]
    assert (
        simulator in content_checks or "http" in simulator
    ), f"{csc} <Simulator> have a URL or one of the following: {', '.join(content_checks)}"


@pytest.mark.parametrize(
    "root,csc,configuration", get_csc_attr_content("Configuration")
)
def test_configuration_tag(root: et.Element, csc: str, configuration: str) -> None:
    """Test that the <Configuration> tag is correctly defined for each CSC.

    Parameters
    ----------
    root: `et.Element`
        Root element for the sal_subsystems_file tree.
    csc : `csc`
        Name of the CSC.
    configuration : `str`
        Value of the <Configuration> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("configuration", csc)
    # Verify the <Configuration> tag is properly defined.
    whitespace_checks(configuration, "Configuration", csc)
    assert (
        configuration == "Not Configurable"
        or "Database" in configuration
        or "http" in configuration
    ), f"{csc} <Configuration> text must either be 'Not Configurable' or a URL to configuration DB or repo"
