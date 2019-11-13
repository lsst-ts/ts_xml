#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import xml.etree.ElementTree as ET
import xml_common

class TestAlias(unittest.TestCase):

	def test_ATAOSCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATAOSEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATAOS/ATAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATArchiverCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATArchiverEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATArchiver/ATArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATBuildingEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATBuilding/ATBuilding_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATCameraCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATCameraEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATCamera/ATCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATDomeCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATDomeEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDome/ATDome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATDomeTrajectoryEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATDomeTrajectory/ATDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATHeaderServiceEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHeaderService/ATHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATHexapodCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATHexapodEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATHexapod/ATHexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATMCSCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATMCSEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMCS/ATMCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATMonochromatorCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATMonochromatorEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATMonochromator/ATMonochromator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATPneumaticsCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATPneumaticsEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPneumatics/ATPneumatics_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATPtgCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATPtgEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATPtg/ATPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATSpectrographCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATSpectrographEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATSpectrograph/ATSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATTCSCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATTCSEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATTCS/ATTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATWhiteLightCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ATWhiteLightEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ATWhiteLight/ATWhiteLight_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_CatchupArchiverEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CatchupArchiver/CatchupArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_CBPCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/CBP/CBP_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_DIMMEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DIMM/DIMM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_DomeCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_DomeEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Dome/Dome_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_DSMEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/DSM/DSM_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_EASEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EAS/EAS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_EFDEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFD/EFD_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_EFDTransformationServerEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/EFDTransformationServer/EFDTransformationServer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ElectrometerCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ElectrometerEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Electrometer/Electrometer_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_FiberSpectrographCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_FiberSpectrographEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/FiberSpectrograph/FiberSpectrograph_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_GenericCameraCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_GenericCameraEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/GenericCamera/GenericCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_IOTAEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/IOTA/IOTA_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_HexapodCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_HexapodEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Hexapod/Hexapod_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_HVACCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_HVACEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/HVAC/HVAC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_LinearStageCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_LinearStageEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LinearStage/LinearStage_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_LOVEEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/LOVE/LOVE_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTAOSCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTAOSEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTAOS/MTAOS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTArchiverEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTArchiver/MTArchiver_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTCameraCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTCameraEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTCamera/MTCamera_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTDomeTrajectoryEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTDomeTrajectory/MTDomeTrajectory_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTEECCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTEECEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTEEC/MTEEC_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTGuiderEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTGuider/MTGuider_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTHeaderServiceEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTHeaderService/MTHeaderService_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTLaserTrackerEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTLaserTracker/MTLaserTracker_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTM1M3CommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTM1M3EventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3/MTM1M3_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTM1M3TSCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTM1M3TSEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM1M3TS/MTM1M3TS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTM2CommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTM2EventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTM2/MTM2_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTMountCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTMountEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTMount/MTMount_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTPtgCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTPtgEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTPtg/MTPtg_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTTCSCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTTCSEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTTCS/MTTCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTVMSCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_MTVMSEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/MTVMS/MTVMS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_OCSCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_OCSEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/OCS/OCS_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_PointingComponentCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_PointingComponentEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PointingComponent/PointingComponent_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_PromptProcessingEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/PromptProcessing/PromptProcessing_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_RotatorCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_RotatorEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Rotator/Rotator_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_SchedulerEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Scheduler/Scheduler_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ScriptCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ScriptEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Script/Script_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ScriptQueueCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_ScriptQueueEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/ScriptQueue/ScriptQueue_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_TestCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_TestEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Test/Test_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_TunableLaserCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_TunableLaserEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/TunableLaser/TunableLaser_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_WatcherCommandsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Commands.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALCommand/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALCommand/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

	def test_WatcherEventsAliases(self):
		self.csc_aliases = []
		self.csc_topics = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.file = open(self.dir_path + '/../sal_interfaces/Watcher/Watcher_Events.xml')
		self.tree = ET.parse(self.file)
		self.root = self.tree.getroot()
		for alias in self.root.findall('./SALEvent/Alias'):
			self.csc_aliases.append(alias.text)
		for topic in self.root.findall('./SALEvent/EFDB_Topic'):
			self.csc_topics.append(topic.text.split('_',2)[2])
		self.csc_aliases.sort()
		self.csc_topics.sort()
		self.assertEqual(self.csc_aliases, self.csc_topics)
		self.file.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)
