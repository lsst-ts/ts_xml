#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et

import lsst.ts.xml as ts_xml
import pytest


def check_for_issues(csc, topic):
    return ""


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_attribute_description(xmlfile, csc, topic):
    """Tests the <Description> field for topic attributes \
    is properly defined, i.e. it is not blank.

    Parameters
    ----------
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xmlfile.stem`
        One of ['Commands','Events','Telemetry']
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    """
    saltype = "SAL" + topic.rstrip("s")
    # Check for known issues.
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(f"{jira}: {csc}_{topic}.xml contains blank <Description> fields.")
    # Test the attribute <Description> fields.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    for description in root.findall(f"./{saltype}/item/Description"):
        assert description.text is not None, "Description cannot be blank."
        assert (
            description.text.replace(" ", "") != ""
        ), "Description cannot contain only whitespace."
