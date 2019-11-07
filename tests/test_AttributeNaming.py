#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
import xml.etree.ElementTree as ET
cwd = os.getcwd()
sys.path.insert(1, cwd + '/../scripts/unittests')
import xml_common

class TestAttributeNaming(unittest.TestCase):

	def test_ATAOSCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATAOSEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATAOSTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATAOS/ATAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATArchiverCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATArchiverEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATArchiverTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATBuildingEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATBuildingTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATCameraCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATCameraEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATCameraTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATCamera/ATCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATDome/ATDome_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATDomeTrajectoryEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHeaderServiceEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHexapodCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHexapodEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATHexapodTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMCSCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMCSEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMCSTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATMCS/ATMCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMonochromatorCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMonochromatorEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATMonochromatorTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPneumaticsCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPneumaticsEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPneumaticsTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPtgCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPtgEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATPtgTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATPtg/ATPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATSpectrographCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATSpectrographEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATSpectrographTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATTCSCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATTCSEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATTCSTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATTCS/ATTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATWhiteLightCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATWhiteLightEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ATWhiteLightTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CatchupArchiverEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CatchupArchiverTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CBPCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_CBPTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/CBP/CBP_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DIMMEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DIMMTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/DIMM/DIMM_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DomeCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DomeEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DomeTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Dome/Dome_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DSMEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_DSMTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/DSM/DSM_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EASEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EASTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/EAS/EAS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EFDEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EFDTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/EFD/EFD_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EFDTransformationServerEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EFDTransformationServerTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ElectrometerCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ElectrometerEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_EnvironmentTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Environment/Environment_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_FiberSpectrographCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_FiberSpectrographEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_FiberSpectrographTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_GenericCameraCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_GenericCameraEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_GenericCameraTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_IOTAEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_IOTATelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/IOTA/IOTA_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HexapodCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HexapodEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HexapodTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Hexapod/Hexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HVACCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HVACEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_HVACTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/HVAC/HVAC_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LinearStageCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LinearStageEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LinearStageTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/LinearStage/LinearStage_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_LOVEEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTAOSCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTAOSEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTAOSTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTAOS/MTAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTArchiverEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTArchiverTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTCameraCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTCameraEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTCameraTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTCamera/MTCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTDomeTrajectoryEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTDomeTrajectoryTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTEECCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTEECEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTGuiderEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTGuiderTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTGuider/MTGuider_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTHeaderServiceEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTLaserTrackerEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTLaserTrackerTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3CommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3EventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TSCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TSEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM1M3TSTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM2CommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM2EventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTM2TelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTM2/MTM2_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTMountCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTMountEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTMountTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTMount/MTMount_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTPtgCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTPtgEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTPtgTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTPtg/MTPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTTCSCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTTCSEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTTCSTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTTCS/MTTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTVMSCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTVMSEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_MTVMSTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/MTVMS/MTVMS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_OCSCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_OCSEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_OCSTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/OCS/OCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PointingComponentCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PointingComponentEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PointingComponentTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PromptProcessingEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_PromptProcessingTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_RotatorCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_RotatorEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_RotatorTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Rotator/Rotator_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_SchedulerEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_SchedulerTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Scheduler/Scheduler_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptQueueCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_ScriptQueueEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_SummitFacilityTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TestCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TestEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TestTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Test/Test_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TunableLaserCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TunableLaserEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_TunableLaserTelemetryAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALTelemetry/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_WatcherCommandsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALCommand/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

	def test_WatcherEventsAttributeNaming(self):
		self.attributes = []
		self.tree = ET.parse("/Users/rbovill/trunk/ts_xml/scripts/unittests/../../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for attribute in self.root.findall('./SALEvent/item/EFDB_Name'):
			self.assertRegex(attribute.text, r'^[a-z]([a-z0-9]*)', msg='Attribute ' + attribute.text + ' does not being with a lowercase letter and/or contains non-alphanumeric characters.')

if __name__ == "__main__":
	unittest.main(verbosity=2)
