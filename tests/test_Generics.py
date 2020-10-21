#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


def get_salgenerics_file():
    sal_generics_file = ts_xml.get_sal_interfaces_dir() / "SALGenerics.xml"
    return sal_generics_file


def check_for_issues(csc, topic):
    jira = ""
    return jira


def test_salgenerics_topics():
    """Test that SALGenerics.xml defines the expected set of generic topics."""
    sal_generics_file = get_salgenerics_file()
    # Check for known issues.
    jira = check_for_issues("none", "generic_topics")
    if jira:
        pytest.skip(jira + ": " + str(sal_generics_file.name))
    # Test SALGenerics.xml contains the expected commands.
    with open(str(sal_generics_file), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    required_prefix = "SALGeneric_"
    topic_name_start_ind = len(required_prefix)
    topics = set()

    command_prefix = required_prefix + "command_"
    for topic in root.findall("./SALCommandSet/SALCommand/EFDB_Topic"):
        assert topic.text.startswith(
            command_prefix
        ), f"Generic command '{topic.text}' does not start with '{command_prefix}'"
        topics.add(topic.text[topic_name_start_ind:])

    event_prefix = required_prefix + "logevent_"
    for topic in root.findall("./SALEventSet/SALEvent/EFDB_Topic"):
        assert topic.text.startswith(
            event_prefix
        ), f"Generic event '{topic.text}' does not start with '{event_prefix}'"
        topics.add(topic.text[topic_name_start_ind:])
    assert sorted(topics) == sorted(ts_xml.generic_topics)


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
        saltype = "SAL" + topic.rstrip("s")
        # Check for known issues.
        jira = check_for_issues(csc, topic)
        if jira:
            pytest.skip(jira + ": " + str(xmlfile.name))
        # Verify no explicitly defined generic topics.
        with open(str(xmlfile), "r", encoding="utf-8") as f:
            tree = et.parse(f)
        root = tree.getroot()
        csc_topics = set()
        topic_name_start_ind = len(csc) + 1
        for topic in root.findall(f"./{saltype}/EFDB_Topic"):
            csc_topics.add(topic.text[topic_name_start_ind:])
        assert ts_xml.generic_topics & csc_topics == set()
