#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import pathlib
import pytest
import xml.etree.ElementTree as ET
import lsst.ts.xml as ts_xml 

@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.test_utils.get_xmlfile_csc_topic())
def test_count(csc,message_type,xml_file):
	"""Test that the <Count> is properly defined, i.e. it is not blank.
	
	Parameters
	----------
	csc : `test_utils.subsystems`
		Name of the CSC
	message_type : `xml_file.stem`
		One of ['Commands','Events','Telemetry']
	xml_file : `pathlib.Path`
		Full filepath to the Commands or Events XML file for the CSC.	
	"""
	saltype = "SAL" + message_type.rstrip('s')
	with open(str(xmlfile), "r", encoding="utf-8") as f:
		tree = ET.parse(f)
		root = tree.getroot()
		for count in root.findall(f"./{saltype}/item/Count"):
			if count.text:
				assert count.text.isnumeric()
			else:
				assert False, "The <Count> tag cannot be blank: " + xmlfile.name

