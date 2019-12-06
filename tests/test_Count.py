#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_count(xmlfile, csc, topic):
    """Test that the <Count> is properly defined, i.e. it is not blank.

    Parameters
    ----------
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xml_file.stem`
        One of ['Commands','Events','Telemetry']
    xml_file : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    """
    saltype = "SAL" + topic.rstrip('s')
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
        root = tree.getroot()
        for count in root.findall(f"./{saltype}/item/Count"):
            if count.text:
                assert count.text.isnumeric()
            else:
                assert False, "The <Count> tag cannot be blank: " + xmlfile.name
