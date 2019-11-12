#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import glob
import re
import os
import os.path
import xml_common

# Create/Open test suite file.
cwd = os.getcwd()
file = open(cwd + "/../../tests/test_Count.py","w")

# Create Settings header.
file.write("#!/usr/bin/env python\n")
file.write("# -*- coding: utf-8 -*-\n")
file.write("import os\n")
file.write("import sys\n")
file.write("import unittest\n")
file.write("import xml.etree.ElementTree as ET\n")
file.write("cwd = os.getcwd()\n")
file.write("sys.path.insert(1, cwd + '/../scripts/unittests')\n")
file.write("import xml_common\n")
file.write("from Unit_Validator import Unit_Validator\n")
file.write("\n")

# Create Test Case table.
file.write("class TestCount(unittest.TestCase):\n\n")

file.write("\tuv = Unit_Validator()\n\n")

# Verify the Count field is not empty and is a valid number.
for csc in xml_common.subsystems:

	# Get the list of XMLs for each CSC, to include Telemetry, Events and Commands.
	xmls = glob.glob("../../sal_interfaces/" + csc + "/" + csc + "*")
	for xml in xmls:
		# Get the message type, i.e. Telemetry, Events, Commands.
		messageType = xml.split('/')[4].split('_')[1].split('.')[0]
		# Mark test cases with Jira tickets
		if csc == "junk":
			jira=""
		else:
			jira=""

		# Create the Test Cases.
		## Skip tests with known issues.
		if jira:
			file.write("\t@unittest.skip(\"" + jira + "\")\n")
		## Verify the Count tag is not empty.
		file.write("\tdef test_" + csc + messageType + "CountValid(self):\n")
		file.write("\t\tself.tree = ET.parse(\"" + xml[3:] + "\")\n")
		file.write("\t\tself.root = self.tree.getroot()\n")
		file.write("\t\tfor count in self.root.findall('./SAL" + messageType.rstrip('s') + "/item/Count'):\n")
		file.write("\t\t\tself.assertNotEqual(count.text, None, msg='Count cannot be blank.')\n")
		file.write("\n")

file.write("if __name__ == \"__main__\":\n")
file.write("\tunittest.main(verbosity=2)\n")
