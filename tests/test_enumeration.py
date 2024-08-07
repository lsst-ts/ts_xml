#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
import re
import xml.etree.ElementTree as et

import pytest
from lsst.ts.xml import enums, get_xmlfile_csc_topic, subsystems
from lsst.ts.xml.get_enums_from_xml import get_field_and_global_enums


@pytest.mark.parametrize("xmlfile,csc,topic", get_xmlfile_csc_topic())
def test_enumeration(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Test that enumerations have the correct format.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Events XML file for the CSC.
    csc : `csc`
        Name of the CSC
    """
    # Test the topic <EFDB_Name> field.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()

    reg_exp = re.compile(r"^[A-Z][a-zA-Z0-9_]*(\s*=\s*((0[xX][0-9a-fA-F]+)|(-?\d+)))?$")

    for sal_enum in root.findall("Enumeration"):
        assert sal_enum.text is not None
        for enum_value in sal_enum.text.split(","):
            assert (
                reg_exp.match(enum_value.strip()) is not None
            ), f"Invalid enumeration in {csc}/{topic}: {enum_value.strip()} :: {sal_enum.text}."


@pytest.mark.parametrize("xmlfile,csc,topic", get_xmlfile_csc_topic())
def test_enumeration_consistency(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Test that the enumeration lines either all declare a value or none do.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Events XML file for the CSC.
    csc : `csc`
        Name of the CSC
    """
    # Test the topic <EFDB_Name> field.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()

    for sal_enum in root.findall("Enumeration"):
        assert sal_enum.text is not None
        num_lines_with_explicit_value = 0
        num_lines_without_explicit_value = 0
        for enum_value in sal_enum.text.split(","):
            if "=" in enum_value:
                num_lines_with_explicit_value += 1
            else:
                num_lines_without_explicit_value += 1

        assert (
            num_lines_with_explicit_value == 0 or num_lines_without_explicit_value == 0
        ), f"Enumeration in {csc}/{topic} has mixed use cases."


@pytest.mark.parametrize("csc", subsystems)
def test_enum_classes(csc: str) -> None:
    _, global_enums = get_field_and_global_enums(csc)

    global_enums_set = set(global_enum.class_name for global_enum in global_enums) - {
        "SummaryStates",
        "SummaryState",
    }

    if not global_enums_set:
        return

    assert hasattr(
        enums, csc
    ), f"{csc} does not define enumeration. Expected {global_enums_set} enums."
    assert hasattr(
        getattr(enums, csc), "__all__"
    ), f"{csc} enumeration does not define __all__."

    try:
        enums_set = set(getattr(enums, csc).__all__)
    except AttributeError:
        raise RuntimeError(f"{csc} does not define a valid enumeration.")

    missing_enums = global_enums_set.difference(enums_set)
    undefined_enums = enums_set.difference(global_enums_set) - {"SalIndex"}

    assert (
        not missing_enums
    ), f"[{csc}] The following enums are missing: {missing_enums}."
    assert (
        not undefined_enums
    ), f"[{csc}] The following enums are not defined in the xml file: {undefined_enums}"
