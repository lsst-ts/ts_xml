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

def skip_if_known_issue(test, csc):
	sal_subsystems_file = get_salsubsystems_file()
	jira=""
	if jira:
		pytest.skip(jira + f": {csc}")

def get_file_root_element():
	sal_subsystems_file = get_salsubsystems_file()
	with open(str(sal_subsystems_file), "r", encoding="utf-8") as f:
		tree = ET.parse(f)
	root = tree.getroot()
	return root

def get_csc_generics():
	sal_subsystems_file = get_salsubsystems_file()
	root = get_file_root_element()
	arguments = []
	for csc in xml_common.subsystems:
		generics = root.find("./Subsystem/[Name='" + csc + "']/Generics").text
		arguments.append((root,csc,generics))
	return arguments

def get_csc_simulator():
	sal_subsystems_file = get_salsubsystems_file()
	root = get_file_root_element()
	arguments = []
	for csc in xml_common.subsystems:
		simulator = root.find("./Subsystem/[Name='" + csc + "']/Simulator").text
		arguments.append((root,csc,simulator))
	return arguments

#==================
## Tests
#==================

def test_salsubsystems_count():
	"""Test that SALSubsystems.xml defines the expected number of CSCs. 
	
	Parameters
	----------
	sal_subsystems_file: `pathlib.Path(sal_interfaces/SALSubsystems.xml)`
		The file being tested
	subsystems: `xml_common.subsystems`
		The list of expected CSCs.
	"""
	# Check for known issues.
	skip_if_known_issue("count", "none")
	# Test SALGenerics.xml contains the expected commands.
	root = get_file_root_element()
	assert len(root.findall("./Subsystem/Name")) == len(xml_common.subsystems), \
	"There is an unexpected number of CSCs."

def test_salsubsystems_uniq_cscs():
	"""Test that SALSubsystems.xml does not contain duplicate CSCs. 

	Parameters
	----------
	sal_subsystems_file: `pathlib.Path(sal_interfaces/SALSubsystems.xml)`
		The file being tested
	subsystems: `xml_common.subsystems`
		The list of expected CSCs.
	"""
	# Check for known issues.
	skip_if_known_issue("uniq", "none")
	# Test SALGenerics.xml contains unique CSCs.
	root = get_file_root_element()
	assert len(root.findall("./Subsystem/Name")) == len(set(root.findall("./Subsystem/Name"))) \
	and len(xml_common.subsystems) == len(set(xml_common.subsystems)), \
	"SALSubsystems.xml or xml_common.subsystems contains duplicate entries"

def test_each_csc_defined():
	"""Test that SALSubsystems.xml defines the expected set of CSCs. 
	
	Parameters
	----------
	sal_subsystems_file: `pathlib.Path(sal_interfaces/SALSubsystems.xml)`
		Full filepath to SALSubsystems.xml dictionary file.   
	csc : `xml_common.subsystems`
		Name of the CSC
	"""
	# Check for known issues.
	skip_if_known_issue("defined", "none")
	# Verify each CSC is explicitly defined.
	root = get_file_root_element()
	subsystems = xml_common.subsystems
	subsystems.sort()
	cscs = []
	for csc in root.findall(f"./Subsystem/Name"):
		cscs.append(csc.text)
	cscs.sort()
	assert xml_common.subsystems == cscs, "There is a duplicate CSC."

@pytest.mark.parametrize("root,csc,generics", get_csc_generics())
def test_generics_tag(root,csc,generics):
	"""Test that the <Generics> tag is correctly defined for each CSC. 
	
	Parameters
	----------
	sal_subsystems_file: `pathlib.Path(sal_interfaces/SALSubsystems.xml)`
		Full filepath to SALSubsystems.xml dictionary file.   
	csc : `xml_common.subsystems`
		Name of the CSC
	"""
	# Check for known issues.
	skip_if_known_issue("generics", csc)
	# Set the condition to no for the CSCs that do not utilize the Generic topics.
	if csc == "Script":
		value="no"
	elif csc == "LOVE":
		value="no"
	else:
		value="yes"
	# Verify each CSC is explicitly defined.
	assert root.find("./Subsystem/[Name='" + csc + "']/Generics").text == value, \
		csc + " <Generics> tag is not defined as expected."

@pytest.mark.parametrize("root,csc,simulator", get_csc_simulator())
def test_simulator_tag(root,csc,simulator):
	"""Test that the <Simulator> tag is correctly defined for each CSC. 
	
	Parameters
	----------
	sal_subsystems_file: `pathlib.Path(sal_interfaces/SALSubsystems.xml)`
		Full filepath to SALSubsystems.xml dictionary file.   
	csc : `xml_common.subsystems`
		Name of the CSC
	"""
	# Check for known issues.
	skip_if_known_issue("simulator", csc)
	# Verify each CSC is explicitly defined.
	assert type(root.find("./Subsystem/[Name='" + csc + "']/Simulator")) is ET.Element, \
		csc + " <Simulator> tag is NOT defined."

