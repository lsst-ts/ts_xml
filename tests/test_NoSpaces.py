#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import re
import pathlib
import pytest
import xml.etree.ElementTree as ET
import xml_common

def check_for_issues(csc, topic):
	jira=""
	return jira

def get_xmlfile_csc_topic():
	pkgroot = pathlib.Path(__file__).resolve().parents[1]
	arguments = []
	for csc in xml_common.subsystems:
		xml_path = pkgroot / "sal_interfaces" / csc
		for xmlfile in xml_path.glob(f"{csc}_*.xml"):
			topic = xmlfile.stem.split("_")[1]
			arguments.append((xmlfile,csc,topic))
	return arguments

@pytest.mark.parametrize("xmlfile,csc,topic", get_xmlfile_csc_topic())
def test_no_spaces(xmlfile,csc,topic):
	"""Test that the <Subsystem>, <EFDB_Topic> and <EFDB_Name> tags \
	do not contain any whitespace..
	
	Parameters
	----------
	csc : `xml_common.subsystems`
		Name of the CSC
	topic : `xmlfile.stem`
		One of ['Commands','Events','Telemetry']
	xmlfile : `pathlib.Path`
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
		for subsystem in root.findall(f"./{saltype}/Subsystem"):
			assert re.search(r"\s", subsystem.text) is None, "'" + subsystem.text + "'" + \
			' in ' + str(xmlfile.name) + ' contains a whitespace character.'

