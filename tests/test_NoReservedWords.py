#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


def check_for_issues(csc, topic):
    if csc == "ATAOS" and topic == "Commands":
        jira = "DM-22612"
    elif csc == "ATMCS" and (topic == "Commands" or topic == "Events"):
        jira = "DM-22613"
    elif csc == "ATSpectrograph" and (topic == "Commands" or topic == "Events"):
        jira = "DM-22614"
    elif csc == "CatchupArchiver" and (topic == "Telemetry" or topic == "Events"):
        jira = "CAP-399"
    elif csc == "FiberSpectrograph" and topic == "Commands":
        jira = "DM-22616"
    elif csc == "LOVE" and topic == "Events":
        jira = "DM-22617"
    elif csc == "MTAOS" and topic == "Telemetry":
        jira = "DM-22618"
    elif csc == "MTArchiver" and topic == "Events":
        jira = "CAP398"
    elif csc == "MTCamera" and topic == "Commands":
        jira = "CAP-397"
    elif csc == "MTM1M3" and topic == "Telemetry":
        jira = "DM-22621"
    elif csc == "MTMount" and topic == "Commands":
        jira = "DM-22622"
    elif csc == "OCS" and (topic == "Telemetry" or topic == "Events"):
        jira = "DM-22623"
    elif csc == "PromptProcessing" and (topic == "Telemetry" or topic == "Events"):
        jira = "DM-22624"
    elif csc == "Scheduler" and topic == "Telemetry":
        jira = "DM-22625"
    elif csc == "Script" and topic == "Events":
        jira = "DM-22626"
    elif csc == "Test" and topic == "Commands":
        jira = "DM-22627"
    elif csc == "Watcher" and (topic == "Commands" or topic == "Events"):
        jira = "DM-22628"
    else:
        jira = ""
    return jira


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_no_reserved_words(xmlfile, csc, topic):
    """Test that the <EFDB_Name> field does not use any Reserved Words.

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
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(jira + ": " + str(xmlfile.name) + " <EFDB_Name> is not properly formed.")
    # Test the <EFDB_Name> fields do not use Reserved Words.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    bad_names = []
    for name in root.findall(f"./{saltype}/item/EFDB_Name"):
        if name.text.upper() in set(ts_xml.idl_reserved + ts_xml.db_reserved):
            bad_names.append(name.text.upper())
    assert bad_names == [], \
        "Reserved Words used one or more times: " + str(bad_names)
