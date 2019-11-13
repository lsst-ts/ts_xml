#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import xml.etree.ElementTree as ET
import xml_common
from Unit_Validator import Unit_Validator

class TestUnits(unittest.TestCase):

	uv = Unit_Validator()

	def test_ATAOSCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATAOSEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATAOSTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATArchiverCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATArchiverEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATArchiverTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATBuildingEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATBuildingTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("CAP-318")
	def test_ATCameraCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("CAP-318")
	def test_ATCameraEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("CAP-318")
	def test_ATCameraTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATDomeCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATDomeEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATDomeTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATDomeTrajectoryEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATHeaderServiceEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATHexapodCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATHexapodEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATHexapodTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATMCSCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATMCSEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATMCSTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATMonochromatorCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATMonochromatorEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATMonochromatorTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATPneumaticsCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATPneumaticsEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATPneumaticsTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATPtgCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATPtgEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATPtgTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("DM-22158")
	def test_ATSpectrographCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATSpectrographEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATSpectrographTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATTCSCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATTCSEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATTCSTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATWhiteLightCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATWhiteLightEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ATWhiteLightTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_CBPCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_CBPTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_CatchupArchiverEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_CatchupArchiverTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_DIMMEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_DIMMTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_DSMEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_DSMTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_DomeCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_DomeEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_DomeTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_EASEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_EASTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_EFDEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_EFDTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_EFDTransformationServerEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_EFDTransformationServerTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ElectrometerCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ElectrometerEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_EnvironmentTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Environment/Environment_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_FiberSpectrographCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_FiberSpectrographEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_FiberSpectrographTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_GenericCameraCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_GenericCameraEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_GenericCameraTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_HVACCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_HVACEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_HVACTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_HexapodCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_HexapodEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_HexapodTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_IOTAEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_IOTATelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_LOVEEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_LinearStageCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_LinearStageEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_LinearStageTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTAOSCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTAOSEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTAOSTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTArchiverEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTArchiverTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("CAP-318")
	def test_MTCameraCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("CAP-318")
	def test_MTCameraEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("CAP-318")
	def test_MTCameraTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTDomeTrajectoryEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTDomeTrajectoryTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("DM-22159")
	def test_MTEECCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTEECEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTGuiderEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTGuiderTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTHeaderServiceEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTLaserTrackerEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTLaserTrackerTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("DM-20956")
	def test_MTM1M3CommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("DM-20956")
	def test_MTM1M3EventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("DM-20956")
	def test_MTM1M3TelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTM1M3TSCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTM1M3TSEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTM1M3TSTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTM2CommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTM2EventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTM2TelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTMountCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTMountEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTMountTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTPtgCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTPtgEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTPtgTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTTCSCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTTCSEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTTCSTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTVMSCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTVMSEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_MTVMSTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	@unittest.skip("DM-22160")
	def test_OCSCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_OCSEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_OCSTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_PointingComponentCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_PointingComponentEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_PointingComponentTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_PromptProcessingEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_PromptProcessingTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_RotatorCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_RotatorEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_RotatorTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_SchedulerEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_SchedulerTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ScriptCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ScriptEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ScriptQueueCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_ScriptQueueEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_SummitFacilityTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/SummitFacility/SummitFacility_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_TestCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_TestEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_TestTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_TunableLaserCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_TunableLaserEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_TunableLaserTelemetryUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Telemetry.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALTelemetry/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_WatcherCommandsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALCommand/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

	def test_WatcherEventsUnitsValid(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for unit in self.root.findall('./SALEvent/item/Units'):
			if not unit.text:
				self.assertTrue(False, msg='Units cannot be blank.')
			elif unit.text == "unitless" or unit.text == "dimensionless":
				self.assertTrue(True)
			else:
				self.assertNotIn('Error', self.uv.check_unit(unit.text))
		self.file.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)
