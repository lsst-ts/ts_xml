#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import re
import pytest
import xml.etree.ElementTree as ET
import lsst.ts.xml as ts_xml

def check_for_issues(csc, topic):
	jira=""
	return jira

@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.test_utils.get_xmlfile_csc_topic())
def test_no_spaces(xmlfile,csc,topic):
	"""Test that the <Subsystem>, <EFDB_Topic> and <EFDB_Name> tags \
	do not contain any whitespace..
	
	Parameters
	----------
	csc : `test_utils.subsystems`
		Name of the CSC
	topic : `xmlfile.stem`
		One of ['Commands','Events','Telemetry']
	xmlfile : `test_utils.pathlib.Path`
		Full filepath to the Commands or Events XML file for the CSC.	
	"""
	saltype = "SAL" + topic.rstrip('s')
	# Check for known issues.
	jira = check_for_issues(csc, topic)
	if jira:
		pytest.skip(jira + ": " + str(xmlfile.name) + ".xml <Subsystem> field contains whitespace.")
	with open(str(xmlfile), "r", encoding="utf-8") as f:
		tree = ET.parse(f)
	root = tree.getroot()
	check_subsystem(saltype, root)
	check_topic(saltype, root)
	for name in root.findall(f"./{saltype}/item/EFDB_Name"):
		assert re.search(r"\s", name.text) is None, f"<EFDB_Name> " + \
		"'" + name.text + "' in " + str(xmlfile.name) + \
		" contains a whitespace character."

def check_subsystem(saltype, element_root):
	for subsystem in element_root.findall(f"./{saltype}/Subsystem"):
		assert re.search(r"\s", subsystem.text) is None, f"<Subsystem> " + \
		"'" + subsystem.text + "' in " + str(xmlfile.name) + \
		" contains a whitespace character."

def check_topic(saltype, element_root):
	for topic in element_root.findall(f"./{saltype}/EFDB_Topic"):
		assert re.search(r"\s", topic.text) is None, f"<EFDB_Topic> " + \
		"'" + topic.text + "' in " + str(xmlfile.name) + \
		" contains a whitespace character."

