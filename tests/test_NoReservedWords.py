#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import xml.etree.ElementTree as ET
import xml_common

class TestNoReservedWords(unittest.TestCase):

	def test_ATAOSCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATAOSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATAOSEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATAOSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATAOSTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATAOSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATArchiverCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATArchiverCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATArchiverEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATArchiverEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATArchiverTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATArchiverTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATBuildingEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATBuildingEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATBuildingTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATBuildingTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATCameraCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATCameraCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATCameraEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATCameraEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATCameraTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATCameraTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATDomeCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATDomeCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATDomeEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATDomeEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATDomeTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATDomeTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATDomeTrajectoryEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATDomeTrajectoryEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATHeaderServiceEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATHeaderServiceEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATHexapodCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATHexapodCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATHexapodEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATHexapodEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATHexapodTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATHexapodTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMCSCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMCSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMCSEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMCSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMCSTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMCSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMonochromatorCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMonochromatorCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMonochromatorEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMonochromatorEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMonochromatorTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATMonochromatorTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPneumaticsCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPneumaticsCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPneumaticsEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPneumaticsEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPneumaticsTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPneumaticsTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPtgCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPtgCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPtgEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPtgEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPtgTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATPtgTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATSpectrographCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATSpectrographCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATSpectrographEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATSpectrographEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATSpectrographTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATSpectrographTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATTCSCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATTCSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATTCSEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATTCSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATTCSTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATTCSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATWhiteLightCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATWhiteLightCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATWhiteLightEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATWhiteLightEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATWhiteLightTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ATWhiteLightTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_CatchupArchiverEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_CatchupArchiverEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_CatchupArchiverTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_CatchupArchiverTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_CBPCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_CBPCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_CBPTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_CBPTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_DIMMEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_DIMMEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_DIMMTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_DIMMTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_DomeCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_DomeCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_DomeEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_DomeEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_DomeTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_DomeTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_DSMEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_DSMEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_DSMTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_DSMTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_EASEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_EASEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_EASTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_EASTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_EFDEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_EFDEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_EFDTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_EFDTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_EFDTransformationServerEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_EFDTransformationServerEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_EFDTransformationServerTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_EFDTransformationServerTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ElectrometerCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ElectrometerCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ElectrometerEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ElectrometerEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_EnvironmentTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Environment/Environment_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_EnvironmentTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Environment/Environment_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_FiberSpectrographCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_FiberSpectrographCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_FiberSpectrographEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_FiberSpectrographEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_FiberSpectrographTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_FiberSpectrographTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_GenericCameraCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_GenericCameraCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_GenericCameraEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_GenericCameraEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_GenericCameraTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_GenericCameraTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_IOTAEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_IOTAEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_IOTATelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_IOTATelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_HexapodCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_HexapodCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_HexapodEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_HexapodEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_HexapodTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_HexapodTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_HVACCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_HVACCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_HVACEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_HVACEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_HVACTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_HVACTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_LinearStageCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_LinearStageCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_LinearStageEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_LinearStageEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_LinearStageTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_LinearStageTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_LOVEEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_LOVEEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTAOSCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTAOSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTAOSEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTAOSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTAOSTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTAOSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTArchiverEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTArchiverEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTArchiverTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTArchiverTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTCameraCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTCameraCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTCameraEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTCameraEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTCameraTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTCameraTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTDomeTrajectoryEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTDomeTrajectoryEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTDomeTrajectoryTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTDomeTrajectoryTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTEECCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTEECCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTEECEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTEECEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTGuiderEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTGuiderEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTGuiderTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTGuiderTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTHeaderServiceEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTHeaderServiceEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTLaserTrackerEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTLaserTrackerEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTLaserTrackerTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTLaserTrackerTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3CommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3CommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3EventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3EventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3TelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3TelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3TSCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3TSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3TSEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3TSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3TSTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM1M3TSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM2CommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM2CommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM2EventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM2EventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM2TelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTM2TelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTMountCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTMountCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTMountEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTMountEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTMountTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTMountTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTPtgCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTPtgCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTPtgEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTPtgEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTPtgTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTPtgTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTTCSCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTTCSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTTCSEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTTCSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTTCSTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTTCSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTVMSCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTVMSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTVMSEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTVMSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTVMSTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_MTVMSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_OCSCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_OCSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_OCSEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_OCSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_OCSTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_OCSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_PointingComponentCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_PointingComponentCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_PointingComponentEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_PointingComponentEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_PointingComponentTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_PointingComponentTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_PromptProcessingEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_PromptProcessingEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_PromptProcessingTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_PromptProcessingTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_RotatorCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_RotatorCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_RotatorEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_RotatorEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_RotatorTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_RotatorTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_SchedulerEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_SchedulerEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_SchedulerTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_SchedulerTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ScriptCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ScriptCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ScriptEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ScriptEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ScriptQueueCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ScriptQueueCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_ScriptQueueEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_ScriptQueueEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_SummitFacilityTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_SummitFacilityTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_TestCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_TestCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_TestEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_TestEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_TestTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_TestTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_TunableLaserCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_TunableLaserCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_TunableLaserEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_TunableLaserEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_TunableLaserTelemetrySubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_TunableLaserTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_WatcherCommandsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_WatcherCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

	def test_WatcherEventsSubsystemNoIDLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')

	def test_WatcherEventsEFDB_TopicNoMySQLReservedWords(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')

if __name__ == "__main__":
	unittest.main(verbosity=2)
