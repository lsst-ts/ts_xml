#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from lxml import etree
import lsst.ts.xml as ts_xml


def get_xml_schema(saltype):
    pkgroot = ts_xml.get_pkg_root()
    xmlschema_doc = etree.parse(f"{pkgroot}/schema/{saltype}Set.xsd")
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
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = etree.parse(f)
    try:
        xmlschema.assertValid(tree)
    except etree.DocumentInvalid as err:
        assert False, f"{xmlfile.name}: {err}"
