#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import re
import pytest
import xml.etree.ElementTree as ET
import xml_common

def check_for_issues(csc, topic):
	if csc == "Hexapod" and (topic == "Telemetry"):
		jira="DM-20971"
	elif csc == "MTMount" and (topic == "Telemetry"):
		jira="DM-17276"
	elif csc == "Rotator" and (topic == "Telemetry"):
		jira="DM-20969"
	else:
		jira=""
	return jira

@pytest.mark.parametrize("xmlfile,csc,topic", xml_common.get_xmlfile_csc_topic())
def test_attribute_naming(xmlfile,csc,topic):
	"""Test that the <EFDB_Name> field for topic attributes is properly formed, 
	i.e. it begins with a lowercase letter and contains only alphanumeric 
	and underscore characters.
	
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
	# Test the attribute <Description> fields.
	with open(str(xmlfile), "r", encoding="utf-8") as f:
		tree = ET.parse(f)
	root = tree.getroot()
	for name in root.findall(f"./{saltype}/item/EFDB_Name"):
		# re.match() returns None if the string does not match the regex.
		assert re.match(r"^[a-z]([a-zA-Z0-9_]*$)",name.text) is not None, \
		name.text + ' in ' + str(xmlfile.name) + ' does not begin with a lowercase '\
		'letter and/or contains non-alphanumeric characters.'

