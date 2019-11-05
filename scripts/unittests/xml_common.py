#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os

"""This library defines common variables and functions used by the various XML test suite generator scripts.""" 

# =========
# Variables
# =========
"""Defines the array of Commandable SAL Components, or CSCs."""

subsystems = [	'ATAOS', 'ATArchiver', 'ATBuilding', 'ATCamera', 'ATDome', 'ATDomeTrajectory', 'ATHeaderService', 
				'ATHexapod', 'ATMCS', 'ATMonochromator', 'ATPneumatics', 'ATPtg', 'ATSpectrograph', 'ATTCS', 'ATWhiteLight', 
				'CatchupArchiver', 'CBP', 'DIMM', 'Dome', 'DSM', 'EAS', 'EFD', 'EFDTransformationServer', 'Electrometer', 'Environment', 
				'FiberSpectrograph', 'GenericCamera', 'IOTA', 'Hexapod', 'HVAC', 'LinearStage', 'LOVE',
				'MTAOS', 'MTArchiver', 'MTCamera', 'MTDomeTrajectory', 'MTEEC', 'MTGuider', 
				'MTHeaderService', 'MTLaserTracker', 'MTM1M3', 'MTM1M3TS', 'MTM2', 'MTMount', 'MTPtg', 'MTTCS', 'MTVMS', 
				'OCS', 'PointingComponent', 'PromptProcessing', 'Rotator', 'Scheduler',
				'Script', 'ScriptQueue', 'SummitFacility', 'Test', 'TunableLaser', 'Watcher' ]

"""Define the array of Generic Commands."""

generic_commands = [ 'abort', 'enable', 'disable', 'standby', 'exitControl', 'start', 'enterControl', 'setLogLevel', 'setSimulationMode', 'setValue' ]

"""Define the array of Generic Events."""

generic_events = [ 'appliedSettingsMatchStart', 'errorCode', 'heartbeat', 'logLevel', 'logMessage', 'settingVersions', 'simulationMode', 'softwareVersions', 'summaryState' ]

# =========
# Functions
# =========

def CapitalizeSubsystem( subsystem ):
	"""Certain CSCs used to be capitalized in non-standard ways. This function is holdover and should be removed."""
	return subsystem

def GetSubsystemVersion( string ):
	# Right now, the topic version is controlled manually, which requries a 
	# manual configuration file.  If/when this is formallized, switch to
	# that source.
	"""Get the version of the CSC topic (command, event or telemetry)."""
	version = ""
	with open(os.environ['HOME'] + "/bin/XML_Versions.txt") as versionfile:
		for line in versionfile:
			if string in line:
				line = versionfile.next()
				while line != "\n":
					version+=line.split(" ")[1].rstrip() + "\\n"
					line = versionfile.next()   #.split(" ")[1].rstrip()
	return version[:-2]


