#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import os
import unittest
import xml.etree.ElementTree as ET
import xml_common

class TestAliases(unittest.TestCase):

	def setUp(self):
		self.pkgroot = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
		self.sal_interfaces = os.path.join(self.pkgroot, "sal_interfaces")

	def test_aliases(self):
		"""Test that the Alias name matches the EFDB_Topic name."""
		for csc in xml_common.subsystems:
			xml_paths = glob.glob(os.path.join(self.sal_interfaces, csc, f"{csc}_*.xml"))
			for xml_path in xml_paths:
				category = xml_path.split('/')[4].split('_')[1].split('.')[0]
				if category == "Telemetry":
					# Telemetry XML files have no Alias
					continue
				with self.subTest(xml_path=xml_path):
					self.check_aliases(xml_path)    

	def check_aliases(self, xml_path):
		"""Check that the Alias name matches the EFDB_Topic name for all topics in a file."""
		csc_aliases = []
		csc_topics = []
		with open(xml_path, "r", encoding="utf-8") as f:
			tree = ET.parse(f)
			root = tree.getroot()
			csc_aliases = set(alias.text for alias in root.findall('./SALEvent/Alias'))
			csc_topics = set(topic.text.split('_', 2)[2] for topic in root.findall('./SALEvent/EFDB_Topic'))
			differences = csc_aliases ^ csc_topics
			if len(differences) != 0:
				self.fail(f"The aliases and topic names for {xml_path} are not an exact match: "
							f"differences {differences}")

if __name__ == "__main__":
	unittest.main(verbosity=2)
