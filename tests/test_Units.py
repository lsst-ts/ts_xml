#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import xml.etree.ElementTree as et
import astropy.units
import lsst.ts.xml as ts_xml


def check_for_issues(csc, topic):
    if csc == "PromptProcessing":
        jira = "CAP-592"
    return jira


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_units(xmlfile, csc, topic):
    """Test that the <Units> field for topic attributes is properly formed,
    i.e. it is not blank, conforms to astropy standards or is unitless.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xmlfile.stem`
        One of ['Commands','Events','Telemetry']
    """
    saltype = "SAL" + topic.rstrip("s")
    # Check for known issues.
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(
            jira
            + ": "
            + str(xmlfile.name)
            + " <Unit> fields do not conform to astropy standards."
        )
    # Test the attribute <Description> fields.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    for unit in root.findall(f"./{saltype}/item/Units"):
        if not unit.text.replace(" ", ""):
            assert False, "Units cannot be blank."
        elif unit.text in ("unitless", "dimensionless"):
            assert True
        elif unit.text in (
            "Torr",
            "mTorr",
            "psia",
            "VA",
        ):  # TODO remove this when astropy adds support for this unit
            assert True
        else:
            assert type(ts_xml.check_unit(unit.text)) is astropy.units.Quantity
            "Unit '" + unit.text + "' in " + str(
                xmlfile.name
            ) + " does not meet astropy standards."


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_string_units(xmlfile, csc, topic):
    """Test that the <Units> field for STRING-type attributes is 'unitless.'

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xmlfile.stem`
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
            name = attrib.find("EFDB_Name")
            unit = attrib.find("Units")
            # There is a robust skip list,
            # as many strings represent angles or time.
            if csc in ["ATPtg", "MTPtg"] and name.text in ts_xml.strings_with_units:
                assert True
            else:
                assert unit.text in (
                    "unitless",
                    "dimensionless",
                ), f"{csc}: string-type attribute {name.text!r} has the unit {unit.text!r}"
