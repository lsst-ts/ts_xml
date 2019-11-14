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
file = open(cwd + "/../../tests/test_TopicNaming.py","w")

# Create Settings header.
file.write("#!/usr/bin/env python\n")
file.write("# -*- coding: utf-8 -*-\n")
file.write("import os\n")
file.write("import unittest\n")
file.write("import xml.etree.ElementTree as ET\n")
file.write("import xml_common\n")
file.write("\n")

# Create Test Case table.
file.write("class TestTopicNaming(unittest.TestCase):\n\n")

# Verify the TopicNames conform to naming conventions.
for csc in xml_common.subsystems:

	# Get the list of XMLs for each CSC, to include Telemetry, Events and Commands.
	xmls = glob.glob("../../sal_interfaces/" + csc + "/" + csc + "*")
	for xml in xmls:
		# Get the message type, i.e. Telemetry, Events, Commands.
		messageType = xml.split('/')[4].split('_')[1].split('.')[0]
		# The full TopicName is made of three part, <CSC_Name>_<topicType>_<Alias>.
		# The topicType depends on the messageType, as defined below.
		# NOTE: Telemetry topics do not have the <topicType> string.
		if messageType == "Commands":
			topicType = "command_"
			index="2"
		elif messageType == "Events":
			topicType = "logevent_"
			index="2"
		else:
			topicType = ""
			index="1"
		# Mark test cases with Jira tickets
		if csc == "MTMount" and (messageType == "Telemetry"):
			jira="DM-17276"
		elif csc == "Dome" and (messageType == "Telemetry"):
			jira="DM-22153"
		elif csc == "EFD" and (messageType == "Telemetry"):
			jira="DM-22154"
		elif csc == "Hexapod" and (messageType == "Telemetry"):
			jira="DM-20971"
		elif csc == "MTVMS" and (messageType == "Telemetry"):
			jira="DM-22155"
		elif csc == "Rotator" and (messageType == "Telemetry"):
			jira="DM-20969"
		else:
			jira=""
		# Create the Test Cases.
		if jira:
			file.write("\t@unittest.skip(\"" + jira + "\")\n")
		file.write("\tdef test_" + csc + messageType + "TopicNaming(self):\n")
		file.write("\t\tself.dir_path = os.path.dirname(os.path.realpath(__file__))\n")
		file.write("\t\tself.file = open(self.dir_path + '/" + xml[3:] + "', 'r', encoding='utf-8')\n")
		file.write("\t\tself.tree = ET.parse(self.file)\n")
		file.write("\t\tself.root = self.tree.getroot()\n")
		file.write("\t\tfor topic in self.root.findall('./SAL" + messageType.rstrip('s') + "/EFDB_Topic'):\n")
		file.write("\t\t\tself.assertEqual(topic.text.split('_')[0], '" + csc + "', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')\n")
		# Skip the next unit test for Telemetry topic names, since they do not contain the topicType string.
		if topicType:
			file.write("\t\t\tself.assertEqual(topic.text.split('_')[1], '" + topicType.strip('_') + "', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')\n")
		file.write("\t\t\tself.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')\n")
		file.write("\t\tself.file.close()\n")
		file.write("\n")

file.write("if __name__ == \"__main__\":\n")
file.write("\tunittest.main(verbosity=2)\n")
