#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import pathlib
import pytest
import xml.etree.ElementTree as ET
import xml_common

def get_arguments():
	pkgroot = pathlib.Path(__file__).resolve().parents[1]
	arguments = []
	for csc in xml_common.subsystems:
		xml_path = pkgroot / "sal_interfaces" / csc
		for xml_file in xml_path.glob(f"{csc}_*.xml"):
			message_type = xml_file.stem.split("_")[1]
			if message_type == "Telemetry":
				# Telemetry topics have no <Alias> tag.
				continue
			arguments.append((csc,xml_file,message_type))
	return arguments

@pytest.mark.parametrize("csc,xml_file,message_type", get_arguments())
def test_aliases(csc,message_type,xml_file):
	"""Test that the <Alias> conforms to the <EFDB_Topic>.
	
	Telemetry files are excluded because telemetry topics have no aliases.

	Parameters
	----------
	csc : `xml_common.subsystems`
		Name of the CSC
	message_type : `xml_file.stem`
		One of ['Commands','Events']
	xml_file : `pathlib.Path`
		Full filepath to the Commands or Events XML file for the CSC.	
	"""
	saltype = "SAL" + message_type.rstrip('s')
	with open(str(xml_file), "r", encoding="utf-8") as f:
		tree = ET.parse(f)
		root = tree.getroot()
		csc_aliases = set(alias.text for alias in root.findall(f"./{saltype}/Alias"))
		csc_topics = set(topic.text.split('_', 2)[2] for topic in root.findall(f"./{saltype}/EFDB_Topic"))
		assert csc_aliases == csc_topics
