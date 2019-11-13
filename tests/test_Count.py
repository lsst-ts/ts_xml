#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import xml.etree.ElementTree as ET
import xml_common
from Unit_Validator import Unit_Validator

class TestCount(unittest.TestCase):

	uv = Unit_Validator()

	def test_ATAOSCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATAOSEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATAOSTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATArchiverCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATArchiverEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATArchiverTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATBuildingEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATBuildingTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATCameraCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATCameraEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATCameraTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATDomeCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATDomeEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATDomeTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATDomeTrajectoryEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATHeaderServiceEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATHexapodCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATHexapodEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATHexapodTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATMCSCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATMCSEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATMCSTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATMonochromatorCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATMonochromatorEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATMonochromatorTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATPneumaticsCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATPneumaticsEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATPneumaticsTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATPtgCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATPtgEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATPtgTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATSpectrographCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATSpectrographEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATSpectrographTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATTCSCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATTCSEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATTCSTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATWhiteLightCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATWhiteLightEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ATWhiteLightTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_CatchupArchiverEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_CatchupArchiverTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_CBPCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_CBPTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_DIMMEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_DIMMTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_DomeCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_DomeEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_DomeTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_DSMEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_DSMTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_EASEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_EASTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_EFDEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_EFDTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_EFDTransformationServerEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_EFDTransformationServerTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ElectrometerCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ElectrometerEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_EnvironmentTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Environment/Environment_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_FiberSpectrographCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_FiberSpectrographEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_FiberSpectrographTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_GenericCameraCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_GenericCameraEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_GenericCameraTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_IOTAEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_IOTATelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_HexapodCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_HexapodEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_HexapodTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_HVACCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_HVACEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_HVACTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_LinearStageCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_LinearStageEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_LinearStageTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_LOVEEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTAOSCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTAOSEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTAOSTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTArchiverEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTArchiverTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTCameraCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTCameraEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTCameraTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTDomeTrajectoryEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTDomeTrajectoryTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTEECCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTEECEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTGuiderEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTGuiderTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTHeaderServiceEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTLaserTrackerEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTLaserTrackerTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTM1M3CommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTM1M3EventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTM1M3TelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTM1M3TSCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTM1M3TSEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTM1M3TSTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTM2CommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTM2EventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTM2TelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTMountCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTMountEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTMountTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTPtgCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTPtgEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTPtgTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTTCSCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTTCSEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTTCSTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTVMSCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTVMSEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_MTVMSTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_OCSCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_OCSEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_OCSTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_PointingComponentCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_PointingComponentEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_PointingComponentTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_PromptProcessingEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_PromptProcessingTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_RotatorCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_RotatorEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_RotatorTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_SchedulerEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_SchedulerTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ScriptCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ScriptEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ScriptQueueCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_ScriptQueueEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_SummitFacilityTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_TestCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_TestEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_TestTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_TunableLaserCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_TunableLaserEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_TunableLaserTelemetryCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_WatcherCommandsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

	def test_WatcherEventsCountValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')
		self.file.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)
