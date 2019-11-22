#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import pytest
import xml.etree.ElementTree as ET
import xml_common

def check_for_issues(csc, topic):
	jira=""
	return jira

@pytest.mark.parametrize("xmlfile,csc,topic", xml_common.get_xmlfile_csc_topic())
def test_no_reserved_words(xmlfile,csc,topic):
	"""Test that the <EFDB_Name> field does not use any Reserved Words.
	
	Parameters
	----------
	xmlfile : `pathlib.Path`
		Full filepath to the Commands or Events XML file for the CSC.	
	csc : `xml_common.subsystems`
		Name of the CSC
	topic : `xmlfile.stem`
		One of ['Commands','Events','Telemetry']
	"""
	saltype = "SAL" + topic.rstrip('s')
	# Check for known issues.
	jira = check_for_issues(csc, topic)
	if jira:
		pytest.skip(jira + ": " + str(xmlfile.name) + " <EFDB_Name> is not properly formed.")
	# Test the <EFDB_Name> fields do not use Reserved Words.
	with open(str(xmlfile), "r", encoding="utf-8") as f:
		tree = ET.parse(f)
	root = tree.getroot()
	for name in root.findall(f"./{saltype}/item/EFDB_Name"):
		assert name.text.upper() not in set(xml_common.idl_reserved + xml_common.db_reserved), \
		'Reserved Word ' + name.text + ' used one or more times.'

