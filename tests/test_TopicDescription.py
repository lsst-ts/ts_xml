#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
import xml.etree.ElementTree as et

import lsst.ts.xml as ts_xml
import pytest


def check_for_issues(csc: str, topic: str) -> str:
    match f"{csc}-{topic}":
        case _:
            return ""


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_topic_description(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Tests the <Description> field for topic attributes \
    is properly defined, i.e. it is not blank.

    Parameters
    ----------
    csc : `csc`
        Name of the CSC
    topic : `str`
        One of ['Commands','Events','Telemetry']
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    """
    saltype = "SAL" + topic.rstrip("s")

    # Test the topic <Description> fields.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    faulty_descriptions = []
    for element in root.findall(f"./{saltype}"):
        name = element.find("EFDB_Topic")
        assert name is not None
        assert name.text is not None
        description = element.find("Description")
        if description is None:
            faulty_descriptions.append(f"Topic {name.text} requires a description.")
        elif description.text is None:
            faulty_descriptions.append(f"Description of {name.text} cannot be blank.")
        elif description.text.replace(" ", "") == "":
            faulty_descriptions.append(
                f"Description of {name.text} cannot contain only whitespace."
            )

    # Check for known issues.
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(
            f"{jira}: {csc}_{topic}.xml requires the following "
            f"description improvements: {faulty_descriptions}."
        )
    else:
        assert len(faulty_descriptions) == 0, f"{faulty_descriptions}"
