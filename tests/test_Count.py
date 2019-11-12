#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
import xml.etree.ElementTree as ET
cwd = os.getcwd()
sys.path.insert(1, cwd + '/../scripts/unittests')
import xml_common
from Unit_Validator import Unit_Validator

class TestCount(unittest.TestCase):

	uv = Unit_Validator()

	def test_ATAOSCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATAOSEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATAOSTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATArchiverCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATArchiverEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATArchiverTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATBuildingEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATBuildingTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATCameraCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATCameraEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATCameraTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATDomeCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATDomeEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATDomeTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATDomeTrajectoryEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATHeaderServiceEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATHexapodCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATHexapodEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATHexapodTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATMCSCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATMCSEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATMCSTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATMonochromatorCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATMonochromatorEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATMonochromatorTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATPneumaticsCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATPneumaticsEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATPneumaticsTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATPtgCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATPtgEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATPtgTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATSpectrographCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATSpectrographEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATSpectrographTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATTCSCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATTCSEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATTCSTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATWhiteLightCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATWhiteLightEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ATWhiteLightTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_CatchupArchiverEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_CatchupArchiverTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_CBPCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_CBPTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_DIMMEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_DIMMTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_DomeCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_DomeEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_DomeTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_DSMEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_DSMTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_EASEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_EASTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_EFDEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_EFDTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_EFDTransformationServerEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_EFDTransformationServerTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ElectrometerCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ElectrometerEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_EnvironmentTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Environment/Environment_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_FiberSpectrographCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_FiberSpectrographEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_FiberSpectrographTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_GenericCameraCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_GenericCameraEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_GenericCameraTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_IOTAEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_IOTATelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_HexapodCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_HexapodEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_HexapodTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_HVACCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_HVACEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_HVACTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_LinearStageCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_LinearStageEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_LinearStageTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_LOVEEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTAOSCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTAOSEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTAOSTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTArchiverEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTArchiverTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTCameraCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTCameraEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTCameraTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTDomeTrajectoryEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTDomeTrajectoryTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTEECCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTEECEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTGuiderEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTGuiderTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTHeaderServiceEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTLaserTrackerEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTLaserTrackerTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTM1M3CommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTM1M3EventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTM1M3TelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTM1M3TSCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTM1M3TSEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTM1M3TSTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTM2CommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTM2EventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTM2TelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTMountCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTMountEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTMountTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTPtgCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTPtgEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTPtgTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTTCSCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTTCSEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTTCSTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTVMSCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTVMSEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_MTVMSTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_OCSCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_OCSEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_OCSTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_PointingComponentCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_PointingComponentEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_PointingComponentTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_PromptProcessingEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_PromptProcessingTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_RotatorCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_RotatorEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_RotatorTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_SchedulerEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_SchedulerTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ScriptCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ScriptEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ScriptQueueCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_ScriptQueueEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_SummitFacilityTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_TestCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_TestEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_TestTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_TunableLaserCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_TunableLaserEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_TunableLaserTelemetryCountValid(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALTelemetry/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_WatcherCommandsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALCommand/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

	def test_WatcherEventsCountValid(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for count in self.root.findall('./SALEvent/item/Count'):
			self.assertNotEqual(count.text, None, msg='Count cannot be blank.')

if __name__ == "__main__":
	unittest.main(verbosity=2)
