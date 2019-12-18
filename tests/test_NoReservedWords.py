#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


def check_for_issues(csc, topic, language):
    if csc == "ATAOS" and topic == "Commands" and language == "optional":
        jira = "DM-22612"
    elif (csc == "ATMCS" and topic in ("Commands", "Events") and
            language == "critical"):
        jira = "DM-22613"
    elif (csc == "ATSpectrograph" and topic in ("Commands", "Events") and
            language == "optional"):
        jira = "DM-22614"
    elif (csc == "CatchupArchiver" and topic in ("Telemetry", "Events") and
            language == "optional"):
        jira = "CAP-399"
    elif (csc == "FiberSpectrograph" and topic == "Commands" and
            language == "optional"):
        jira = "DM-22616"
    elif (csc == "LOVE" and topic == "Events" and
            language == "optional"):
        jira = "DM-22617"
    elif (csc == "MTAOS" and topic == "Telemetry" and
            language == "optional"):
        jira = "DM-22618"
    elif (csc == "MTArchiver" and topic == "Events" and
            language == "optional"):
        jira = "CAP398"
    elif (csc == "MTCamera" and topic == "Commands" and
            language == "optional"):
        jira = "CAP-397"
    elif (csc == "MTMount" and topic == "Commands" and
            language == "critical"):
        jira = "DM-22622"
    elif (csc == "OCS" and topic in ("Telemetry", "Events") and
            language == "optional"):
        jira = "DM-22623"
    elif (csc == "PromptProcessing" and topic in ("Telemetry", "Events") and
            language == "optional"):
        jira = "DM-22624"
    elif (csc == "Scheduler" and topic == "Telemetry" and
            language == "optional"):
        jira = "DM-22625"
    elif (csc == "Script" and topic == "Events" and
            language == "optional"):
        jira = "DM-22626"
    elif (csc == "Test" and topic == "Commands" and
            language == "optional"):
        jira = "DM-22627"
    elif (csc == "Watcher" and topic in ("Commands", "Events") and
            language == "optional"):
        jira = "DM-22628"
    else:
        jira = ""
    return jira


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_no_idl_reserved_words(xmlfile, csc, topic):
    """Test that the <EFDB_Name> field does not use any IDL Reserved Words.

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
    jira = check_for_issues(csc, topic, "idl")
    if jira:
        pytest.skip(jira + ": " + str(xmlfile.name) +
                    " <EFDB_Name> uses IDL reserved word.")
    # Test the <EFDB_Name> fields do not use Reserved Words.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    bad_names = []
    for name in root.findall(f"./{saltype}/item/EFDB_Name"):
        if name.text.upper() in ts_xml.idl_reserved:
            bad_names.append(name.text.upper())
    assert bad_names == [], \
        "IDL Reserved Words used one or more times: " + str(bad_names)


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_no_db_critical_reserved_words(xmlfile, csc, topic):
    """Test that the <EFDB_Name> field does not use any critical
    database Reserved Words.

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
    jira = check_for_issues(csc, topic, "critical")
    if jira:
        pytest.skip(jira + ": " + str(xmlfile.name) +
                    " <EFDB_Name> uses database CRITICAL reserved word.")
    # Test the <EFDB_Name> fields do not use Reserved Words.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    bad_names = []
    for name in root.findall(f"./{saltype}/item/EFDB_Name"):
        if name.text.upper() in ts_xml.db_critical_reserved:
            bad_names.append(name.text.upper())
    assert bad_names == [], \
        "Critical database Reserved Words used one or more times: " + \
        str(bad_names)


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_no_db_optional_reserved_words(xmlfile, csc, topic):
    """Test that the <EFDB_Name> field does not use any optional
    database Reserved Words.

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
    jira = check_for_issues(csc, topic, "optional")
    if jira:
        pytest.skip(jira + ": " + str(xmlfile.name) +
                    " <EFDB_Name> uses database optional reserved word.")
    # Test the <EFDB_Name> fields do not use Reserved Words.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    bad_names = []
    for name in root.findall(f"./{saltype}/item/EFDB_Name"):
        if name.text.upper() in ts_xml.db_optional_reserved:
            bad_names.append(name.text.upper())
    assert bad_names == [], \
        "Optional database Reserved Words used one or more times: " + \
        str(bad_names)
