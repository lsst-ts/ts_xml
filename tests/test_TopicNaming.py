#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import xml.etree.ElementTree as ET
import xml_common

class TestTopicNaming(unittest.TestCase):

	def test_ATAOSCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATAOSEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATAOSTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATArchiverCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATArchiverEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATArchiverTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATBuildingEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATBuilding', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATBuildingTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATBuilding', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATCameraCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATCameraEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATCameraTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATDomeCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATDome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATDomeEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATDome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATDomeTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATDome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATDomeTrajectoryEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATDomeTrajectory', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATHeaderServiceEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATHeaderService', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATHexapodCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATHexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATHexapodEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATHexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATHexapodTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATHexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMCSCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMCSEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMCSTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMonochromatorCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMonochromator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMonochromatorEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMonochromator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMonochromatorTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMonochromator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPneumaticsCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPneumatics', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPneumaticsEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPneumatics', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPneumaticsTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPneumatics', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPtgCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPtgEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPtgTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATSpectrographCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATSpectrographEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATSpectrographTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATTCSCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATTCSEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATTCSTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATWhiteLightCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATWhiteLight', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATWhiteLightEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATWhiteLight', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATWhiteLightTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATWhiteLight', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_CBPCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'CBP', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_CBPTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'CBP', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_CatchupArchiverEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'CatchupArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_CatchupArchiverTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'CatchupArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DIMMEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'DIMM', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DIMMTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'DIMM', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DSMEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'DSM', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DSMTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'DSM', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DomeCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Dome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DomeEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Dome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	@unittest.skip("DM-22153")
	def test_DomeTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Dome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EASEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EAS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EASTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EAS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EFDEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EFD', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	@unittest.skip("DM-22154")
	def test_EFDTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EFD', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EFDTransformationServerEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EFDTransformationServer', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EFDTransformationServerTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EFDTransformationServer', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ElectrometerCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Electrometer', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ElectrometerEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Electrometer', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EnvironmentTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Environment/Environment_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Environment', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_FiberSpectrographCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'FiberSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_FiberSpectrographEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'FiberSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_FiberSpectrographTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'FiberSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_GenericCameraCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'GenericCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_GenericCameraEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'GenericCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_GenericCameraTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'GenericCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_HVACCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'HVAC', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_HVACEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'HVAC', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_HVACTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'HVAC', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_HexapodCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Hexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_HexapodEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Hexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	@unittest.skip("DM-20971")
	def test_HexapodTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Hexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_IOTAEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'IOTA', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_IOTATelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'IOTA', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_LOVEEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'LOVE', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_LinearStageCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'LinearStage', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_LinearStageEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'LinearStage', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_LinearStageTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'LinearStage', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTAOSCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTAOSEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTAOSTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTArchiverEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTArchiverTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTCameraCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTCameraEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTCameraTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTDomeTrajectoryEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTDomeTrajectory', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTDomeTrajectoryTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTDomeTrajectory', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTEECCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTEEC', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTEECEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTEEC', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTGuiderEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTGuider', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTGuiderTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTGuider', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTHeaderServiceEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTHeaderService', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTLaserTrackerEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTLaserTracker', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTLaserTrackerTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTLaserTracker', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3CommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3EventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3TelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3TSCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3TS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3TSEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3TS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3TSTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3TS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM2CommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM2', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM2EventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM2', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM2TelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM2', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTMountCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTMount', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTMountEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTMount', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	@unittest.skip("DM-17276")
	def test_MTMountTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTMount', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTPtgCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTPtgEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTPtgTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTTCSCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTTCSEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTTCSTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTVMSCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTVMS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTVMSEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTVMS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	@unittest.skip("DM-22155")
	def test_MTVMSTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTVMS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_OCSCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'OCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_OCSEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'OCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_OCSTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'OCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_PointingComponentCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'PointingComponent', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_PointingComponentEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'PointingComponent', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_PointingComponentTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'PointingComponent', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_PromptProcessingEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'PromptProcessing', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_PromptProcessingTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'PromptProcessing', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_RotatorCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Rotator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_RotatorEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Rotator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	@unittest.skip("DM-20969")
	def test_RotatorTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Rotator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_SchedulerEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Scheduler', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_SchedulerTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Scheduler', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ScriptCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Script', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ScriptEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Script', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ScriptQueueCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ScriptQueue', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ScriptQueueEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ScriptQueue', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_SummitFacilityTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'SummitFacility', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TestCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Test', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TestEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Test', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TestTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Test', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TunableLaserCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'TunableLaser', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TunableLaserEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'TunableLaser', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TunableLaserTelemetryTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'TunableLaser', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_WatcherCommandsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Watcher', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_WatcherEventsTopicNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Watcher', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)
