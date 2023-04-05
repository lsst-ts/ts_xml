#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
import xml.etree.ElementTree as et

import astropy.units
import lsst.ts.xml as ts_xml
import pytest

# These nonstandard units are explicitly allowed.
# Remove entries if and when astropy adds support for them.
NONSTANDARD_UNITS = {"unitless", "psia", "VA"}


def check_for_issues(csc: str, topic: str) -> str:
    jira = ""
    return jira


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_units(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Test that the <Units> field for topic attributes is properly formed,
    i.e. it is not blank, conforms to astropy standards or is unitless.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `str`
        Name of the CSC
    topic : `str`
        One of ['Commands','Events','Telemetry']
    """
    saltype = "SAL" + topic.rstrip("s")
    # Check for known issues.
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(
            f"{jira}: {xmlfile.name} <Unit> fields do not conform to astropy standards."
        )
    # Test the attribute <Description> fields.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    for unit in root.findall(f"./{saltype}/item/Units"):
        assert unit.text is not None
        if not unit.text.replace(" ", ""):
            assert False, "Units cannot be blank."
        elif unit.text in NONSTANDARD_UNITS:
            assert True
        else:
            assert type(ts_xml.check_unit(unit.text)) is astropy.units.Quantity
            (f"Unit {unit.text!r} in {xmlfile.name} does not meet astropy standards.")


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_string_units(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Test that the <Units> field for STRING-type attributes is 'unitless.'

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `str`
        Name of the CSC
    topic : `str`
        One of ['Commands','Events','Telemetry']
    """
    saltype = "SAL" + topic.rstrip("s")
    # Check for known issues.
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(
            f"{jira}: {xmlfile.name} <Unit> fields do not conform to astropy standards."
        )
    # Test the attribute <Units> fields.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    for attrib in root.findall(f"./{saltype}/item"):
        idltype = attrib.find("IDL_Type")
        if idltype is not None and idltype.text == "string":
            name = ts_xml.find_text_in_xml(attrib, "EFDB_Name")
            unit = ts_xml.find_text_in_xml(attrib, "Units")
            # There is a robust skip list,
            # as many strings represent angles or time.
            if csc in ["ATPtg", "MTPtg"] and name in ts_xml.strings_with_units:
                assert True
            else:
                assert (
                    unit == "unitless"
                ), f"{csc}: string-type attribute {name!r} has the unit {unit!r}"
