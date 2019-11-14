#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import xml.etree.ElementTree as ET
import xml_common

class TestAttributeNaming(unittest.TestCase):

	def test_ATAOSCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATAOSEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATAOSTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATArchiverCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATArchiverEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATArchiverTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATBuildingEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATBuildingTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATCameraCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATCameraEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATCameraTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATDomeCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATDomeEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATDomeTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATDomeTrajectoryEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATHeaderServiceEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATHexapodCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATHexapodEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATHexapodTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMCSCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMCSEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMCSTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMonochromatorCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMonochromatorEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATMonochromatorTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPneumaticsCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPneumaticsEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPneumaticsTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPtgCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPtgEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATPtgTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATSpectrographCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATSpectrographEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATSpectrographTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATTCSCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATTCSEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATTCSTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATWhiteLightCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATWhiteLightEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ATWhiteLightTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_CatchupArchiverEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_CatchupArchiverTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_CBPCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_CBPTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DIMMEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DIMMTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DomeCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DomeEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DomeTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DSMEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_DSMTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EASEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EASTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EFDEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EFDTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EFDTransformationServerEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EFDTransformationServerTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ElectrometerCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ElectrometerEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_EnvironmentTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Environment/Environment_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_FiberSpectrographCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_FiberSpectrographEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_FiberSpectrographTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_GenericCameraCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_GenericCameraEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_GenericCameraTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_IOTAEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_IOTATelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_HexapodCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_HexapodEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	@unittest.skip("DM-20971")
	def test_HexapodTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_HVACCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_HVACEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_HVACTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_LinearStageCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_LinearStageEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_LinearStageTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_LOVEEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTAOSCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTAOSEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTAOSTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTArchiverEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTArchiverTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTCameraCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTCameraEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTCameraTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTDomeTrajectoryEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTDomeTrajectoryTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTEECCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTEECEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTGuiderEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTGuiderTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTHeaderServiceEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTLaserTrackerEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTLaserTrackerTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3CommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3EventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3TelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3TSCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3TSEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM1M3TSTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM2CommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM2EventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTM2TelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTMountCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTMountEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	@unittest.skip("DM-17276")
	def test_MTMountTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTPtgCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTPtgEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTPtgTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTTCSCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTTCSEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTTCSTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTVMSCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTVMSEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_MTVMSTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_OCSCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_OCSEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_OCSTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_PointingComponentCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_PointingComponentEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_PointingComponentTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_PromptProcessingEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_PromptProcessingTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_RotatorCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_RotatorEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	@unittest.skip("DM-20969")
	def test_RotatorTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_SchedulerEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_SchedulerTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ScriptCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ScriptEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ScriptQueueCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_ScriptQueueEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_SummitFacilityTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TestCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TestEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TestTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TunableLaserCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TunableLaserEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_TunableLaserTelemetryAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_WatcherCommandsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

	def test_WatcherEventsAttributeNaming(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml', 'r', encoding='utf-8')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not begin with a lowercase letter and/or contains non-alphanumeric characters.')
		self.file.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)
