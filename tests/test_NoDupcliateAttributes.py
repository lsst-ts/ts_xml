#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import re
import pytest
import xml.etree.ElementTree as ET
import xml_common

def check_for_issues(csc, topic):
	jira=""
	return jira

@pytest.mark.parametrize("xmlfile,csc,topic", xml_common.get_xmlfile_csc_topic())
def test_no_spaces(xmlfile,csc,topic):
	"""Test that, for each <EFDB_Topic>, there are no duplicate <item>/<EFDB_Name> values.
	
	Parameters
	----------
	csc : `xml_common.subsystems`
		Name of the CSC
	topic : `xmlfile.stem`
		One of ['Commands','Events','Telemetry']
	xmlfile : `xml_common.pathlib.Path`
		Full filepath to the Commands or Events XML file for the CSC.	
	"""
	saltype = "SAL" + topic.rstrip('s')
	# Check for known issues.
	jira = check_for_issues(csc, topic)
	if jira:
		pytest.skip(jira + ": " + str(xmlfile.name) + ".xml <EFDB_Topic> contains duplicate attributes.")
	with open(str(xmlfile), "r", encoding="utf-8") as f:
		tree = ET.parse(f)
	root = tree.getroot()
	for efdb_topic in root.findall(f"./{saltype}/EFDB_Topic"):
		attributes = []
		for item in root.findall(f"./{saltype}/[EFDB_Topic='" + efdb_topic.text + "']/item/EFDB_Name"):
			attributes.append(item.text)
		assert len(attributes) == len(set(attributes)), \
			"The " + efdb_topic.text + " topic contains duplicate attributes."

