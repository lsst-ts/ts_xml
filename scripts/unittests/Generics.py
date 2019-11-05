#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import os.path
import glob
import xml_common

# Create/Open test suite file.
cwd = os.getcwd()
file = open(cwd + "/../../tests/test_Generics.py","w+")
sal_generics_file = "SALGenerics.xml"

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
file.write("class TestGenerics(unittest.TestCase):\n\n")

# Create the Variables table.
file.write("\t# Variables #\n")
file.write("\ttree = ET.parse(cwd + \"/../sal_interfaces/" + sal_generics_file + "\")\n")
file.write("\troot = tree.getroot()\n")
file.write("\tgeneric_commands = xml_common.generic_commands\n")
file.write("\tgeneric_events = xml_common.generic_events\n")
file.write("\tcommand_xml_path = '/SALObjects/SALCommandSet/SALCommand'\n")
file.write("\tevent_xml_path = '/SALObjects/SALEventSet/SALEvent'\n")
file.write("\tcommands = []\n")
file.write("\tevents = []\n")
file.write("\n")

# Create the Test Cases.
# Validate the sal_generics_file defines the Generic Commands.
file.write("\tdef test_" + os.path.splitext(sal_generics_file)[0] + "Commands(self):\n")
file.write("\t\tfor alias in self.root.findall('./SALCommandSet/SALCommand/Alias'):\n")
file.write("\t\t\tself.commands.append(alias.text)\n")
file.write("\t\tself.commands.sort()\n")
file.write("\t\tself.generic_commands.sort()\n")
file.write("\t\tself.assertEqual(self.commands, self.generic_commands)\n")
file.write("\n")

# Validate the sal_generics_file defines the Generic Events.
file.write("\tdef test_" + os.path.splitext(sal_generics_file)[0] + "Events(self):\n")
file.write("\t\tfor alias in self.root.findall('./SALEventSet/SALEvent/Alias'):\n")
file.write("\t\t\tself.events.append(alias.text)\n")
file.write("\t\tself.events.sort()\n")
file.write("\t\tself.generic_events.sort()\n")
file.write("\t\tself.assertEqual(self.events, self.generic_events)\n")
file.write("\n")

# Verify the CSCs DO NOT explicitly define the Generic Events.
for csc in xml_common.subsystems:
	events_file = glob.glob(cwd + "/../../sal_interfaces/" + csc + "/" + csc + "_Events.xml")
	if events_file:
		csc_tree = ET.parse(cwd + "/../../sal_interfaces/" + csc + "/" + csc + "_Events.xml")
		file.write("\tdef test_Validate" + csc + "DoesNotContainGenericEvents(self):\n")
		file.write("\t\tself.csc_events = []\n")
		file.write("\t\tself.csc_tree = ET.parse(cwd + \"/../sal_interfaces/" + csc + "/" + csc + "_Events.xml\")\n")
		file.write("\t\tfor alias in self.csc_tree.findall('./SALEvent/Alias'):\n")
		file.write("\t\t\tself.csc_events.append(alias.text)\n")
		file.write("\t\tfor event in self.csc_events:\n")
		file.write("\t\t\tself.assertTrue(event not in self.generic_events, msg=\"Generic event \" + event + \" is incorrectly defined in the " + csc + " Events XML\")\n")
		file.write("\n")

	commands_file = glob.glob(cwd + "/../../sal_interfaces/" + csc + "/" + csc + "_Commands.xml")
	if commands_file:
		csc_tree = ET.parse(cwd + "/../../sal_interfaces/" + csc + "/" + csc + "_Commands.xml")
		file.write("\tdef test_Validate" + csc + "DoesNotContainGenericCommands(self):\n")
		file.write("\t\tself.csc_commands = []\n")
		file.write("\t\tself.csc_tree = ET.parse(cwd + \"/../sal_interfaces/" + csc + "/" + csc + "_Commands.xml\")\n")
		file.write("\t\tfor alias in self.csc_tree.findall('./SALEvent/Alias'):\n")
		file.write("\t\t\tself.csc_commands.append(alias.text)\n")
		file.write("\t\tfor event in self.csc_commands:\n")
		file.write("\t\t\tself.assertTrue(event not in self.generic_commands, msg=\"Generic command \" + command + \" is incorrectly defined in the " + csc + " Commands XML\")\n")
		file.write("\n")

file.write("if __name__ == \"__main__\":\n")
file.write("\tunittest.main()\n")
