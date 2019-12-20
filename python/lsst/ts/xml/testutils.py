#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
import astropy.units

"""This library defines common variables and functions used by the various
XML test suite generator scripts.
"""

# =========
# Variables
# =========

"""Defines the array of Commandable SAL Components, or CSCs."""

subsystems = [
    'ATAOS', 'ATArchiver', 'ATBuilding', 'ATCamera', 'ATDome',
    'ATDomeTrajectory', 'ATHeaderService', 'ATHexapod', 'ATMCS',
    'ATMonochromator', 'ATPneumatics', 'ATPtg', 'ATSpectrograph', 'ATTCS',
    'ATWhiteLight', 'CCArchiver', 'CCCamera', 'CCHeaderService', 'CatchupArchiver',
    'CBP', 'DIMM', 'Dome',
    'DSM', 'EAS', 'EFD', 'EFDTransformationServer', 'Electrometer', 'Environment',
    'FiberSpectrograph', 'GenericCamera', 'IOTA', 'Hexapod', 'HVAC',
    'LinearStage', 'LOVE', 'MTAOS', 'MTArchiver', 'MTCamera',
    'MTDomeTrajectory', 'MTEEC', 'MTGuider', 'MTHeaderService',
    'MTLaserTracker', 'MTM1M3', 'MTM1M3TS', 'MTM2', 'MTMount', 'MTPtg', 'MTTCS',
    'MTVMS', 'PointingComponent', 'PromptProcessing', 'Rotator',
    'Scheduler', 'Script', 'ScriptQueue', 'SummitFacility', 'Test',
    'TunableLaser', 'Watcher',
]

"""Define the array of Generic Commands."""

generic_commands = [
    'abort', 'enable', 'disable', 'standby', 'exitControl', 'start',
    'enterControl', 'setLogLevel', 'setSimulationMode', 'setValue'
]

"""Define the array of Generic Events."""

generic_events = [
    'appliedSettingsMatchStart', 'errorCode', 'heartbeat', 'logLevel',
    'logMessage', 'settingVersions', 'simulationMode', 'softwareVersions',
    'summaryState'
]

"""Define the lists of IDL and MySQL Reserved Words"""

idl_reserved = [
    'ABSTRACT', 'ANY', 'ATTRIBUTE', 'BOOLEAN', 'CASE', 'CHAR', 'COMPONENT',
    'CONST', 'CONSUMES', 'CONTEXT', 'CUSTOM', 'DEC', 'DEFAULT', 'DOUBLE',
    'EMITS', 'ENUM' 'EVENTTYPE', 'EXCEPTION', 'EXIT', 'FACTORY', 'FALSE',
    'FINDER', 'FIXED', 'FLOAT' 'GETRAISES', 'HOME', 'IMPORT', 'IN', 'INOUT',
    'INTERFACE', 'LIMIT', 'LOCAL', 'LONG', 'MODULE', 'MULTIPLE', 'NATIVE',
    'OBJECT', 'OCTET', 'ONEWAY', 'OUT', 'PRIMARYKEY', 'PRIVATE', 'PROVIDES',
    'PUBLIC', 'PUBLISHES', 'RAISES', 'READONLY', 'SEQUENCE', 'SETRAISES',
    'SHORT', 'STRING', 'STRUCT', 'SUPPORTS', 'SWITCH', 'TRUE', 'TRUNCATABLE',
    'TYPEDEF', 'TYPEID', 'TYPEPREFIX', 'UNION', 'UNSIGNED', 'USES', 'VALUEBASE',
    'VALUETYPE', 'VOID', 'WCHAR', 'WSTRING'
]

db_critical_reserved = [
    "TIME"
]

db_optional_reserved = [
    "ALL", "ALTER", "ANALYZE", "ANY", "AS", "ASC", "BEGIN", "BY", "CREATE",
    "CONTINUOUS", "DATABASE", "DATABASES", "DEFAULT", "DELETE", "DESC",
    "DESTINATIONS", "DIAGNOSTICS", "DISTINCT", "DROP", "DURATION", "END",
    "EVERY", "EXPLAIN", "FIELD", "FOR", "FROM", "GRANT", "GRANTS", "GROUP",
    "GROUPS", "IN", "INF", "INSERT", "INTO", "KEY", "KEYS", "KILL", "LIMIT",
    "SHOW", "MEASUREMENT", "MEASUREMENTS", "NAME", "OFFSET", "ON", "ORDER",
    "PASSWORD", "POLICY", "POLICIES", "PRIVILEGES", "QUERIES", "QUERY", "READ",
    "REPLICATION", "RESAMPLE", "RETENTION", "REVOKE", "SELECT", "SERIES", "SET",
    "SHARD", "SHARDS", "SLIMIT", "SOFFSET", "STATS", "SUBSCRIPTION",
    "SUBSCRIPTIONS", "TAG", "TO", "USER", "USERS", "VALUES", "WHERE",
    "WITH", "WRITE"
]

# =========
# Functions
# =========


def get_pkg_root():
    """Return the root directory of this package."""
    return pathlib.Path(__file__).resolve().parents[4]


def get_sal_interfaces_dir():
    """Return the path to the ``sal_interfaces`` dir within this package."""
    return get_pkg_root() / "sal_interfaces"


def get_xmlfile_csc_topic():
    """Return the XML file for each CSC and each topic"""
    pkgroot = get_pkg_root()
    arguments = []
    for csc in subsystems:
        xml_path = pkgroot / "sal_interfaces" / csc
        for xmlfile in xml_path.glob(f"{csc}_*.xml"):
            topic = xmlfile.stem.split("_")[1]
            arguments.append((xmlfile, csc, topic))
    return arguments


def check_unit(unit_str):
    if not unit_str.isnumeric():
        try:
            return astropy.units.Quantity(1, unit_str)
        except ValueError:
            raise ValueError(unit_str + " is not a valid unit.")
        except Exception:
            raise Exception("UnknownError: " + unit_str)
    else:
        raise TypeError("Units cannot be numbers: " + unit_str)
