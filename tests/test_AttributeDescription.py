#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
import xml.etree.ElementTree as ET
cwd = os.getcwd()
sys.path.insert(1, cwd + '/../scripts/unittests')
import xml_common

class TestAttributeDescriptions(unittest.TestCase):

	def test_ATAOSCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATAOSEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATAOSTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATArchiverCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATArchiverEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATArchiverTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATBuildingEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATBuildingTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATCameraCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	@unittest.skip("CAP-318")
	def test_ATCameraEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	@unittest.skip("CAP-318")
	def test_ATCameraTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATDomeCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATDomeEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATDomeTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATDomeTrajectoryEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATHeaderServiceEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATHexapodCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATHexapodEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATHexapodTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATMCSCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATMCSEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATMCSTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATMonochromatorCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATMonochromatorEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATMonochromatorTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATPneumaticsCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATPneumaticsEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATPneumaticsTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATPtgCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATPtgEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATPtgTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATSpectrographCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATSpectrographEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATSpectrographTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATTCSCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATTCSEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATTCSTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATWhiteLightCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATWhiteLightEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ATWhiteLightTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_CatchupArchiverEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_CatchupArchiverTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_CBPCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_CBPTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_DIMMEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_DIMMTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_DomeCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_DomeEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_DomeTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_DSMEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_DSMTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_EASEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_EASTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_EFDEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_EFDTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_EFDTransformationServerEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_EFDTransformationServerTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ElectrometerCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ElectrometerEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_EnvironmentTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Environment/Environment_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_FiberSpectrographCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_FiberSpectrographEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_FiberSpectrographTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_GenericCameraCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_GenericCameraEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_GenericCameraTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_IOTAEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_IOTATelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_HexapodCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	@unittest.skip("DM-20971")
	def test_HexapodEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	@unittest.skip("DM-20971")
	def test_HexapodTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_HVACCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_HVACEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_HVACTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_LinearStageCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_LinearStageEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_LinearStageTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_LOVEEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTAOSCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTAOSEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTAOSTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTArchiverEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTArchiverTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTCameraCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	@unittest.skip("CAP-318")
	def test_MTCameraEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	@unittest.skip("CAP-318")
	def test_MTCameraTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTDomeTrajectoryEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTDomeTrajectoryTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	@unittest.skip("CAP-374")
	def test_MTEECCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTEECEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTGuiderEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTGuiderTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTHeaderServiceEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTLaserTrackerEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTLaserTrackerTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	@unittest.skip("DM-20956")
	def test_MTM1M3CommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	@unittest.skip("DM-20956")
	def test_MTM1M3EventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	@unittest.skip("DM-20956")
	def test_MTM1M3TelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTM1M3TSCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTM1M3TSEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTM1M3TSTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTM2CommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTM2EventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTM2TelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	@unittest.skip("DM-17276")
	def test_MTMountCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTMountEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTMountTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTPtgCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTPtgEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTPtgTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTTCSCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTTCSEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTTCSTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTVMSCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTVMSEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_MTVMSTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_OCSCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_OCSEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_OCSTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_PointingComponentCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_PointingComponentEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_PointingComponentTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_PromptProcessingEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_PromptProcessingTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_RotatorCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_RotatorEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_RotatorTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_SchedulerEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_SchedulerTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ScriptCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ScriptEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ScriptQueueCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_ScriptQueueEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_SummitFacilityTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_TestCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_TestEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_TestTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_TunableLaserCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_TunableLaserEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_TunableLaserTelemetryAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_WatcherCommandsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

	def test_WatcherEventsAttributeDescriptions(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')

if __name__ == "__main__":
	unittest.main(verbosity=2)
