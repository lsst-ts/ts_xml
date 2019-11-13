#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import glob
import sys
import os
import os.path
cwd = os.getcwd()
sys.path.insert(1, cwd + '/../../tests')
import xml_common

# Create/Open test suite file.
file = open(cwd + "/../../tests/test_AttributeDescription.py","w")

# Create Settings header.
file.write("#!/usr/bin/env python\n")
file.write("# -*- coding: utf-8 -*-\n")
file.write("import os\n")
file.write("import unittest\n")
file.write("import xml.etree.ElementTree as ET\n")
file.write("import xml_common\n")
file.write("\n")

# Create Test Case table.
file.write("class TestAttributeDescriptions(unittest.TestCase):\n\n")

# Verify the Attribute Names conform to naming conventions.
for csc in xml_common.subsystems:

	# Get the list of XMLs for each CSC, to include Telemetry, Events and Commands.
	xmls = glob.glob("../../sal_interfaces/" + csc + "/" + csc + "*")
	for xml in xmls:
		# Get the message type, i.e. Telemetry, Events, Commands.
		messageType = xml.split('/')[4].split('_')[1].split('.')[0]
		# Mark test cases with Jira tickets
		if csc == "Hexapod" and (messageType == "Events" or messageType == "Telemetry"):
			jira="DM-20971"
		elif csc == "ATCamera" and (messageType == "Events" or messageType == "Telemetry"):
			jira="CAP-318"
		elif csc == "MTCamera" and (messageType == "Events" or messageType == "Telemetry"):
			jira="CAP-318"
		elif csc == "MTMount" and (messageType == "Commands"):
			jira="DM-17276"
		elif csc == "MTEEC" and (messageType == "Commands"):
			jira="CAP-374"
		elif csc == "MTM1M3":
			jira="DM-20956"
		else:
			jira=""
		# Create the Test Cases.
		if jira:
			file.write("\t@unittest.skip(\"" + jira + "\")\n")
		file.write("\tdef test_" + csc + messageType + "AttributeDescriptions(self):\n")
		file.write("\t\tself.dir_path = os.path.dirname(os.path.realpath(__file__))\n")
		file.write("\t\tself.file = open(self.dir_path + '/" + xml[3:] + "')\n")
		file.write("\t\tself.tree = ET.parse(self.file)\n")
		file.write("\t\tself.root = self.tree.getroot()\n")
		file.write("\t\tfor description in self.root.findall('./SAL" + messageType.rstrip('s') + "/item/Description'):\n")
		file.write("\t\t\tself.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')\n")
		file.write("\t\tself.file.close()\n")
		file.write("\n")

file.write("if __name__ == \"__main__\":\n")
file.write("\tunittest.main(verbosity=2)\n")
