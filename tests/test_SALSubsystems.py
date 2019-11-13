#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import xml.etree.ElementTree as ET
import xml_common

class TestSALSubsystem(unittest.TestCase):

	# Variables #
	cwd = os.getcwd()
	tree = ET.parse(cwd + "/../sal_interfaces/SALSubsystems.xml")
	root = tree.getroot()
	cscs = xml_common.subsystems

	# Test Cases #
	def test_cscCount(self):
		self.assertEqual(len(self.cscs), 58, msg="Subsystem list has an added or removed entry")

	def test_uniqCSC(self):
		self.assertTrue(len(self.cscs) == len(set(self.cscs)), msg="Subsystem list contains a duplicate entry")

	def test_ataosExists(self):
		self.assertIn("ATAOS", self.cscs)

	def test_ataosGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATAOS']/Generics").text, "yes")

	def test_ataosSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATAOS']/Simulator"), ET.Element, msg="ATAOSSimulator tag is NOT present")

	def test_atarchiverExists(self):
		self.assertIn("ATArchiver", self.cscs)

	def test_atarchiverGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATArchiver']/Generics").text, "yes")

	def test_atarchiverSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATArchiver']/Simulator"), ET.Element, msg="ATArchiverSimulator tag is NOT present")

	def test_atbuildingExists(self):
		self.assertIn("ATBuilding", self.cscs)

	def test_atbuildingGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATBuilding']/Generics").text, "yes")

	def test_atbuildingSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATBuilding']/Simulator"), ET.Element, msg="ATBuildingSimulator tag is NOT present")

	def test_atcameraExists(self):
		self.assertIn("ATCamera", self.cscs)

	def test_atcameraGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATCamera']/Generics").text, "yes")

	def test_atcameraSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATCamera']/Simulator"), ET.Element, msg="ATCameraSimulator tag is NOT present")

	def test_atdomeExists(self):
		self.assertIn("ATDome", self.cscs)

	def test_atdomeGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATDome']/Generics").text, "yes")

	def test_atdomeSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATDome']/Simulator"), ET.Element, msg="ATDomeSimulator tag is NOT present")

	def test_atdometrajectoryExists(self):
		self.assertIn("ATDomeTrajectory", self.cscs)

	def test_atdometrajectoryGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATDomeTrajectory']/Generics").text, "yes")

	def test_atdometrajectorySimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATDomeTrajectory']/Simulator"), ET.Element, msg="ATDomeTrajectorySimulator tag is NOT present")

	def test_atheaderserviceExists(self):
		self.assertIn("ATHeaderService", self.cscs)

	def test_atheaderserviceGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATHeaderService']/Generics").text, "yes")

	def test_atheaderserviceSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATHeaderService']/Simulator"), ET.Element, msg="ATHeaderServiceSimulator tag is NOT present")

	def test_athexapodExists(self):
		self.assertIn("ATHexapod", self.cscs)

	def test_athexapodGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATHexapod']/Generics").text, "yes")

	def test_athexapodSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATHexapod']/Simulator"), ET.Element, msg="ATHexapodSimulator tag is NOT present")

	def test_atmcsExists(self):
		self.assertIn("ATMCS", self.cscs)

	def test_atmcsGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATMCS']/Generics").text, "yes")

	def test_atmcsSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATMCS']/Simulator"), ET.Element, msg="ATMCSSimulator tag is NOT present")

	def test_atmonochromatorExists(self):
		self.assertIn("ATMonochromator", self.cscs)

	def test_atmonochromatorGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATMonochromator']/Generics").text, "yes")

	def test_atmonochromatorSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATMonochromator']/Simulator"), ET.Element, msg="ATMonochromatorSimulator tag is NOT present")

	def test_atpneumaticsExists(self):
		self.assertIn("ATPneumatics", self.cscs)

	def test_atpneumaticsGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATPneumatics']/Generics").text, "yes")

	def test_atpneumaticsSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATPneumatics']/Simulator"), ET.Element, msg="ATPneumaticsSimulator tag is NOT present")

	def test_atptgExists(self):
		self.assertIn("ATPtg", self.cscs)

	def test_atptgGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATPtg']/Generics").text, "yes")

	def test_atptgSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATPtg']/Simulator"), ET.Element, msg="ATPtgSimulator tag is NOT present")

	def test_atspectrographExists(self):
		self.assertIn("ATSpectrograph", self.cscs)

	def test_atspectrographGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATSpectrograph']/Generics").text, "yes")

	def test_atspectrographSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATSpectrograph']/Simulator"), ET.Element, msg="ATSpectrographSimulator tag is NOT present")

	def test_attcsExists(self):
		self.assertIn("ATTCS", self.cscs)

	def test_attcsGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATTCS']/Generics").text, "yes")

	def test_attcsSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATTCS']/Simulator"), ET.Element, msg="ATTCSSimulator tag is NOT present")

	def test_atwhitelightExists(self):
		self.assertIn("ATWhiteLight", self.cscs)

	def test_atwhitelightGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ATWhiteLight']/Generics").text, "yes")

	def test_atwhitelightSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ATWhiteLight']/Simulator"), ET.Element, msg="ATWhiteLightSimulator tag is NOT present")

	def test_cbpExists(self):
		self.assertIn("CBP", self.cscs)

	def test_cbpGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='CBP']/Generics").text, "yes")

	def test_cbpSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='CBP']/Simulator"), ET.Element, msg="CBPSimulator tag is NOT present")

	def test_catchuparchiverExists(self):
		self.assertIn("CatchupArchiver", self.cscs)

	def test_catchuparchiverGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='CatchupArchiver']/Generics").text, "yes")

	def test_catchuparchiverSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='CatchupArchiver']/Simulator"), ET.Element, msg="CatchupArchiverSimulator tag is NOT present")

	def test_dimmExists(self):
		self.assertIn("DIMM", self.cscs)

	def test_dimmGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='DIMM']/Generics").text, "yes")

	def test_dimmSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='DIMM']/Simulator"), ET.Element, msg="DIMMSimulator tag is NOT present")

	def test_dsmExists(self):
		self.assertIn("DSM", self.cscs)

	def test_dsmGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='DSM']/Generics").text, "yes")

	def test_dsmSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='DSM']/Simulator"), ET.Element, msg="DSMSimulator tag is NOT present")

	def test_domeExists(self):
		self.assertIn("Dome", self.cscs)

	def test_domeGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='Dome']/Generics").text, "yes")

	def test_domeSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='Dome']/Simulator"), ET.Element, msg="DomeSimulator tag is NOT present")

	def test_easExists(self):
		self.assertIn("EAS", self.cscs)

	def test_easGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='EAS']/Generics").text, "yes")

	def test_easSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='EAS']/Simulator"), ET.Element, msg="EASSimulator tag is NOT present")

	def test_efdExists(self):
		self.assertIn("EFD", self.cscs)

	def test_efdGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='EFD']/Generics").text, "yes")

	def test_efdSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='EFD']/Simulator"), ET.Element, msg="EFDSimulator tag is NOT present")

	def test_efdtransformationserverExists(self):
		self.assertIn("EFDTransformationServer", self.cscs)

	def test_efdtransformationserverGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='EFDTransformationServer']/Generics").text, "yes")

	def test_efdtransformationserverSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='EFDTransformationServer']/Simulator"), ET.Element, msg="EFDTransformationServerSimulator tag is NOT present")

	def test_electrometerExists(self):
		self.assertIn("Electrometer", self.cscs)

	def test_electrometerGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='Electrometer']/Generics").text, "yes")

	def test_electrometerSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='Electrometer']/Simulator"), ET.Element, msg="ElectrometerSimulator tag is NOT present")

	def test_environmentExists(self):
		self.assertIn("Environment", self.cscs)

	def test_environmentGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='Environment']/Generics").text, "yes")

	def test_environmentSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='Environment']/Simulator"), ET.Element, msg="EnvironmentSimulator tag is NOT present")

	def test_fiberspectrographExists(self):
		self.assertIn("FiberSpectrograph", self.cscs)

	def test_fiberspectrographGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='FiberSpectrograph']/Generics").text, "yes")

	def test_fiberspectrographSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='FiberSpectrograph']/Simulator"), ET.Element, msg="FiberSpectrographSimulator tag is NOT present")

	def test_genericcameraExists(self):
		self.assertIn("GenericCamera", self.cscs)

	def test_genericcameraGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='GenericCamera']/Generics").text, "yes")

	def test_genericcameraSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='GenericCamera']/Simulator"), ET.Element, msg="GenericCameraSimulator tag is NOT present")

	def test_hvacExists(self):
		self.assertIn("HVAC", self.cscs)

	def test_hvacGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='HVAC']/Generics").text, "yes")

	def test_hvacSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='HVAC']/Simulator"), ET.Element, msg="HVACSimulator tag is NOT present")

	def test_hexapodExists(self):
		self.assertIn("Hexapod", self.cscs)

	def test_hexapodGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='Hexapod']/Generics").text, "yes")

	def test_hexapodSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='Hexapod']/Simulator"), ET.Element, msg="HexapodSimulator tag is NOT present")

	def test_iotaExists(self):
		self.assertIn("IOTA", self.cscs)

	def test_iotaGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='IOTA']/Generics").text, "yes")

	def test_iotaSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='IOTA']/Simulator"), ET.Element, msg="IOTASimulator tag is NOT present")

	def test_loveExists(self):
		self.assertIn("LOVE", self.cscs)

	def test_loveGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='LOVE']/Generics").text, "no")

	def test_loveSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='LOVE']/Simulator"), ET.Element, msg="LOVESimulator tag is NOT present")

	def test_linearstageExists(self):
		self.assertIn("LinearStage", self.cscs)

	def test_linearstageGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='LinearStage']/Generics").text, "yes")

	def test_linearstageSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='LinearStage']/Simulator"), ET.Element, msg="LinearStageSimulator tag is NOT present")

	def test_mtaosExists(self):
		self.assertIn("MTAOS", self.cscs)

	def test_mtaosGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTAOS']/Generics").text, "yes")

	def test_mtaosSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTAOS']/Simulator"), ET.Element, msg="MTAOSSimulator tag is NOT present")

	def test_mtarchiverExists(self):
		self.assertIn("MTArchiver", self.cscs)

	def test_mtarchiverGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTArchiver']/Generics").text, "yes")

	def test_mtarchiverSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTArchiver']/Simulator"), ET.Element, msg="MTArchiverSimulator tag is NOT present")

	def test_mtcameraExists(self):
		self.assertIn("MTCamera", self.cscs)

	def test_mtcameraGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTCamera']/Generics").text, "yes")

	def test_mtcameraSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTCamera']/Simulator"), ET.Element, msg="MTCameraSimulator tag is NOT present")

	def test_mtdometrajectoryExists(self):
		self.assertIn("MTDomeTrajectory", self.cscs)

	def test_mtdometrajectoryGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTDomeTrajectory']/Generics").text, "yes")

	def test_mtdometrajectorySimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTDomeTrajectory']/Simulator"), ET.Element, msg="MTDomeTrajectorySimulator tag is NOT present")

	def test_mteecExists(self):
		self.assertIn("MTEEC", self.cscs)

	def test_mteecGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTEEC']/Generics").text, "yes")

	def test_mteecSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTEEC']/Simulator"), ET.Element, msg="MTEECSimulator tag is NOT present")

	def test_mtguiderExists(self):
		self.assertIn("MTGuider", self.cscs)

	def test_mtguiderGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTGuider']/Generics").text, "yes")

	def test_mtguiderSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTGuider']/Simulator"), ET.Element, msg="MTGuiderSimulator tag is NOT present")

	def test_mtheaderserviceExists(self):
		self.assertIn("MTHeaderService", self.cscs)

	def test_mtheaderserviceGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTHeaderService']/Generics").text, "yes")

	def test_mtheaderserviceSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTHeaderService']/Simulator"), ET.Element, msg="MTHeaderServiceSimulator tag is NOT present")

	def test_mtlasertrackerExists(self):
		self.assertIn("MTLaserTracker", self.cscs)

	def test_mtlasertrackerGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTLaserTracker']/Generics").text, "yes")

	def test_mtlasertrackerSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTLaserTracker']/Simulator"), ET.Element, msg="MTLaserTrackerSimulator tag is NOT present")

	def test_mtm1m3Exists(self):
		self.assertIn("MTM1M3", self.cscs)

	def test_mtm1m3Generics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTM1M3']/Generics").text, "yes")

	def test_mtm1m3Simulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTM1M3']/Simulator"), ET.Element, msg="MTM1M3Simulator tag is NOT present")

	def test_mtm1m3tsExists(self):
		self.assertIn("MTM1M3TS", self.cscs)

	def test_mtm1m3tsGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTM1M3TS']/Generics").text, "yes")

	def test_mtm1m3tsSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTM1M3TS']/Simulator"), ET.Element, msg="MTM1M3TSSimulator tag is NOT present")

	def test_mtm2Exists(self):
		self.assertIn("MTM2", self.cscs)

	def test_mtm2Generics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTM2']/Generics").text, "yes")

	def test_mtm2Simulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTM2']/Simulator"), ET.Element, msg="MTM2Simulator tag is NOT present")

	def test_mtmountExists(self):
		self.assertIn("MTMount", self.cscs)

	def test_mtmountGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTMount']/Generics").text, "yes")

	def test_mtmountSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTMount']/Simulator"), ET.Element, msg="MTMountSimulator tag is NOT present")

	def test_mtptgExists(self):
		self.assertIn("MTPtg", self.cscs)

	def test_mtptgGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTPtg']/Generics").text, "yes")

	def test_mtptgSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTPtg']/Simulator"), ET.Element, msg="MTPtgSimulator tag is NOT present")

	def test_mttcsExists(self):
		self.assertIn("MTTCS", self.cscs)

	def test_mttcsGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTTCS']/Generics").text, "yes")

	def test_mttcsSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTTCS']/Simulator"), ET.Element, msg="MTTCSSimulator tag is NOT present")

	def test_mtvmsExists(self):
		self.assertIn("MTVMS", self.cscs)

	def test_mtvmsGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='MTVMS']/Generics").text, "yes")

	def test_mtvmsSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='MTVMS']/Simulator"), ET.Element, msg="MTVMSSimulator tag is NOT present")

	def test_ocsExists(self):
		self.assertIn("OCS", self.cscs)

	def test_ocsGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='OCS']/Generics").text, "yes")

	def test_ocsSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='OCS']/Simulator"), ET.Element, msg="OCSSimulator tag is NOT present")

	def test_pointingcomponentExists(self):
		self.assertIn("PointingComponent", self.cscs)

	def test_pointingcomponentGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='PointingComponent']/Generics").text, "yes")

	def test_pointingcomponentSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='PointingComponent']/Simulator"), ET.Element, msg="PointingComponentSimulator tag is NOT present")

	def test_promptprocessingExists(self):
		self.assertIn("PromptProcessing", self.cscs)

	def test_promptprocessingGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='PromptProcessing']/Generics").text, "yes")

	def test_promptprocessingSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='PromptProcessing']/Simulator"), ET.Element, msg="PromptProcessingSimulator tag is NOT present")

	def test_rotatorExists(self):
		self.assertIn("Rotator", self.cscs)

	def test_rotatorGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='Rotator']/Generics").text, "yes")

	def test_rotatorSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='Rotator']/Simulator"), ET.Element, msg="RotatorSimulator tag is NOT present")

	def test_schedulerExists(self):
		self.assertIn("Scheduler", self.cscs)

	def test_schedulerGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='Scheduler']/Generics").text, "yes")

	def test_schedulerSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='Scheduler']/Simulator"), ET.Element, msg="SchedulerSimulator tag is NOT present")

	def test_scriptExists(self):
		self.assertIn("Script", self.cscs)

	def test_scriptGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='Script']/Generics").text, "no")

	def test_scriptSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='Script']/Simulator"), ET.Element, msg="ScriptSimulator tag is NOT present")

	def test_scriptqueueExists(self):
		self.assertIn("ScriptQueue", self.cscs)

	def test_scriptqueueGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='ScriptQueue']/Generics").text, "yes")

	def test_scriptqueueSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='ScriptQueue']/Simulator"), ET.Element, msg="ScriptQueueSimulator tag is NOT present")

	def test_summitfacilityExists(self):
		self.assertIn("SummitFacility", self.cscs)

	def test_summitfacilityGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='SummitFacility']/Generics").text, "yes")

	def test_summitfacilitySimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='SummitFacility']/Simulator"), ET.Element, msg="SummitFacilitySimulator tag is NOT present")

	def test_testExists(self):
		self.assertIn("Test", self.cscs)

	def test_testGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='Test']/Generics").text, "yes")

	def test_testSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='Test']/Simulator"), ET.Element, msg="TestSimulator tag is NOT present")

	def test_tunablelaserExists(self):
		self.assertIn("TunableLaser", self.cscs)

	def test_tunablelaserGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='TunableLaser']/Generics").text, "yes")

	def test_tunablelaserSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='TunableLaser']/Simulator"), ET.Element, msg="TunableLaserSimulator tag is NOT present")

	def test_watcherExists(self):
		self.assertIn("Watcher", self.cscs)

	def test_watcherGenerics(self):
		self.assertEqual(self.root.find("./Subsystem/[Name='Watcher']/Generics").text, "yes")

	def test_watcherSimulator(self):
		self.assertIsInstance(self.root.find("./Subsystem/[Name='Watcher']/Simulator"), ET.Element, msg="WatcherSimulator tag is NOT present")

if __name__ == "__main__":
	unittest.main(verbosity=2)
