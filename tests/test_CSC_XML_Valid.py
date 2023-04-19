#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib

import lsst.ts.xml as ts_xml
import pytest
from lxml import etree


def check_for_issues(csc: str, topic: str) -> str:
    jira = ""
    return jira


def get_xml_schema(saltype: str) -> etree.XMLSchema:
    datadir = ts_xml.get_data_dir()
    xmlschema_doc = etree.parse(f"{datadir}/schema/{saltype}Set.xsd")
    xmlschema = etree.XMLSchema(xmlschema_doc)
    return xmlschema


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_csc_xml_valid(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Test that the CSC XML files are valid and conform to the schema.

    Parameters
    ----------
    csc : `csc`
        Name of the CSC
    topic : `str`
        One of ['Commands','Events','Telemetry']
    xmlfile : `pathlib.Path`
        Full filepath to each XML file for the CSC.
    xmlschema : `pathlib.Path`
        Full filepath to schema XSD file for the xmlfile.
    """
    saltype = "SAL" + topic.rstrip("s")
    xmlschema = get_xml_schema(saltype)
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(f"{jira}: {xmlfile.name} Does not conform to XML schema.")
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = etree.parse(f)
    try:
        xmlschema.assertValid(tree)
    except etree.DocumentInvalid as err:
        assert False, f"{xmlfile.name}: {err}"
