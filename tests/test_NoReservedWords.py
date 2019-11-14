#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import xml.etree.ElementTree as ET
import xml_common

class TestNoReservedWords(unittest.TestCase):

	def test_ATAOSCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATAOSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATAOSEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATAOSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATAOSTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATAOSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATArchiverCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATArchiverCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATArchiverEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATArchiverEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATArchiverTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATArchiverTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATBuildingEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATBuildingEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATBuildingTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATBuildingTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATCameraCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATCameraCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATCameraEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATCameraEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATCameraTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATCameraTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATDomeCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATDomeCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATDomeEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATDomeEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATDomeTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATDomeTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATDomeTrajectoryEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATDomeTrajectoryEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATHeaderServiceEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATHeaderServiceEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATHexapodCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATHexapodCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATHexapodEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATHexapodEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATHexapodTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATHexapodTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMCSCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMCSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMCSEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMCSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMCSTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMCSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMonochromatorCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMonochromatorCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMonochromatorEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMonochromatorEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMonochromatorTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATMonochromatorTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPneumaticsCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPneumaticsCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPneumaticsEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPneumaticsEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPneumaticsTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPneumaticsTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPtgCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPtgCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPtgEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPtgEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPtgTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATPtgTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATSpectrographCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATSpectrographCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATSpectrographEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATSpectrographEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATSpectrographTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATSpectrographTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATTCSCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATTCSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATTCSEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATTCSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATTCSTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATTCSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATWhiteLightCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATWhiteLightCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATWhiteLightEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATWhiteLightEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATWhiteLightTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ATWhiteLightTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_CatchupArchiverEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_CatchupArchiverEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_CatchupArchiverTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_CatchupArchiverTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_CBPCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_CBPCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_CBPTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_CBPTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DIMMEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DIMMEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DIMMTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DIMMTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DomeCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DomeCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DomeEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DomeEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DomeTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DomeTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DSMEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DSMEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DSMTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_DSMTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EASEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EASEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EASTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EASTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EFDEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EFDEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EFDTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EFDTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EFDTransformationServerEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EFDTransformationServerEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EFDTransformationServerTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EFDTransformationServerTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ElectrometerCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ElectrometerCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ElectrometerEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ElectrometerEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EnvironmentTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Environment/Environment_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_EnvironmentTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Environment/Environment_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_FiberSpectrographCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_FiberSpectrographCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_FiberSpectrographEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_FiberSpectrographEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_FiberSpectrographTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_FiberSpectrographTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_GenericCameraCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_GenericCameraCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_GenericCameraEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_GenericCameraEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_GenericCameraTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_GenericCameraTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_IOTAEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_IOTAEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_IOTATelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_IOTATelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HexapodCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HexapodCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HexapodEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HexapodEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HexapodTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HexapodTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HVACCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HVACCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HVACEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HVACEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HVACTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_HVACTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_LinearStageCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_LinearStageCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_LinearStageEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_LinearStageEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_LinearStageTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_LinearStageTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_LOVEEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_LOVEEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTAOSCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTAOSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTAOSEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTAOSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTAOSTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTAOSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTArchiverEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTArchiverEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTArchiverTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTArchiverTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTCameraCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTCameraCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTCameraEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTCameraEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTCameraTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTCameraTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTDomeTrajectoryEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTDomeTrajectoryEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTDomeTrajectoryTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTDomeTrajectoryTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTEECCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTEECCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTEECEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTEECEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTGuiderEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTGuiderEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTGuiderTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTGuiderTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTHeaderServiceEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTHeaderServiceEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTLaserTrackerEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTLaserTrackerEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTLaserTrackerTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTLaserTrackerTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3CommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3CommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3EventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3EventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3TelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3TelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3TSCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3TSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3TSEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3TSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3TSTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM1M3TSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM2CommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM2CommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM2EventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM2EventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM2TelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTM2TelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTMountCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTMountCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTMountEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTMountEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTMountTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTMountTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTPtgCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTPtgCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTPtgEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTPtgEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTPtgTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTPtgTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTTCSCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTTCSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTTCSEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTTCSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTTCSTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTTCSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTVMSCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTVMSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTVMSEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTVMSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTVMSTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_MTVMSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_OCSCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_OCSCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_OCSEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_OCSEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_OCSTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_OCSTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_PointingComponentCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_PointingComponentCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_PointingComponentEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_PointingComponentEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_PointingComponentTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_PointingComponentTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_PromptProcessingEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_PromptProcessingEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_PromptProcessingTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_PromptProcessingTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_RotatorCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_RotatorCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_RotatorEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_RotatorEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_RotatorTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_RotatorTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_SchedulerEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_SchedulerEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_SchedulerTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_SchedulerTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ScriptCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ScriptCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ScriptEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ScriptEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ScriptQueueCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ScriptQueueCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ScriptQueueEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_ScriptQueueEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_SummitFacilityTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_SummitFacilityTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TestCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TestCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TestEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TestEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TestTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TestTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TunableLaserCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TunableLaserCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TunableLaserEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TunableLaserEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TunableLaserTelemetrySubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_TunableLaserTelemetryEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_WatcherCommandsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_WatcherCommandsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_WatcherEventsSubsystemNoIDLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.idl_reserved, msg='IDL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

	def test_WatcherEventsEFDB_TopicNoMySQLReservedWords(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for name in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertNotIn(name.text.upper(), xml_common.mysql_reserved, msg='MySQL Reserved Word ' + name.text + ' used one or more times.')
		self.file.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)
