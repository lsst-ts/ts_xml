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

class TestUnits(unittest.TestCase):

	uv = Unit_Validator()

	def test_ATAOSCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATAOSEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATAOSTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATAOS/ATAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATArchiverCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATArchiverEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATArchiverTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATBuildingEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATBuildingTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("CAP-318")
	def test_ATCameraCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("CAP-318")
	def test_ATCameraEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("CAP-318")
	def test_ATCameraTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATCamera/ATCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATDomeCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATDomeEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATDomeTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATDome/ATDome_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATDomeTrajectoryEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATHeaderServiceEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATHexapodCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATHexapodEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATHexapodTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATMCSCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATMCSEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATMCSTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMCS/ATMCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATMonochromatorCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATMonochromatorEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATMonochromatorTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATPneumaticsCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATPneumaticsEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATPneumaticsTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATPtgCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATPtgEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATPtgTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATPtg/ATPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("DM-22158")
	def test_ATSpectrographCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATSpectrographEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATSpectrographTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATTCSCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATTCSEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATTCSTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATTCS/ATTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATWhiteLightCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATWhiteLightEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ATWhiteLightTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_CatchupArchiverEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_CatchupArchiverTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_CBPCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_CBPTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/CBP/CBP_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_DIMMEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_DIMMTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/DIMM/DIMM_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_DomeCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_DomeEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_DomeTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Dome/Dome_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_DSMEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_DSMTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/DSM/DSM_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_EASEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_EASTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/EAS/EAS_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_EFDEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_EFDTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/EFD/EFD_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_EFDTransformationServerEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_EFDTransformationServerTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ElectrometerCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ElectrometerEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Electrometer/Electrometer_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_EnvironmentTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Environment/Environment_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_FiberSpectrographCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_FiberSpectrographEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_FiberSpectrographTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_GenericCameraCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_GenericCameraEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_GenericCameraTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_IOTAEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_IOTATelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/IOTA/IOTA_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_HexapodCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_HexapodEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_HexapodTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Hexapod/Hexapod_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_HVACCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_HVACEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_HVACTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/HVAC/HVAC_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_LinearStageCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_LinearStageEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_LinearStageTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/LinearStage/LinearStage_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_LOVEEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/LOVE/LOVE_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTAOSCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTAOSEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTAOSTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTAOS/MTAOS_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTArchiverEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTArchiverTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("CAP-318")
	def test_MTCameraCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("CAP-318")
	def test_MTCameraEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("CAP-318")
	def test_MTCameraTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTCamera/MTCamera_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTDomeTrajectoryEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTDomeTrajectoryTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("DM-22159")
	def test_MTEECCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTEECEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTEEC/MTEEC_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTGuiderEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTGuiderTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTGuider/MTGuider_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTHeaderServiceEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTLaserTrackerEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTLaserTrackerTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("DM-20956")
	def test_MTM1M3CommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("DM-20956")
	def test_MTM1M3EventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("DM-20956")
	def test_MTM1M3TelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTM1M3TSCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTM1M3TSEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTM1M3TSTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTM2CommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTM2EventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTM2TelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTM2/MTM2_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTMountCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTMountEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTMountTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTMount/MTMount_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTPtgCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTPtgEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTPtgTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTPtg/MTPtg_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTTCSCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTTCSEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTTCSTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTTCS/MTTCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTVMSCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTVMSEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_MTVMSTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/MTVMS/MTVMS_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	@unittest.skip("DM-22160")
	def test_OCSCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_OCSEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_OCSTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/OCS/OCS_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_PointingComponentCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_PointingComponentEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_PointingComponentTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_PromptProcessingEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_PromptProcessingTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_RotatorCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_RotatorEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_RotatorTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Rotator/Rotator_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_SchedulerEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_SchedulerTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Scheduler/Scheduler_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ScriptCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ScriptEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Script/Script_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ScriptQueueCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_ScriptQueueEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_SummitFacilityTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_TestCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_TestEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_TestTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Test/Test_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_TunableLaserCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_TunableLaserEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_TunableLaserTelemetryUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_WatcherCommandsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Commands.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

	def test_WatcherEventsUnitsValid(self):
		self.tree = ET.parse("../sal_interfaces/Watcher/Watcher_Events.xml")
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))

if __name__ == "__main__":
	unittest.main(verbosity=2)
