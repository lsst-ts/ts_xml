#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import pathlib
import pytest
import xml.etree.ElementTree as ET
import xml_common

def check_for_issues(csc, topic):
	if csc == "Hexapod" and (topic == "Events" or topic == "Telemetry"):
		jira="DM-20971"
	elif csc == "ATCamera" and (topic == "Events" or topic == "Telemetry"):
		jira="CAP-318"
	elif csc == "MTCamera" and (topic == "Events" or topic == "Telemetry"):
		jira="CAP-318"
	elif csc == "MTMount" and (topic == "Commands"):
		jira="DM-17276"
	elif csc == "MTEEC" and (topic == "Commands"):
		jira="CAP-374"
	elif csc == "MTM1M3":
		jira="DM-20956"
	else:
		jira=""
	return jira

def get_csc_xmlfile_topic():
	pkgroot = pathlib.Path(__file__).resolve().parents[1]
	arguments = []
	for csc in xml_common.subsystems:
		xml_path = pkgroot / "sal_interfaces" / csc
		for xmlfile in xml_path.glob(f"{csc}_*.xml"):
			topic = xmlfile.stem.split("_")[1]
			arguments.append((csc,xmlfile,topic))
	return arguments

@pytest.mark.parametrize("csc,xmlfile,topic", get_csc_xmlfile_topic())
def test_attribute_description(csc,topic,xmlfile):
	"""Test that the <Description> field for topic attributes is properly defined, i.e. it is not blank.
	
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
		pytest.skip(jira + ": " + csc + "_" + topic + ".xml contains blank <Description> fields.")
	# Test the attribute <Description> fields.
	with open(str(xmlfile), "r", encoding="utf-8") as f:
		tree = ET.parse(f)
		root = tree.getroot()
		for description in root.findall(f"./{saltype}/item/Description"):
			assert description.text.replace(" ", "") != None

