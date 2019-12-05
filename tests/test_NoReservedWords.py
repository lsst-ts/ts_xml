#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


def check_for_issues(csc, topic):
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
