#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


def get_salsubsystems_file():
    pkgroot = pathlib.Path(__file__).resolve().parents[1]
    sal_subsystems_file = pkgroot / "sal_interfaces/SALSubsystems.xml"
    return sal_subsystems_file


def skip_if_known_issue(test, csc):
    jira = ""
    if jira:
        pytest.skip(jira + f": {csc}")


def get_file_root_element():
    sal_subsystems_file = get_salsubsystems_file()
    with open(str(sal_subsystems_file), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    return root


def get_csc_generics():
    root = get_file_root_element()
    arguments = []
    for csc in ts_xml.subsystems:
        generics = root.find("./SALSubsystem/[Name='" + csc + "']/Generics").text
        arguments.append((root, csc, generics))
    return arguments


def get_csc_runtimelanguages():
    root = get_file_root_element()
    arguments = []
    for csc in ts_xml.subsystems:
        languages = root.find("./SALSubsystem/[Name='" + csc + "']/RuntimeLanguages").text
        arguments.append((root, csc, languages))
    return arguments


def get_csc_simulator():
    root = get_file_root_element()
    arguments = []
    for csc in ts_xml.subsystems:
        simulator = root.find("./SALSubsystem/[Name='" + csc + "']/Simulator").text
        arguments.append((root, csc, simulator))
    return arguments


def get_csc_configurable():
    root = get_file_root_element()
    arguments = []
    for csc in ts_xml.subsystems:
        configurable = root.find("./SALSubsystem/[Name='" + csc + "']/Configurable").text
        arguments.append((root, csc, configurable))
    return arguments


# ==================
# Tests
# ==================

def test_salsubsystems_count():
    """Test that SALSubsystems.xml defines the expected number of CSCs.
    """
    # Check for known issues.
    skip_if_known_issue("count", "none")
    # Test SALGenerics.xml contains the expected commands.
    root = get_file_root_element()
    assert len(root.findall("./SALSubsystem/Name")) == len(ts_xml.subsystems), \
        "There is an unexpected number of CSCs."


def test_salsubsystems_uniq_cscs():
    """Test that SALSubsystems.xml does not contain duplicate CSCs.
    """
    # Check for known issues.
    skip_if_known_issue("uniq", "none")
    # Test SALGenerics.xml contains unique CSCs.
    root = get_file_root_element()
    assert len(root.findall("./SALSubsystem/Name")) == len(set(root.findall("./SALSubsystem/Name"))) \
        and len(ts_xml.subsystems) == len(set(ts_xml.subsystems)), \
        "SALSubsystems.xml or testutils.subsystems contains duplicate entries"


def test_each_csc_defined():
    """Test that SALSubsystems.xml defines the expected set of CSCs.
    """
    # Check for known issues.
    skip_if_known_issue("defined", "none")
    # Verify each CSC is explicitly defined.
    root = get_file_root_element()
    subsystems = ts_xml.subsystems
    subsystems.sort()
    cscs = []
    for csc in root.findall(f"./SALSubsystem/Name"):
        cscs.append(csc.text)
    cscs.sort()
    assert ts_xml.subsystems == cscs, "There is a duplicate CSC."


@pytest.mark.parametrize("root,csc,generics", get_csc_generics())
def test_generics_tag(root, csc, generics):
    """Test that the <Generics> tag is correctly defined for each CSC.

    Parameters
    ----------
    root: `get_file_root_element()`
        Root element for the sal_subsystems_file tree.
    csc : `testutils.subsystems`
        Name of the CSC.
    generics : `get_csc_generics()`
        Value of the <Generics> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("generics", csc)
    # Set the condition to no for CSCs that do not utilize Generic topics.
    if csc == "Script":
        value = "no"
    elif csc == "LOVE":
        value = "no"
    else:
        value = "yes"
    # Verify each CSC is explicitly defined.
    assert root.find("./SALSubsystem/[Name='" + csc + "']/Generics").text == value, \
        csc + " <Generics> tag is not defined as expected."


@pytest.mark.parametrize("root,csc,languages", get_csc_runtimelanguages())
def test_runtimelanguages_tag(root, csc, languages):
    """Test that the <RuntimeLanguages> tag is correctly defined for each CSC.

    Parameters
    ----------
    root: `get_file_root_element()`
        Root element for the sal_subsystems_file tree.
    csc : `testutils.subsystems`
        Name of the CSC.
    languages : `get_csc_runtimelanguages()`
        Value of the <RuntimeLanguages> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("languages", csc)
    # Verify each CSC is explicitly defined.
    for language in languages.split(','):
        assert language in ["CPP", "Java", "LabVIEW", "PyDDS", "Python"], \
            csc + ": " + language + " is not a valid value for <RuntimeLanguages>."


@pytest.mark.parametrize("root,csc,simulator", get_csc_simulator())
def test_simulator_tag(root, csc, simulator):
    """Test that the <Simulator> tag is correctly defined for each CSC.

    Parameters
    ----------
    root: `get_file_root_element()`
        Root element for the sal_subsystems_file tree.
    csc : `testutils.subsystems`
        Name of the CSC.
    simulator : `get_csc_simulator()`
        Value of the <Simulator> tag in sal_subsystems_file.
    """
    # Check for known issues.
    skip_if_known_issue("simulator", csc)
    # Verify each CSC is explicitly defined.
    assert type(root.find("./SALSubsystem/[Name='" + csc + "']/Simulator")) is et.Element, \
        csc + " <Simulator> tag is NOT defined."


def test_configurable_tag():
    """Test for the <Configurable> tag.

    Attributes
    ----------
    root: `get_file_root_element()`
        Root element for the sal_subsystems_file tree.
    """
    root = get_file_root_element()

    for csc in ts_xml.subsystems:

        # Verify that the tag is defined
        assert root.find("./SALSubsystem/[Name='" + csc + "']/Configurable") is not None, \
            csc + " <Simulator> tag is NOT defined."

        # Verify that the text of the tag is either "yes" or "no"
        assert root.find("./SALSubsystem/[Name='" + csc + "']/Configurable").text == "Yes" or \
            root.find("./SALSubsystem/[Name='" + csc + "']/Configurable").text == "No", \
            csc + " <Simulator> text must either be 'yes' or 'no'"
