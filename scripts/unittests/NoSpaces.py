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
file = open(cwd + "/../../tests/test_NoSpaces.py","w")

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
file.write("\n")

# Create Test Case table.
file.write("class TestNoSpaces(unittest.TestCase):\n\n")

# Verify the <Subsystem>, <EFDB_Topics>, <Alias> and <EFDB_Name> tags do NOT contain spaces.
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
		## Verify the <Subsystem> tag is not empty.
		file.write("\tdef test_" + csc + messageType + "SubsystemNoSpace(self):\n")
		file.write("\t\tself.tree = ET.parse(\"" + xml[3:] + "\")\n")
		file.write("\t\tself.root = self.tree.getroot()\n")
		file.write("\t\tfor subsystem in self.root.findall('./SAL" + messageType.rstrip('s') + "/Subsystem'):\n")
		file.write("\t\t\tself.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')\n\n")

		## Verify the <EFDB_Topic> tag is not empty.
		file.write("\tdef test_" + csc + messageType + "EFDB_TopicNoSpace(self):\n")
		file.write("\t\tself.tree = ET.parse(\"" + xml[3:] + "\")\n")
		file.write("\t\tself.root = self.tree.getroot()\n")
		file.write("\t\tfor topic in self.root.findall('./SAL" + messageType.rstrip('s') + "/EFDB_Topic'):\n")
		file.write("\t\t\tself.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')\n\n")

		## Verify the <Alias> tag is not empty.
		## NOTE: Telemetry XMLs do not include the <Alias> tag, so skip them.
		if (messageType != "Telemetry"):
			file.write("\tdef test_" + csc + messageType + "AliasNoSpace(self):\n")
			file.write("\t\tself.tree = ET.parse(\"" + xml[3:] + "\")\n")
			file.write("\t\tself.root = self.tree.getroot()\n")
			file.write("\t\tfor alias in self.root.findall('./SAL" + messageType.rstrip('s') + "/Alias'):\n")
			file.write("\t\t\tself.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')\n\n")

		## Verify the <EFDB_Name> tag is not empty.
		file.write("\tdef test_" + csc + messageType + "EFDB_NameNoSpace(self):\n")
		file.write("\t\tself.tree = ET.parse(\"" + xml[3:] + "\")\n")
		file.write("\t\tself.root = self.tree.getroot()\n")
		file.write("\t\tfor name in self.root.findall('./SAL" + messageType.rstrip('s') + "/item/EFDB_Name'):\n")
		file.write("\t\t\tself.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')\n\n")

file.write("if __name__ == \"__main__\":\n")
file.write("\tunittest.main(verbosity=2)\n")
