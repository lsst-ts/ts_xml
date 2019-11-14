#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import xml.etree.ElementTree as ET
import xml_common

class TestNoSpaces(unittest.TestCase):

	def test_ATAOSCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATAOSCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATAOSCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATAOSCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATAOSEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATAOSEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATAOSEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATAOSEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATAOSTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATAOSTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATAOSTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATArchiverCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATArchiverCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATArchiverCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATArchiverCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATArchiverEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATArchiverEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATArchiverEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATArchiverEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATArchiverTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATArchiverTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATArchiverTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATBuildingEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATBuildingEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATBuildingEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATBuildingEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATBuildingTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATBuildingTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATBuildingTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATCameraCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATCameraCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATCameraCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATCameraCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATCameraEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATCameraEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATCameraEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATCameraEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATCameraTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATCameraTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATCameraTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeTrajectoryEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeTrajectoryEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeTrajectoryEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATDomeTrajectoryEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATHeaderServiceEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATHeaderServiceEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATHeaderServiceEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATHeaderServiceEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATHexapodCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATHexapodCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATHexapodCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATHexapodCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATHexapodEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATHexapodEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATHexapodEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATHexapodEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATHexapodTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATHexapodTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATHexapodTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATMCSCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATMCSCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATMCSCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATMCSCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATMCSEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATMCSEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATMCSEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATMCSEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATMCSTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATMCSTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATMCSTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATMonochromatorCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATMonochromatorCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATMonochromatorCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATMonochromatorCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATMonochromatorEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATMonochromatorEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATMonochromatorEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATMonochromatorEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATMonochromatorTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATMonochromatorTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATMonochromatorTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATPneumaticsCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATPneumaticsCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATPneumaticsCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATPneumaticsCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATPneumaticsEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATPneumaticsEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATPneumaticsEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATPneumaticsEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATPneumaticsTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATPneumaticsTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATPneumaticsTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATPtgCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATPtgCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATPtgCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATPtgCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATPtgEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATPtgEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATPtgEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATPtgEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATPtgTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATPtgTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATPtgTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATSpectrographCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATSpectrographCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATSpectrographCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATSpectrographCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATSpectrographEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATSpectrographEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATSpectrographEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATSpectrographEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATSpectrographTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATSpectrographTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATSpectrographTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATTCSCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATTCSCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATTCSCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATTCSCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATTCSEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATTCSEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATTCSEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATTCSEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATTCSTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATTCSTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATTCSTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATWhiteLightCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATWhiteLightCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATWhiteLightCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATWhiteLightCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATWhiteLightEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATWhiteLightEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATWhiteLightEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ATWhiteLightEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ATWhiteLightTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ATWhiteLightTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ATWhiteLightTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_CatchupArchiverEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_CatchupArchiverEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_CatchupArchiverEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_CatchupArchiverEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_CatchupArchiverTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_CatchupArchiverTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_CatchupArchiverTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_CBPCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_CBPCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_CBPCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_CBPCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_CBPTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_CBPTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_CBPTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_DIMMEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_DIMMEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_DIMMEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_DIMMEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_DIMMTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_DIMMTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_DIMMTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_DomeCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_DomeCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_DomeCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_DomeCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_DomeEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_DomeEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_DomeEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_DomeEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_DomeTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_DomeTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_DomeTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_DSMEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_DSMEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_DSMEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_DSMEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_DSMTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_DSMTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_DSMTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_EASEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_EASEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_EASEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_EASEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_EASTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_EASTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_EASTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_EFDEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_EFDEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_EFDEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_EFDEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_EFDTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_EFDTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_EFDTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_EFDTransformationServerEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_EFDTransformationServerEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_EFDTransformationServerEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_EFDTransformationServerEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_EFDTransformationServerTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_EFDTransformationServerTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_EFDTransformationServerTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ElectrometerCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ElectrometerCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ElectrometerCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ElectrometerCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ElectrometerEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ElectrometerEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ElectrometerEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ElectrometerEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_EnvironmentTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Environment/Environment_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_EnvironmentTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Environment/Environment_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_EnvironmentTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Environment/Environment_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_FiberSpectrographCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_FiberSpectrographCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_FiberSpectrographCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_FiberSpectrographCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_FiberSpectrographEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_FiberSpectrographEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_FiberSpectrographEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_FiberSpectrographEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_FiberSpectrographTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_FiberSpectrographTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_FiberSpectrographTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_GenericCameraCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_GenericCameraCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_GenericCameraCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_GenericCameraCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_GenericCameraEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_GenericCameraEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_GenericCameraEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_GenericCameraEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_GenericCameraTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_GenericCameraTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_GenericCameraTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_IOTAEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_IOTAEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_IOTAEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_IOTAEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_IOTATelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_IOTATelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_IOTATelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_HexapodCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_HexapodCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_HexapodCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_HexapodCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_HexapodEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_HexapodEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_HexapodEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_HexapodEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_HexapodTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_HexapodTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_HexapodTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_HVACCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_HVACCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_HVACCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_HVACCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_HVACEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_HVACEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_HVACEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_HVACEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_HVACTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_HVACTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_HVACTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_LinearStageCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_LinearStageCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_LinearStageCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_LinearStageCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_LinearStageEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_LinearStageEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_LinearStageEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_LinearStageEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_LinearStageTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_LinearStageTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_LinearStageTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_LOVEEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_LOVEEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_LOVEEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_LOVEEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTAOSCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTAOSCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTAOSCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTAOSCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTAOSEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTAOSEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTAOSEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTAOSEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTAOSTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTAOSTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTAOSTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTArchiverEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTArchiverEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTArchiverEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTArchiverEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTArchiverTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTArchiverTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTArchiverTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTCameraCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTCameraCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTCameraCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTCameraCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTCameraEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTCameraEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTCameraEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTCameraEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTCameraTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTCameraTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTCameraTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTDomeTrajectoryEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTDomeTrajectoryEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTDomeTrajectoryEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTDomeTrajectoryEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTDomeTrajectoryTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTDomeTrajectoryTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTDomeTrajectoryTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTEECCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTEECCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTEECCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTEECCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTEECEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTEECEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTEECEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTEECEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTGuiderEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTGuiderEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTGuiderEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTGuiderEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTGuiderTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTGuiderTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTGuiderTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTHeaderServiceEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTHeaderServiceEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTHeaderServiceEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTHeaderServiceEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTLaserTrackerEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTLaserTrackerEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTLaserTrackerEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTLaserTrackerEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTLaserTrackerTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTLaserTrackerTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTLaserTrackerTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3CommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3CommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3CommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3CommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3EventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3EventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3EventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3EventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TSCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TSCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TSCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TSCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TSEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TSEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TSEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TSEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TSTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TSTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTM1M3TSTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTM2CommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTM2CommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTM2CommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTM2CommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTM2EventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTM2EventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTM2EventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTM2EventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTM2TelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTM2TelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTM2TelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTMountCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTMountCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTMountCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTMountCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTMountEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTMountEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTMountEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTMountEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTMountTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTMountTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTMountTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTPtgCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTPtgCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTPtgCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTPtgCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTPtgEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTPtgEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTPtgEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTPtgEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTPtgTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTPtgTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTPtgTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTTCSCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTTCSCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTTCSCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTTCSCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTTCSEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTTCSEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTTCSEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTTCSEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTTCSTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTTCSTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTTCSTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTVMSCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTVMSCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTVMSCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTVMSCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTVMSEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTVMSEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTVMSEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_MTVMSEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_MTVMSTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_MTVMSTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_MTVMSTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_OCSCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_OCSCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_OCSCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_OCSCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_OCSEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_OCSEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_OCSEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_OCSEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_OCSTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_OCSTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_OCSTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_PointingComponentCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_PointingComponentCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_PointingComponentCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_PointingComponentCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_PointingComponentEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_PointingComponentEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_PointingComponentEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_PointingComponentEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_PointingComponentTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_PointingComponentTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_PointingComponentTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_PromptProcessingEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_PromptProcessingEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_PromptProcessingEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_PromptProcessingEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_PromptProcessingTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_PromptProcessingTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_PromptProcessingTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_RotatorCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_RotatorCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_RotatorCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_RotatorCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_RotatorEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_RotatorEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_RotatorEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_RotatorEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_RotatorTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_RotatorTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_RotatorTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_SchedulerEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_SchedulerEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_SchedulerEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_SchedulerEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_SchedulerTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_SchedulerTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_SchedulerTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptQueueCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptQueueCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptQueueCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptQueueCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptQueueEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptQueueEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptQueueEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_ScriptQueueEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_SummitFacilityTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_SummitFacilityTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_SummitFacilityTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_TestCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_TestCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_TestCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_TestCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_TestEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_TestEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_TestEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_TestEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_TestTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_TestTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_TestTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_TunableLaserCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_TunableLaserCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_TunableLaserCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_TunableLaserCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_TunableLaserEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_TunableLaserEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_TunableLaserEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_TunableLaserEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_TunableLaserTelemetrySubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_TunableLaserTelemetryEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_TunableLaserTelemetryEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_WatcherCommandsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_WatcherCommandsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_WatcherCommandsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_WatcherCommandsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

	def test_WatcherEventsSubsystemNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')
		self.file.close()

	def test_WatcherEventsEFDB_TopicNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')
		self.file.close()

	def test_WatcherEventsAliasNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')
		self.file.close()

	def test_WatcherEventsEFDB_NameNoSpace(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')
		self.file.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)
