#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


def check_for_issues(csc, topic, language):
    if csc == "ATAOS" and topic == "Commands" and language == "optional":
        jira = "DM-22612"
    elif csc == "ATMCS" and topic in ("Commands", "Events") and language == "critical":
        jira = "DM-22613"
    elif (
        csc == "ATSpectrograph"
        and topic in ("Commands", "Events")
        and language == "optional"
    ):
        jira = "DM-22614"
    elif (
        csc == "CatchupArchiver"
        and topic in ("Telemetry", "Events")
        and language == "optional"
    ):
        jira = "CAP-399"
    elif csc == "FiberSpectrograph" and topic == "Commands" and language == "optional":
        jira = "DM-22616"
    elif csc == "LOVE" and topic == "Events" and language == "optional":
        jira = "DM-22617"
    elif csc == "ATCamera" and language == "optional":
        jira = "CAP-793"
    elif csc == "MTCamera" and language == "optional":
        jira = "CAP-397"
    elif csc == "CCCamera" and language == "optional":
        jira = "CAP-402"
    elif (
        csc == "PromptProcessing"
        and topic in ("Telemetry", "Events")
        and language == "optional"
    ):
        jira = "DM-22624"
    elif csc == "Scheduler" and topic == "Telemetry" and language == "optional":
        jira = "DM-22625"
    elif (
        csc in ("Script", "ScriptQueue")
        and topic == "Events"
        and language == "optional"
    ):
        jira = "DM-22626"
    elif csc == "Test" and topic == "Commands" and language == "optional":
        jira = "DM-22627"
    elif (
        csc == "Watcher" and topic in ("Commands", "Events") and language == "optional"
    ):
        jira = "DM-22628"
    else:
        jira = ""
    return jira


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_reserved_words(xmlfile, csc, topic):
    """Control function to execute the IDL, and
    database reserved words tests.
    """
    for restriction in ("idl", "critical", "optional"):
        reserved_words(xmlfile, csc, topic, restriction)


def reserved_words(xmlfile, csc, topic, restriction):
    """Test that the <EFDB_Name> field does not use any Reserved Words.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xmlfile.stem`
        One of ['Commands', 'Events', 'Telemetry']
    restriction : `test_reserved_words.restriction`
        One of ['idl', 'critical', 'optional']
    """
    saltype = "SAL" + topic.rstrip("s")
    # Check for known issues.
    jira = check_for_issues(csc, topic, restriction)
    if jira:
        pytest.skip(
            jira
            + ": "
            + str(xmlfile.name)
            + " <EFDB_Name> uses "
            + restriction.upper()
            + " reserved word."
        )
    # Test the <EFDB_Name> fields do not use Reserved Words.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    bad_names = []
    # Set the list based on the restriction type.
    if restriction == "idl":
        word_list = ts_xml.idl_reserved
    elif restriction == "critical":
        word_list = ts_xml.db_critical_reserved
    else:
        word_list = ts_xml.db_optional_reserved
    for name in root.findall(f"./{saltype}/item/EFDB_Name"):
        if name.text.upper() in word_list:
            bad_names.append(name.text.upper())
    assert bad_names == [], (
        restriction.upper()
        + " Reserved Words used one or more times: "
        + str(bad_names)
    )
