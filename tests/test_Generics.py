#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


def get_salgenerics_file():
    pkgroot = pathlib.Path(__file__).resolve().parents[1]
    sal_generics_file = pkgroot / "sal_interfaces/SALGenerics.xml"
    return sal_generics_file


def check_for_issues(csc, topic):
    if csc == "LOVE" and topic == "Events":
        jira = "DM-22109"
    elif csc == "Script" and (topic == "Commands" or topic == "Events"):
        jira = "DM-22329"
    else:
        jira = ""
    return jira


def test_salgenerics_commands():
    """Test that SALGenerics.xml defines the expected set of generic commands.
    """
    sal_generics_file = get_salgenerics_file()
    # Check for known issues.
    jira = check_for_issues("none", "generic_commands")
    if jira:
        pytest.skip(jira + ": " + str(sal_generics_file.name))
    # Test SALGenerics.xml contains the expected commands.
    with open(str(sal_generics_file), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    commands = []
    for command in root.findall(f"./SALCommandSet/SALCommand/Alias"):
        commands.append(command.text)
    commands.sort()
    ts_xml.generic_commands.sort()
    assert commands == ts_xml.generic_commands


def test_salgenerics_events():
    """Test that SALGenerics.xml defines the expected set of generic events.
    """
    sal_generics_file = get_salgenerics_file()
    # Check for known issues.
    jira = check_for_issues("none", "generic_events")
    if jira:
        pytest.skip(jira + ": " + str(sal_generics_file.name))
    # Test SALGenerics.xml contains the expected commands.
    with open(str(sal_generics_file), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    events = []
    for event in root.findall(f"./SALEventSet/SALEvent/Alias"):
        events.append(event.text)
    events.sort()
    ts_xml.generic_events.sort()
    assert events == ts_xml.generic_events


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_xmlfiles_do_not_define_generic_topics(xmlfile, csc, topic):
    """Test that CSC XML files do not define any of the generic topics.

    NOTE: Telemetry is skipped because there is no generic telemetry.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xmlfile.stem`
        One of ['Commands','Events']
    """
    if topic == "Telemetry":
        pass
    else:
        saltype = "SAL" + topic.rstrip('s')
        # Check for known issues.
        jira = check_for_issues(csc, topic)
        if jira:
            pytest.skip(jira + ": " + str(xmlfile.name))
        # Verify no explicitly defined generic topics.
        with open(str(xmlfile), "r", encoding="utf-8") as f:
            tree = et.parse(f)
        root = tree.getroot()
        csc_topics = []
        for alias in root.findall(f"./{saltype}/Alias"):
            csc_topics.append(alias.text)
        for topic in csc_topics:
            assert topic not in set(ts_xml.generic_commands + ts_xml.generic_events)
