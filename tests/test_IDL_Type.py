#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et

import lsst.ts.xml as ts_xml
import pytest


def check_for_issues(test, csc, topic):
    return ""


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_idl_type_exists(xmlfile, csc, topic):
    """Test that the <IDL_Type> field for topic attributes exists.

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
    jira = check_for_issues("exists", csc, topic)
    if jira:
        pytest.skip(f"{jira}: {xmlfile.name} <IDL_Type> fields must be defined.")
    # Test the <IDL_Type> field exists for each attribute.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    untyped_field_names = []
    for attrib in root.findall(f"./{saltype}/item"):
        name = attrib.find("EFDB_Name")
        idltype = attrib.find("IDL_Type")
        if idltype is None:
            untyped_field_names.append(name.text)
    assert (
        len(untyped_field_names) == 0
    ), f"IDL_Type for {untyped_field_names} must be defined."


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_idl_type(xmlfile, csc, topic):
    """Test that the <IDL_Type> field for topic attributes is properly formed,
    i.e. it is not blank and it is one of a set of predefined IDL Types.

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
    jira = check_for_issues("type", csc, topic)
    if jira:
        pytest.skip(
            f"{jira}: {xmlfile.name} <IDL_Type> fields do not conform to IDL standards."
        )
    # Test the attribute <Description> fields.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    for idl_type in root.findall(f"./{saltype}/item/IDL_Type"):
        assert idl_type.text is not None, "IDL_Type cannot be blank."
        assert (
            idl_type.text in ts_xml.idl_types
        ), f"IDL_Type {idl_type.text} needs to be one of {ts_xml.idl_types}"
