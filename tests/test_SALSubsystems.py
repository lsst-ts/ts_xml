#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import pathlib
import pytest
import xml.etree.ElementTree as ET
import xml_common

def get_salsubsystems_file():
	pkgroot = pathlib.Path(__file__).resolve().parents[1]
	sal_subsystems_file = pkgroot / "sal_interfaces/SALSubsystems.xml"
	return sal_subsystems_file

def check_for_issues(csc, topic):
	jira=""
	return jira

def test_salsubsystems_count():
	"""Test that SALSubsystems.xml defines the expected number of CSCs. 
	
	Parameters
	----------
	sal_subsystems_file: `pathlib.Path(sal_interfaces/SALSubsystems.xml)`
		The file being tested
	"""
	sal_subsystems_file = get_salsubsystems_file()
	# Check for known issues.
	jira = check_for_issues("none", "generic_commands")
	if jira:
		pytest.skip(jira + ": " + str(sal_generics_file.name))
	# Test SALGenerics.xml contains the expected commands.
	with open(str(sal_subsystems_file), "r", encoding="utf-8") as f:
		tree = ET.parse(f)
	root = tree.getroot()
	assert len(root.findall("./Subsystem/Name")) == len(xml_common.subsystems), \
	"There is an unexpected number of CSCs."

#@pytest.mark.parametrize("xmlfile,csc,topic", xml_common.get_xmlfile_csc_topic())
#def test_xmlfiles_do_not_define_generic_topics(xmlfile,csc,topic):
	#"""Test that CSC XML files do not define any of the generic topics. 
#	
	#NOTE: Telemetry is skipped because there is no generic telemetry.
#
	#Parameters
	#----------
	#generic_commands : `xml_common.generic_commands`
		#The list of Generic Commands
	#generic_events : `xml_common.generic_events`
		#The list of Generic Events
	#xmlfile : `pathlib.Path`
		#Full filepath to the Commands or Events XML file for the CSC.   
	#csc : `xml_common.subsystems`
		#Name of the CSC
	#topic : `xmlfile.stem`
		#One of ['Commands','Events']
	#"""
	#if topic == "Telemetry":
		#pass
	#else:
		#saltype = "SAL" + topic.rstrip('s')
		## Check for known issues.
		#jira = check_for_issues(csc, topic)
		#if jira:
			#pytest.skip(jira + ": " + str(xmlfile.name))
		## Verify no explicitly defined generic topics.
		#with open(str(xmlfile), "r", encoding="utf-8") as f:
			#tree = ET.parse(f)
		#root = tree.getroot()
		#csc_topics = []
		#for alias in root.findall(f"./{saltype}/Alias"):
			#csc_topics.append(alias.text)
		#for topic in csc_topics:
			#assert topic not in set(xml_common.generic_commands + xml_common.generic_events)
