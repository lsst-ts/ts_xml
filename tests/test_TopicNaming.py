#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
import xml.etree.ElementTree as ET
cwd = os.getcwd()
sys.path.insert(1, cwd + '/../scripts/unittests')
import xml_common

class TestTopicNaming(unittest.TestCase):

	def test_ATAOSCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATAOSEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATAOSTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATArchiverCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATArchiverEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATArchiverTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATBuildingEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATBuilding', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATBuildingTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATBuilding', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATCameraCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATCameraEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATCameraTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATDome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATDome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATDome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeTrajectoryEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATDomeTrajectory', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHeaderServiceEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATHeaderService', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHexapodCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATHexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHexapodEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATHexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHexapodTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATHexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMCSCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMCSEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMCSTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMonochromatorCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMonochromator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMonochromatorEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMonochromator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMonochromatorTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATMonochromator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPneumaticsCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPneumatics', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPneumaticsEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPneumatics', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPneumaticsTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPneumatics', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPtgCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPtgEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPtgTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATSpectrographCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATSpectrographEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATSpectrographTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATTCSCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATTCSEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATTCSTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATWhiteLightCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATWhiteLight', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATWhiteLightEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATWhiteLight', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATWhiteLightTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ATWhiteLight', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CatchupArchiverEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'CatchupArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CatchupArchiverTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'CatchupArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CBPCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'CBP', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CBPTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'CBP', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DIMMEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'DIMM', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DIMMTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'DIMM', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DomeCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Dome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DomeEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Dome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	@unittest.skip("DM-22153")
	def test_DomeTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Dome', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DSMEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'DSM', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DSMTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'DSM', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EASEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EAS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EASTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EAS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EFDEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EFD', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	@unittest.skip("DM-22154")
	def test_EFDTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EFD', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EFDTransformationServerEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EFDTransformationServer', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EFDTransformationServerTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'EFDTransformationServer', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ElectrometerCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Electrometer', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ElectrometerEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Electrometer', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EnvironmentTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Environment/Environment_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Environment', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_FiberSpectrographCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'FiberSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_FiberSpectrographEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'FiberSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_FiberSpectrographTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'FiberSpectrograph', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_GenericCameraCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'GenericCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_GenericCameraEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'GenericCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_GenericCameraTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'GenericCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_IOTAEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'IOTA', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_IOTATelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'IOTA', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HexapodCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Hexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HexapodEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Hexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	@unittest.skip("DM-20971")
	def test_HexapodTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Hexapod', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HVACCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'HVAC', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HVACEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'HVAC', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HVACTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'HVAC', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LinearStageCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'LinearStage', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LinearStageEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'LinearStage', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LinearStageTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'LinearStage', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LOVEEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'LOVE', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTAOSCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTAOSEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTAOSTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTAOS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTArchiverEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTArchiverTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTArchiver', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTCameraCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTCameraEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTCameraTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTCamera', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTDomeTrajectoryEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTDomeTrajectory', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTDomeTrajectoryTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTDomeTrajectory', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTEECCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTEEC', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTEECEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTEEC', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTGuiderEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTGuider', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTGuiderTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTGuider', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTHeaderServiceEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTHeaderService', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTLaserTrackerEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTLaserTracker', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTLaserTrackerTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTLaserTracker', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3CommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3EventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TSCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3TS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TSEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3TS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TSTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM1M3TS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM2CommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM2', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM2EventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM2', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM2TelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTM2', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTMountCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTMount', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTMountEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTMount', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	@unittest.skip("DM-17276")
	def test_MTMountTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTMount', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTPtgCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTPtgEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTPtgTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTPtg', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTTCSCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTTCSEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTTCSTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTTCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTVMSCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTVMS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTVMSEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTVMS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	@unittest.skip("DM-22155")
	def test_MTVMSTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'MTVMS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_OCSCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'OCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_OCSEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'OCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_OCSTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'OCS', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PointingComponentCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'PointingComponent', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PointingComponentEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'PointingComponent', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PointingComponentTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'PointingComponent', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PromptProcessingEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'PromptProcessing', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PromptProcessingTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'PromptProcessing', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_RotatorCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Rotator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_RotatorEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Rotator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	@unittest.skip("DM-20969")
	def test_RotatorTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Rotator', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_SchedulerEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Scheduler', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_SchedulerTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Scheduler', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Script', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Script', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptQueueCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ScriptQueue', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptQueueEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'ScriptQueue', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_SummitFacilityTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'SummitFacility', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TestCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Test', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TestEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Test', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TestTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Test', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TunableLaserCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'TunableLaser', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TunableLaserEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'TunableLaser', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TunableLaserTelemetryTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'TunableLaser', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_WatcherCommandsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Watcher', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'command', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_WatcherEventsTopicNaming(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertEqual(topic.text.split('_')[0], 'Watcher', msg='EFDB_Name ' + topic.text + ' does not properly contain the CSC name.')
			self.assertEqual(topic.text.split('_')[1], 'logevent', msg='EFDB_Name ' + topic.text + ' does not properly contain the topicType string.')
			self.assertRegex(topic.text.partition('_')[2], r'^[a-z]([a-z0-9]*)', msg='EFDB_Name Topic string ' + topic.text.partition('_')[2] + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

if __name__ == "__main__":
	unittest.main(verbosity=2)
