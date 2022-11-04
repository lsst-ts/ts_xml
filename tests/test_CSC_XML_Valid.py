#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from lxml import etree
import lsst.ts.xml as ts_xml


def check_for_issues(csc, topic):
    if csc == "WeatherForecast":
        jira = "DM-36801"
    else:
        jira = ""
    return jira


def get_xml_schema(saltype):
    datadir = ts_xml.get_data_dir()
    xmlschema_doc = etree.parse(f"{datadir}/schema/{saltype}Set.xsd")
    xmlschema = etree.XMLSchema(xmlschema_doc)
    return xmlschema


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_csc_xml_valid(xmlfile, csc, topic):
    """Test that the CSC XML files are valid and conform to the schema.

    Parameters
    ----------
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xmlfile.stem`
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
