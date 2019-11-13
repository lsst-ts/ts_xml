#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import xml.etree.ElementTree as ET
import xml_common

class TestNoSpaces(unittest.TestCase):

	def test_ATAOSCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATAOSCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATAOSCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATAOSCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATAOSEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATAOSEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATAOSEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATAOSEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATAOSTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATAOSTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATAOSTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATArchiverCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATArchiverCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATArchiverCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATArchiverCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATArchiverEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATArchiverEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATArchiverEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATArchiverEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATArchiverTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATArchiverTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATArchiverTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATBuildingEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATBuildingEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATBuildingEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATBuildingEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATBuildingTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATBuildingTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATBuildingTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATCameraCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATCameraCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATCameraCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATCameraCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATCameraEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATCameraEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATCameraEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATCameraEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATCameraTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATCameraTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATCameraTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATDomeCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATDomeCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATDomeCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATDomeCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATDomeEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATDomeEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATDomeEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATDomeEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATDomeTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATDomeTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATDomeTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATDomeTrajectoryEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATDomeTrajectoryEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATDomeTrajectoryEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATDomeTrajectoryEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATHeaderServiceEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATHeaderServiceEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATHeaderServiceEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATHeaderServiceEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATHexapodCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATHexapodCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATHexapodCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATHexapodCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATHexapodEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATHexapodEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATHexapodEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATHexapodEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATHexapodTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATHexapodTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATHexapodTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATMCSCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATMCSCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATMCSCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATMCSCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATMCSEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATMCSEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATMCSEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATMCSEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATMCSTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATMCSTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATMCSTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATMonochromatorCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATMonochromatorCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATMonochromatorCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATMonochromatorCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATMonochromatorEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATMonochromatorEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATMonochromatorEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATMonochromatorEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATMonochromatorTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATMonochromatorTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATMonochromatorTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATPneumaticsCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATPneumaticsCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATPneumaticsCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATPneumaticsCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATPneumaticsEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATPneumaticsEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATPneumaticsEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATPneumaticsEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATPneumaticsTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATPneumaticsTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATPneumaticsTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATPtgCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATPtgCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATPtgCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATPtgCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATPtgEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATPtgEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATPtgEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATPtgEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATPtgTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATPtgTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATPtgTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATSpectrographCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATSpectrographCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATSpectrographCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATSpectrographCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATSpectrographEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATSpectrographEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATSpectrographEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATSpectrographEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATSpectrographTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATSpectrographTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATSpectrographTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATTCSCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATTCSCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATTCSCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATTCSCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATTCSEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATTCSEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATTCSEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATTCSEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATTCSTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATTCSTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATTCSTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATWhiteLightCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATWhiteLightCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATWhiteLightCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATWhiteLightCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATWhiteLightEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATWhiteLightEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATWhiteLightEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ATWhiteLightEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ATWhiteLightTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ATWhiteLightTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ATWhiteLightTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_CatchupArchiverEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_CatchupArchiverEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_CatchupArchiverEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_CatchupArchiverEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_CatchupArchiverTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_CatchupArchiverTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_CatchupArchiverTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_CBPCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_CBPCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_CBPCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_CBPCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_CBPTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_CBPTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_CBPTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_DIMMEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_DIMMEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_DIMMEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_DIMMEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_DIMMTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_DIMMTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_DIMMTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_DomeCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_DomeCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_DomeCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_DomeCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_DomeEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_DomeEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_DomeEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_DomeEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_DomeTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_DomeTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_DomeTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_DSMEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_DSMEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_DSMEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_DSMEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_DSMTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_DSMTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_DSMTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_EASEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_EASEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_EASEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_EASEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_EASTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_EASTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_EASTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_EFDEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_EFDEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_EFDEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_EFDEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_EFDTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_EFDTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_EFDTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_EFDTransformationServerEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_EFDTransformationServerEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_EFDTransformationServerEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_EFDTransformationServerEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_EFDTransformationServerTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_EFDTransformationServerTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_EFDTransformationServerTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ElectrometerCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ElectrometerCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ElectrometerCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ElectrometerCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ElectrometerEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ElectrometerEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ElectrometerEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ElectrometerEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_EnvironmentTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Environment/Environment_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_EnvironmentTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Environment/Environment_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_EnvironmentTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Environment/Environment_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_FiberSpectrographCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_FiberSpectrographCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_FiberSpectrographCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_FiberSpectrographCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_FiberSpectrographEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_FiberSpectrographEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_FiberSpectrographEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_FiberSpectrographEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_FiberSpectrographTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_FiberSpectrographTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_FiberSpectrographTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_GenericCameraCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_GenericCameraCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_GenericCameraCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_GenericCameraCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_GenericCameraEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_GenericCameraEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_GenericCameraEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_GenericCameraEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_GenericCameraTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_GenericCameraTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_GenericCameraTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_IOTAEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_IOTAEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_IOTAEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_IOTAEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_IOTATelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_IOTATelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_IOTATelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_HexapodCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_HexapodCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_HexapodCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_HexapodCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_HexapodEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_HexapodEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_HexapodEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_HexapodEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_HexapodTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_HexapodTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_HexapodTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_HVACCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_HVACCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_HVACCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_HVACCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_HVACEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_HVACEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_HVACEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_HVACEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_HVACTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_HVACTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_HVACTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_LinearStageCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_LinearStageCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_LinearStageCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_LinearStageCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_LinearStageEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_LinearStageEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_LinearStageEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_LinearStageEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_LinearStageTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_LinearStageTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_LinearStageTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_LOVEEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_LOVEEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_LOVEEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_LOVEEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTAOSCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTAOSCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTAOSCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTAOSCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTAOSEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTAOSEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTAOSEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTAOSEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTAOSTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTAOSTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTAOSTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTArchiverEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTArchiverEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTArchiverEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTArchiverEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTArchiverTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTArchiverTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTArchiverTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTCameraCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTCameraCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTCameraCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTCameraCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTCameraEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTCameraEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTCameraEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTCameraEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTCameraTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTCameraTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTCameraTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTDomeTrajectoryEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTDomeTrajectoryEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTDomeTrajectoryEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTDomeTrajectoryEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTDomeTrajectoryTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTDomeTrajectoryTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTDomeTrajectoryTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTEECCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTEECCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTEECCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTEECCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTEECEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTEECEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTEECEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTEECEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTGuiderEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTGuiderEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTGuiderEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTGuiderEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTGuiderTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTGuiderTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTGuiderTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTHeaderServiceEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTHeaderServiceEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTHeaderServiceEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTHeaderServiceEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTLaserTrackerEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTLaserTrackerEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTLaserTrackerEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTLaserTrackerEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTLaserTrackerTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTLaserTrackerTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTLaserTrackerTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTM1M3CommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTM1M3CommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTM1M3CommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTM1M3CommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTM1M3EventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTM1M3EventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTM1M3EventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTM1M3EventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTM1M3TelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTM1M3TelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTM1M3TelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTM1M3TSCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTM1M3TSCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTM1M3TSCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTM1M3TSCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTM1M3TSEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTM1M3TSEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTM1M3TSEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTM1M3TSEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTM1M3TSTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTM1M3TSTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTM1M3TSTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTM2CommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTM2CommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTM2CommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTM2CommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTM2EventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTM2EventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTM2EventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTM2EventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTM2TelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTM2TelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTM2TelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTMountCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTMountCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTMountCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTMountCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTMountEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTMountEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTMountEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTMountEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTMountTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTMountTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTMountTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTPtgCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTPtgCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTPtgCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTPtgCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTPtgEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTPtgEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTPtgEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTPtgEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTPtgTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTPtgTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTPtgTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTTCSCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTTCSCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTTCSCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTTCSCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTTCSEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTTCSEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTTCSEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTTCSEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTTCSTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTTCSTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTTCSTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTVMSCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTVMSCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTVMSCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTVMSCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTVMSEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTVMSEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTVMSEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_MTVMSEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_MTVMSTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_MTVMSTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_MTVMSTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_OCSCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_OCSCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_OCSCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_OCSCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_OCSEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_OCSEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_OCSEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_OCSEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_OCSTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_OCSTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_OCSTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_PointingComponentCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_PointingComponentCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_PointingComponentCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_PointingComponentCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_PointingComponentEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_PointingComponentEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_PointingComponentEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_PointingComponentEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_PointingComponentTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_PointingComponentTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_PointingComponentTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_PromptProcessingEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_PromptProcessingEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_PromptProcessingEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_PromptProcessingEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_PromptProcessingTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_PromptProcessingTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_PromptProcessingTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_RotatorCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_RotatorCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_RotatorCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_RotatorCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_RotatorEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_RotatorEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_RotatorEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_RotatorEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_RotatorTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_RotatorTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_RotatorTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_SchedulerEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_SchedulerEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_SchedulerEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_SchedulerEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_SchedulerTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_SchedulerTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_SchedulerTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ScriptCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ScriptCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ScriptCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ScriptCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ScriptEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ScriptEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ScriptEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ScriptEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ScriptQueueCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ScriptQueueCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ScriptQueueCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ScriptQueueCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_ScriptQueueEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_ScriptQueueEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_ScriptQueueEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_ScriptQueueEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_SummitFacilityTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_SummitFacilityTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_SummitFacilityTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_TestCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_TestCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_TestCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_TestCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_TestEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_TestEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_TestEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_TestEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_TestTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_TestTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_TestTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_TunableLaserCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_TunableLaserCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_TunableLaserCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_TunableLaserCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_TunableLaserEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_TunableLaserEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_TunableLaserEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_TunableLaserEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_TunableLaserTelemetrySubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALTelemetry/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_TunableLaserTelemetryEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALTelemetry/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_TunableLaserTelemetryEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_WatcherCommandsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALCommand/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_WatcherCommandsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_WatcherCommandsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_WatcherCommandsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

	def test_WatcherEventsSubsystemNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for subsystem in self.root.findall('./SALEvent/Subsystem'):
			self.assertNotIn(' ', subsystem.text, msg='<Subsystem> tag cannot contain spaces.')

	def test_WatcherEventsEFDB_TopicNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.assertNotIn(' ', topic.text, msg='<EFDB_Topic> tag cannot contain spaces.')

	def test_WatcherEventsAliasNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.assertNotIn(' ', alias.text, msg='<Alias> tag cannot contain spaces.')

	def test_WatcherEventsEFDB_NameNoSpace(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(' ', name.text, msg='<EFDB_Name> tag cannot contain spaces.')

if __name__ == "__main__":
	unittest.main(verbosity=2)
