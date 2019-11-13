#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import sys
import os
import os.path
cwd = os.getcwd()
sys.path.insert(1, cwd + '/../../tests')
import xml_common

# Create/Open test suite file.
file = open("../../tests/test_SALSubsystems.py","w+")

# Create Settings header.
file.write("#!/usr/bin/env python\n")
file.write("# -*- coding: utf-8 -*-\n")
file.write("import os\n")
file.write("import unittest\n")
file.write("import xml.etree.ElementTree as ET\n")
file.write("import xml_common\n")
file.write("\n")

# Create the TestSALSubsystem Class and TestCases
file.write("class TestSALSubsystem(unittest.TestCase):\n")
file.write("\n")

# Get the list of CSCs from the SAL Dictionary, SALSubsystems.xml.
cscs = xml_common.subsystems
cscs.sort()

# Create the Variables table.
file.write("\t# Variables #\n")
file.write("\tdir_path = os.path.dirname(os.path.realpath(__file__))\n")
file.write("\tfile = open(dir_path + '/../sal_interfaces/SALSubsystems.xml')\n")
file.write("\ttree = ET.parse(file)\n")
file.write("\troot = tree.getroot()\n")
file.write("\tcscs = xml_common.subsystems\n")
file.write("\n")

# Create Test Case table.
file.write("\t# Test Cases #\n")

# Validate the sal_dict_file.
### TBD ###

# Ensure expected number of CSCs. This will catch when CSCs are added or removed.
file.write("\tdef test_cscCount(self):\n")
file.write("\t\tself.assertEqual(len(self.cscs), 58, msg=\"Subsystem list has an added or removed entry\")\n")
file.write("\n")

# Ensure the SAL Dictionary does not contain duplicate entries.
file.write("\tdef test_uniqCSC(self):\n")
file.write("\t\tself.assertTrue(len(self.cscs) == len(set(self.cscs)), msg=\"Subsystem list contains a duplicate entry\")\n")
file.write("\n")

# Begin testing each CSC.
for csc in cscs:

	# Verify each CSC is defined in the SAL Dictionary.
	file.write("\tdef test_" + csc.lower() + "Exists(self):\n")
	file.write("\t\tself.assertIn(\"" + csc + "\", self.cscs)\n")
	file.write("\n")

	# Set the condition to no for the CSCs that do not utilize the Generic topics.
	if csc == "Script":
		value="no"
	elif csc == "LOVE":
		value="no"
	else:
		value="yes"

	# Verify the Generics tag is properly defined for each CSC in the SAL Dictionary.
	file.write("\tdef test_" + csc.lower() + "Generics(self):\n")
	file.write("\t\tself.assertEqual(self.root.find(\"./Subsystem/[Name='" + csc + "']/Generics\").text, \"" + value +"\")\n")
	file.write("\n")

	# Verify the Simulator tag is properly defined for each CSC in the SAL Dictionary.
	file.write("\tdef test_" + csc.lower() + "Simulator(self):\n")
	file.write("\t\tself.assertIsInstance(self.root.find(\"./Subsystem/[Name='" + csc + "']/Simulator\"), ET.Element, msg=\"" + csc + "Simulator tag is NOT present\")\n")
	file.write("\n")


file.write("if __name__ == \"__main__\":\n")
file.write("\tunittest.main(verbosity=2)\n")