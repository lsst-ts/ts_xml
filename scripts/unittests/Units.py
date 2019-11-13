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
file = open(cwd + "/../../tests/test_Units.py","w")

# Create Settings header.
file.write("#!/usr/bin/env python\n")
file.write("# -*- coding: utf-8 -*-\n")
file.write("import os\n")
file.write("import unittest\n")
file.write("import xml.etree.ElementTree as ET\n")
file.write("import xml_common\n")
file.write("from Unit_Validator import Unit_Validator\n")
file.write("\n")

# Create Test Case table.
file.write("class TestUnits(unittest.TestCase):\n\n")

file.write("\tuv = Unit_Validator()\n\n")

# Verify the Units conform to naming conventions.
for csc in xml_common.subsystems:

	# Get the list of XMLs for each CSC, to include Telemetry, Events and Commands.
	xmls = glob.glob("../../sal_interfaces/" + csc + "/" + csc + "*")
	for xml in xmls:
		# Get the message type, i.e. Telemetry, Events, Commands.
		messageType = xml.split('/')[4].split('_')[1].split('.')[0]
		# Mark test cases with Jira tickets
		if csc == "ATCamera":
			jira="CAP-318"
		elif csc == "ATSpectrograph" and messageType == "Commands":
			jira="DM-22158"
		elif csc == "MTCamera":
			jira="CAP-318"
		elif csc == "MTEEC" and messageType == "Commands":
			jira="DM-22159"
		elif csc == "MTM1M3":
			jira="DM-20956"
		elif csc == "OCS" and messageType == "Commands":
			jira="DM-22160"
		else:
			jira=""

		# Create the Test Cases.
		## Skip tests with known issues.
		if jira:
			file.write("\t@unittest.skip(\"" + jira + "\")\n")
		## Verify the Units tag is not empty.
		## Validate that the units conform to the astropy Units definitions.
		file.write("\tdef test_" + csc + messageType + "UnitsValid(self):\n")
		file.write("\t\tself.dir_path = os.path.dirname(os.path.realpath(__file__))\n")
		file.write("\t\tself.file = open(self.dir_path + '/" + xml[3:] + "')\n")
		file.write("\t\tself.tree = ET.parse(self.file)\n")
		file.write("\t\tself.root = self.tree.getroot()\n")
		file.write("\t\tfor unit in self.root.findall('./SAL" + messageType.rstrip('s') + "/item/Units'):\n")
		file.write("\t\t\tif not unit.text:\n")
		file.write("\t\t\t\tself.assertTrue(False, msg='Units cannot be blank.')\n")
		file.write("\t\t\telif unit.text == \"unitless\" or unit.text == \"dimensionless\":\n")
		file.write("\t\t\t\tself.assertTrue(True)\n")
		file.write("\t\t\telse:\n")
		file.write("\t\t\t\tself.assertNotIn('Error', self.uv.check_unit(unit.text))\n")
		file.write("\t\tself.file.close()\n")
		file.write("\n")

file.write("if __name__ == \"__main__\":\n")
file.write("\tunittest.main(verbosity=2)\n")
