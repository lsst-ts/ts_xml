#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


def check_for_issues(csc, topic, test):
    if csc == "Hexapod" and topic == "Telemetry" and test == "alias":
        jira = "DM-20971"
    elif csc == "Dome" and topic == "Telemetry" and test == "alias":
        jira = "DM-22153"
    elif csc == "MTMount" and topic == "Telemetry" and test == "alias":
        jira = "DM-17276"
    elif csc == "Rotator" and topic == "Telemetry" and test == "alias":
        jira = "DM-20969"
    else:
        jira = ""
    return jira


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_topic_naming_csc(xmlfile, csc, topic):
    """Test that the <EFDB_Topic> field for topics is properly formed.
    The <EFDB_Topic> is a compound word comprising the CSC Name,
    the topic type, if applicable, and the topic name.
    Names begin with a lowercase letter and contain only alphanumeric
    and underscore characters.

    This tests the first root, the CSC name.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xmlfile.stem`
        One of ['Commands','Events','Telemetry']
    """
    saltype = "SAL" + topic.rstrip('s')
    # Check for known issues.
    jira = check_for_issues(csc, topic, "csc")
    if jira:
        pytest.skip(jira + ": " + str(xmlfile.name) + " <EFDB_Topic> is not properly formed.")
    # Test the topic <EFDB_Name> field.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    for name in root.findall(f"./{saltype}/EFDB_Topic"):
        index = 0
        assert name.text.split('_')[index] == csc, "<EFDB_Topic> " + name.text + \
            ' in ' + str(xmlfile.name) + ' does not properly contain the CSC name.'


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_topic_naming_type(xmlfile, csc, topic):
    """Test that the <EFDB_Topic> field for topics is properly formed.
    The <EFDB_Topic> is a compound word comprising the CSC Name,
    the topic type, if applicable, and the topic name.

    This tests the second root, the topic type.
    NOTE: Telemetry topics do not explicitly define the topic type.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xmlfile.stem`
        One of ['Commands','Events','Telemetry']
    """
    saltype = "SAL" + topic.rstrip('s')
    # Check for known issues.
    jira = check_for_issues(csc, topic, "type")
    if jira:
        pytest.skip(jira + ": " + str(xmlfile.name) + " <EFDB_Topic> is not properly formed.")
    # Test the topic <EFDB_Name> field.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    for name in root.findall(f"./{saltype}/EFDB_Topic"):
        if topic == "Telemetry":
            # Telemetry topics do not explicitly define the topic type.
            continue
        elif topic == "Events":
            topictype = "logevent"
        else:
            topictype = "command"
        index = 1
        assert name.text.split('_')[index] == topictype, \
            "<EFDB_Topic> " + name.text + ' in ' + str(xmlfile.name) + \
            ' does not properly contain the topicType string.'


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_topic_naming_alias(xmlfile, csc, topic):
    """Test that the <EFDB_Topic> field for topics is properly formed.
    The <EFDB_Topic> is a compound word comprising the CSC Name,
    the topic type, if applicable, and the topic name.
    Names begin with a lowercase letter and contain only alphanumeric
    and underscore characters.

    This tests the last root, the topic name.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xmlfile.stem`
        One of ['Commands','Events','Telemetry']
    """
    saltype = "SAL" + topic.rstrip('s')
    # Check for known issues.
    jira = check_for_issues(csc, topic, "alias")
    if jira:
        pytest.skip(jira + ": " + str(xmlfile.name) + " <EFDB_Topic> is not properly formed.")
    # Test the topic <EFDB_Name> field.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    for name in root.findall(f"./{saltype}/EFDB_Topic"):
        # re.match() returns None if the string does not match the regex.
        if topic == "Telemetry":
            index = 1
        else:
            index = 2
        assert re.match(r"^[a-z]([a-zA-Z0-9_]*$)", name.text.split('_')[index]) is not None, \
            name.text + ' in ' + str(xmlfile.name) + ' does not begin with a lowercase '\
            'letter and/or contains non-alphanumeric characters.'
