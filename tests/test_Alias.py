#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_aliases(xmlfile, csc, topic):
    """Test that the <Alias> conforms to the <EFDB_Topic>.

    Telemetry files are excluded because telemetry topics have no aliases.

    Parameters
    ----------
    csc : `testutils.subsystems`
        Name of the CSC
    message_type : `xml_file.stem`
        One of ['Commands','Events']
    xml_file : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    """
    if topic == "Telemetry":
        pass
    else:
        saltype = "SAL" + topic.rstrip('s')
        with open(str(xmlfile), "r", encoding="utf-8") as f:
            tree = et.parse(f)
        root = tree.getroot()
        csc_aliases = set(alias.text for alias in root.findall(f"./{saltype}/Alias"))
        csc_topics = set(topic.text.split('_', 2)[2] for topic in root.findall(f"./{saltype}/EFDB_Topic"))
        assert csc_aliases == csc_topics
