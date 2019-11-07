#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
import xml.etree.ElementTree as ET
cwd = os.getcwd()
sys.path.insert(1, cwd + '/../scripts/unittests')
import xml_common

class TestGenerics(unittest.TestCase):

	# Variables #
	tree = ET.parse(cwd + "/../sal_interfaces/SALGenerics.xml")
	root = tree.getroot()
	generic_commands = xml_common.generic_commands
	generic_events = xml_common.generic_events
	command_xml_path = '/SALObjects/SALCommandSet/SALCommand'
	event_xml_path = '/SALObjects/SALEventSet/SALEvent'
	commands = []
	events = []

	def test_SALGenericsCommands(self):
		for alias in self.root.findall('./SALCommandSet/SALCommand/Alias'):
			self.commands.append(alias.text)
		self.commands.sort()
		self.generic_commands.sort()
		self.assertEqual(self.commands, self.generic_commands)

	def test_SALGenericsEvents(self):
		for alias in self.root.findall('./SALEventSet/SALEvent/Alias'):
			self.events.append(alias.text)
		self.events.sort()
		self.generic_events.sort()
		self.assertEqual(self.events, self.generic_events)

	def test_ValidateATAOSDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATAOS/ATAOS_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATAOS Events XML")

	def test_ValidateATAOSDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATAOS Commands XML")

	def test_ValidateATArchiverDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATArchiver Events XML")

	def test_ValidateATArchiverDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATArchiver Commands XML")

	def test_ValidateATBuildingDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATBuilding Events XML")

	def test_ValidateATCameraDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATCamera/ATCamera_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATCamera Events XML")

	def test_ValidateATCameraDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATCamera Commands XML")

	def test_ValidateATDomeDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATDome/ATDome_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATDome Events XML")

	def test_ValidateATDomeDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATDome/ATDome_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATDome Commands XML")

	def test_ValidateATDomeTrajectoryDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATDomeTrajectory Events XML")

	def test_ValidateATHeaderServiceDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATHeaderService Events XML")

	def test_ValidateATHexapodDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATHexapod Events XML")

	def test_ValidateATHexapodDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATHexapod Commands XML")

	def test_ValidateATMCSDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATMCS/ATMCS_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATMCS Events XML")

	def test_ValidateATMCSDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATMCS Commands XML")

	def test_ValidateATMonochromatorDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATMonochromator Events XML")

	def test_ValidateATMonochromatorDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATMonochromator Commands XML")

	def test_ValidateATPneumaticsDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATPneumatics Events XML")

	def test_ValidateATPneumaticsDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATPneumatics Commands XML")

	def test_ValidateATPtgDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATPtg/ATPtg_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATPtg Events XML")

	def test_ValidateATPtgDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATPtg Commands XML")

	def test_ValidateATSpectrographDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATSpectrograph Events XML")

	def test_ValidateATSpectrographDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATSpectrograph Commands XML")

	def test_ValidateATTCSDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATTCS/ATTCS_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATTCS Events XML")

	def test_ValidateATTCSDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATTCS Commands XML")

	def test_ValidateATWhiteLightDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ATWhiteLight Events XML")

	def test_ValidateATWhiteLightDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ATWhiteLight Commands XML")

	def test_ValidateCatchupArchiverDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the CatchupArchiver Events XML")

	def test_ValidateCBPDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/CBP/CBP_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the CBP Commands XML")

	def test_ValidateDIMMDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/DIMM/DIMM_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the DIMM Events XML")

	def test_ValidateDomeDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Dome/Dome_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the Dome Events XML")

	def test_ValidateDomeDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Dome/Dome_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the Dome Commands XML")

	def test_ValidateDSMDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/DSM/DSM_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the DSM Events XML")

	def test_ValidateEASDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/EAS/EAS_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the EAS Events XML")

	def test_ValidateEFDDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/EFD/EFD_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the EFD Events XML")

	def test_ValidateEFDTransformationServerDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the EFDTransformationServer Events XML")

	def test_ValidateElectrometerDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Electrometer/Electrometer_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the Electrometer Events XML")

	def test_ValidateElectrometerDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the Electrometer Commands XML")

	def test_ValidateFiberSpectrographDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the FiberSpectrograph Events XML")

	def test_ValidateFiberSpectrographDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the FiberSpectrograph Commands XML")

	def test_ValidateGenericCameraDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the GenericCamera Events XML")

	def test_ValidateGenericCameraDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the GenericCamera Commands XML")

	def test_ValidateIOTADoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/IOTA/IOTA_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the IOTA Events XML")

	def test_ValidateHexapodDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Hexapod/Hexapod_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the Hexapod Events XML")

	def test_ValidateHexapodDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the Hexapod Commands XML")

	def test_ValidateHVACDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/HVAC/HVAC_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the HVAC Events XML")

	def test_ValidateHVACDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/HVAC/HVAC_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the HVAC Commands XML")

	def test_ValidateLinearStageDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/LinearStage/LinearStage_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the LinearStage Events XML")

	def test_ValidateLinearStageDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the LinearStage Commands XML")

	def test_ValidateLOVEDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/LOVE/LOVE_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the LOVE Events XML")

	def test_ValidateMTAOSDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTAOS/MTAOS_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTAOS Events XML")

	def test_ValidateMTAOSDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the MTAOS Commands XML")

	def test_ValidateMTArchiverDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTArchiver Events XML")

	def test_ValidateMTCameraDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTCamera/MTCamera_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTCamera Events XML")

	def test_ValidateMTCameraDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the MTCamera Commands XML")

	def test_ValidateMTDomeTrajectoryDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTDomeTrajectory Events XML")

	def test_ValidateMTEECDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTEEC/MTEEC_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTEEC Events XML")

	def test_ValidateMTEECDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the MTEEC Commands XML")

	def test_ValidateMTGuiderDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTGuider/MTGuider_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTGuider Events XML")

	def test_ValidateMTHeaderServiceDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTHeaderService Events XML")

	def test_ValidateMTLaserTrackerDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTLaserTracker Events XML")

	def test_ValidateMTM1M3DoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTM1M3 Events XML")

	def test_ValidateMTM1M3DoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the MTM1M3 Commands XML")

	def test_ValidateMTM1M3TSDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTM1M3TS Events XML")

	def test_ValidateMTM1M3TSDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the MTM1M3TS Commands XML")

	def test_ValidateMTM2DoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTM2/MTM2_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTM2 Events XML")

	def test_ValidateMTM2DoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTM2/MTM2_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the MTM2 Commands XML")

	def test_ValidateMTMountDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTMount/MTMount_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTMount Events XML")

	def test_ValidateMTMountDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTMount/MTMount_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the MTMount Commands XML")

	def test_ValidateMTPtgDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTPtg/MTPtg_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTPtg Events XML")

	def test_ValidateMTPtgDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the MTPtg Commands XML")

	def test_ValidateMTTCSDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTTCS/MTTCS_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTTCS Events XML")

	def test_ValidateMTTCSDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the MTTCS Commands XML")

	def test_ValidateMTVMSDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTVMS/MTVMS_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the MTVMS Events XML")

	def test_ValidateMTVMSDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the MTVMS Commands XML")

	def test_ValidateOCSDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/OCS/OCS_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the OCS Events XML")

	def test_ValidateOCSDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/OCS/OCS_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the OCS Commands XML")

	def test_ValidatePointingComponentDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the PointingComponent Events XML")

	def test_ValidatePointingComponentDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the PointingComponent Commands XML")

	def test_ValidatePromptProcessingDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the PromptProcessing Events XML")

	def test_ValidateRotatorDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Rotator/Rotator_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the Rotator Events XML")

	def test_ValidateRotatorDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Rotator/Rotator_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the Rotator Commands XML")

	def test_ValidateSchedulerDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Scheduler/Scheduler_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the Scheduler Events XML")

	def test_ValidateScriptDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Script/Script_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the Script Events XML")

	def test_ValidateScriptDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Script/Script_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the Script Commands XML")

	def test_ValidateScriptQueueDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the ScriptQueue Events XML")

	def test_ValidateScriptQueueDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the ScriptQueue Commands XML")

	def test_ValidateTestDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Test/Test_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the Test Events XML")

	def test_ValidateTestDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Test/Test_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the Test Commands XML")

	def test_ValidateTunableLaserDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the TunableLaser Events XML")

	def test_ValidateTunableLaserDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the TunableLaser Commands XML")

	def test_ValidateWatcherDoesNotContainGenericEvents(self):
		self.csc_events = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Watcher/Watcher_Events.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_events.append(alias.text)
		for event in self.csc_events:
			self.assertTrue(event not in self.generic_events, msg="Generic event " + event + " is incorrectly defined in the Watcher Events XML")

	def test_ValidateWatcherDoesNotContainGenericCommands(self):
		self.csc_commands = []
		self.csc_tree = ET.parse(cwd + "/../sal_interfaces/Watcher/Watcher_Commands.xml")
		for alias in self.csc_tree.findall('./SALEvent/Alias'):
			self.csc_commands.append(alias.text)
		for event in self.csc_commands:
			self.assertTrue(event not in self.generic_commands, msg="Generic command " + command + " is incorrectly defined in the Watcher Commands XML")

if __name__ == "__main__":
	unittest.main(verbosity=2)
