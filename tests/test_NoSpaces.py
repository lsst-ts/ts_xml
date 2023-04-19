#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
import re
import xml.etree.ElementTree as et

import lsst.ts.xml as ts_xml
import pytest


def check_for_issues(csc: str, topic: str) -> str:
    jira = ""
    return jira


def check_subsystem(
    xmlfile: pathlib.Path, saltype: str, element_root: et.Element
) -> None:
    for subsystem in element_root.findall(f"./{saltype}/Subsystem"):
        assert subsystem.text is not None
        assert (
            re.search(r"\s", subsystem.text) is None
        ), f"<Subsystem> '{subsystem.text}' in {xmlfile.name} contains a whitespace character."


def check_topic(xmlfile: pathlib.Path, saltype: str, element_root: et.Element) -> None:
    for topic in element_root.findall(f"./{saltype}/EFDB_Topic"):
        assert topic.text is not None
        assert (
            re.search(r"\s", topic.text) is None
        ), f"<EFDB_Topic> '{topic.text}' in {xmlfile.name} contains a whitespace character."


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_no_spaces(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Test that the <Subsystem>, <EFDB_Topic> and <EFDB_Name> tags
    do not contain any whitespace.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `str`
        Name of the CSC
    topic : `str`
        One of ['Commands','Events','Telemetry']
    """
    saltype = "SAL" + topic.rstrip("s")
    # Check for known issues.
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(
            f"{jira}: {xmlfile.name}.xml <Subsystem> field contains whitespace."
        )
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    check_subsystem(xmlfile, saltype, root)
    check_topic(xmlfile, saltype, root)
    for name in root.findall(f"./{saltype}/item/EFDB_Name"):
        assert name.text is not None
        assert (
            re.search(r"\s", name.text) is None
        ), f"<EFDB_Name> {name.text!r} in {xmlfile.name} contains a whitespace character."
