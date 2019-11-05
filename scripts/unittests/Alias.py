#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import os.path
import glob
import xml_common

# Create/Open test suite file.
cwd = os.getcwd()
home = os.path.expanduser("~")
file = open(cwd + "/../../tests/test_Alias.py","w+")

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

# Create Variables table.
file.write("class TestAlias(unittest.TestCase):\n\n")

# Create the Test Cases.
# For each CSC, validate the Alias matches the EFDB_Topic.
for csc in xml_common.subsystems:
	# Get the list of XMLs for each CSC, to include Telemetry, Events and Commands.
	xmls = glob.glob(cwd + "/../../sal_interfaces/" + csc + "/" + csc + "*")
	for xml in xmls:
		homelength = len(home.split('/'))
		messageType = xml.split('/')[homelength + 8].split('_')[1].split('.')[0]
		# Telemetry XML definition files do not define an Alias, therefore these tests are skipped.
		if messageType == "Telemetry":
			continue
		# Create the Test Cases.
		## Verify the Alias tag conforms to the EFDB_Topic tag.
		file.write("\tdef test_" + csc + messageType + "Aliases(self):\n")
		file.write("\t\tself.csc_aliases = []\n")
		file.write("\t\tself.csc_topics = []\n")
		file.write("\t\tself.tree = ET.parse(\"" + xml + "\")\n")
		file.write("\t\tself.root = self.tree.getroot()\n")
		file.write("\t\tfor alias in self.root.findall('./SAL" + messageType.rstrip('s') + "/Alias'):\n")
		file.write("\t\t\tself.csc_aliases.append(alias.text)\n")
		file.write("\t\tfor topic in self.root.findall('./SAL" + messageType.rstrip('s') + "/EFDB_Topic'):\n")
		file.write("\t\t\tself.csc_topics.append(topic.text.split('_',2)[2])\n")
		file.write("\t\tself.csc_aliases.sort()\n")
		file.write("\t\tself.csc_topics.sort()\n")
		file.write("\t\tself.assertEqual(self.csc_aliases, self.csc_topics)\n")
		file.write("\n")

file.write("if __name__ == \"__main__\":\n")
file.write("\tunittest.main()\n")
