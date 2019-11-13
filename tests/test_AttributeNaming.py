#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import xml.etree.ElementTree as ET
import xml_common

class TestAttributeNaming(unittest.TestCase):

	def test_ATAOSCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATAOSEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATAOSTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATArchiverCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATArchiverEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATArchiverTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATBuildingEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATBuildingTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATCameraCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATCameraEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATCameraTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeTrajectoryEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHeaderServiceEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHexapodCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHexapodEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHexapodTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMCSCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMCSEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMCSTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMonochromatorCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMonochromatorEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMonochromatorTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPneumaticsCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPneumaticsEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPneumaticsTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPtgCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPtgEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPtgTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATSpectrographCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATSpectrographEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATSpectrographTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATTCSCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATTCSEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATTCSTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATWhiteLightCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATWhiteLightEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATWhiteLightTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CatchupArchiverEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CatchupArchiverTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CBPCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CBPTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DIMMEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DIMMTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DomeCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DomeEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DomeTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DSMEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DSMTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EASEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EASTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EFDEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EFDTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EFDTransformationServerEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EFDTransformationServerTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ElectrometerCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ElectrometerEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EnvironmentTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Environment/Environment_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_FiberSpectrographCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_FiberSpectrographEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_FiberSpectrographTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_GenericCameraCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_GenericCameraEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_GenericCameraTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_IOTAEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_IOTATelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HexapodCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HexapodEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	@unittest.skip("DM-20971")
	def test_HexapodTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HVACCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HVACEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HVACTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LinearStageCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LinearStageEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LinearStageTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LOVEEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTAOSCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTAOSEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTAOSTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTArchiverEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTArchiverTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTCameraCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTCameraEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTCameraTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTDomeTrajectoryEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTDomeTrajectoryTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTEECCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTEECEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTGuiderEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTGuiderTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTHeaderServiceEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTLaserTrackerEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTLaserTrackerTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3CommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3EventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TSCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TSEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TSTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM2CommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM2EventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM2TelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTMountCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTMountEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	@unittest.skip("DM-17276")
	def test_MTMountTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTPtgCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTPtgEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTPtgTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTTCSCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTTCSEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTTCSTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTVMSCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTVMSEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTVMSTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_OCSCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_OCSEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_OCSTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PointingComponentCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PointingComponentEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PointingComponentTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PromptProcessingEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PromptProcessingTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_RotatorCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_RotatorEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	@unittest.skip("DM-20969")
	def test_RotatorTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_SchedulerEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_SchedulerTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptQueueCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptQueueEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_SummitFacilityTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TestCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TestEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TestTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TunableLaserCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TunableLaserEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TunableLaserTelemetryAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_WatcherCommandsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_WatcherEventsAttributeNaming(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')

if __name__ == "__main__":
	unittest.main(verbosity=2)
