#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import xml.etree.ElementTree as ET
import xml_common

class TestAttributeDescriptions(unittest.TestCase):

	def test_ATAOSCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATAOSEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATAOSTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATArchiverCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATArchiverEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATArchiverTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATBuildingEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATBuildingTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATCameraCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	@unittest.skip("CAP-318")
	def test_ATCameraEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	@unittest.skip("CAP-318")
	def test_ATCameraTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATDomeCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATDomeEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATDomeTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATDomeTrajectoryEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATHeaderServiceEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATHexapodCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATHexapodEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATHexapodTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATMCSCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATMCSEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATMCSTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATMonochromatorCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATMonochromatorEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATMonochromatorTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATPneumaticsCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATPneumaticsEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATPneumaticsTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATPtgCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATPtgEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATPtgTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATSpectrographCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATSpectrographEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATSpectrographTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATTCSCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATTCSEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATTCSTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATWhiteLightCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATWhiteLightEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ATWhiteLightTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_CatchupArchiverEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_CatchupArchiverTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_CBPCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_CBPTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_DIMMEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_DIMMTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_DomeCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_DomeEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_DomeTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_DSMEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_DSMTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_EASEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_EASTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_EFDEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_EFDTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_EFDTransformationServerEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_EFDTransformationServerTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ElectrometerCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ElectrometerEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_EnvironmentTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Environment/Environment_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_FiberSpectrographCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_FiberSpectrographEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_FiberSpectrographTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_GenericCameraCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_GenericCameraEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_GenericCameraTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_IOTAEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_IOTATelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_HexapodCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	@unittest.skip("DM-20971")
	def test_HexapodEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	@unittest.skip("DM-20971")
	def test_HexapodTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_HVACCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_HVACEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_HVACTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_LinearStageCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_LinearStageEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_LinearStageTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_LOVEEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTAOSCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTAOSEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTAOSTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTArchiverEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTArchiverTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTCameraCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	@unittest.skip("CAP-318")
	def test_MTCameraEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	@unittest.skip("CAP-318")
	def test_MTCameraTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTDomeTrajectoryEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTDomeTrajectoryTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	@unittest.skip("CAP-374")
	def test_MTEECCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTEECEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTGuiderEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTGuiderTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTHeaderServiceEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTLaserTrackerEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTLaserTrackerTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	@unittest.skip("DM-20956")
	def test_MTM1M3CommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	@unittest.skip("DM-20956")
	def test_MTM1M3EventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	@unittest.skip("DM-20956")
	def test_MTM1M3TelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTM1M3TSCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTM1M3TSEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTM1M3TSTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTM2CommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTM2EventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTM2TelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	@unittest.skip("DM-17276")
	def test_MTMountCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTMountEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTMountTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTPtgCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTPtgEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTPtgTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTTCSCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTTCSEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTTCSTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTVMSCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTVMSEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_MTVMSTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_OCSCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_OCSEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_OCSTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_PointingComponentCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_PointingComponentEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_PointingComponentTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_PromptProcessingEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_PromptProcessingTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_RotatorCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_RotatorEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_RotatorTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_SchedulerEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_SchedulerTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ScriptCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ScriptEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ScriptQueueCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_ScriptQueueEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_SummitFacilityTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_TestCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_TestEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_TestTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_TunableLaserCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_TunableLaserEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_TunableLaserTelemetryAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALTelemetry/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_WatcherCommandsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALCommand/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

	def test_WatcherEventsAttributeDescriptions(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for description in self.root.findall('./SALEvent/item/Description'):
			self.assertNotEqual(description.text.strip(), '', msg='Description cannot be blank.')
		self.file.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)
