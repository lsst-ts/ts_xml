#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_count(xmlfile, csc, topic):
    """Test that the <Count> is properly defined.

    Count must be present, must be a positive integer,
    and must be 1 for string fields.

    Parameters
    ----------
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xml_file.stem`
        One of ['Commands','Events','Telemetry']
    xml_file : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    """
    saltype = "SAL" + topic.rstrip("s")
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
        root = tree.getroot()
        for attrib in root.findall(f"./{saltype}/item"):
            count = attrib.find("Count")
            assert (
                count.text is not None
            ), f"The <Count> tag cannot be blank: {xmlfile.name}"
            assert count.text.isdigit()
            int_count = int(count.text)
            assert int_count > 0
            idltype = attrib.find("IDL_Type")
            assert idltype is not None
            if idltype is not None and idltype.text == "string":
                assert (
                    int_count == 1
                ), f"The <Count> for a string must be 1, not {count.text}: {xmlfile.name}"
