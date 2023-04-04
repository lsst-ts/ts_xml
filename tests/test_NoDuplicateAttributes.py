#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et

import lsst.ts.xml as ts_xml
import pytest


def check_for_issues(csc, topic):
    jira = ""
    return jira


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_no_spaces(xmlfile, csc, topic):
    """Test that, for each <EFDB_Topic>, there are no duplicate \
    <item>/<EFDB_Name> values.

    Parameters
    ----------
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xmlfile.stem`
        One of ['Commands','Events','Telemetry']
    xmlfile : `testutils.pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    """
    saltype = "SAL" + topic.rstrip("s")
    # Check for known issues.
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(
            f"{jira}: {xmlfile.name}.xml <EFDB_Topic> contains duplicate attributes."
        )
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    for efdb_topic in root.findall(f"./{saltype}/EFDB_Topic"):
        attributes = []
        for item in root.findall(
            f"./{saltype}/[EFDB_Topic='{efdb_topic.text}']/item/EFDB_Name"
        ):
            attributes.append(item.text)
        assert len(attributes) == len(
            set(attributes)
        ), f"The {efdb_topic.text} topic contains duplicate attributes."
