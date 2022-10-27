# This file is part of ts_xml
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
import pathlib
import astropy.units

"""This library defines common variables and functions used by the various
XML test suite generator scripts.
"""

# =========
# Variables
# =========

"""Defines the list of Commandable SAL Components, or CSCs."""

subsystems = [
    "ATAOS",
    "MTAirCompressor",
    "ATArchiver",
    "ATBuilding",
    "ATCamera",
    "ATDome",
    "ATDomeTrajectory",
    "ATHeaderService",
    "ATHexapod",
    "ATMCS",
    "ATMonochromator",
    "ATOODS",
    "ATPneumatics",
    "ATPtg",
    "ATSpectrograph",
    "ATWhiteLight",
    "Authorize",
    "GCHeaderService",
    "CCArchiver",
    "CCCamera",
    "CCHeaderService",
    "CCOODS",
    "CatchupArchiver",
    "CBP",
    "DIMM",
    "DREAM",
    "DSM",
    "EAS",
    "Electrometer",
    "ESS",
    "FiberSpectrograph",
    "GenericCamera",
    "GIS",
    "Guider",
    "IOTA",
    "HVAC",
    "LinearStage",
    "LOVE",
    "MTAOS",
    "MTAlignment",
    "MTCamera",
    "MTDome",
    "MTDomeTrajectory",
    "MTEEC",
    "MTHeaderService",
    "MTHexapod",
    "MTM1M3",
    "MTM1M3TS",
    "MTM2",
    "MTMount",
    "MTPtg",
    "MTRotator",
    "MTVMS",
    "OCPS",
    "PMD",
    "Scheduler",
    "Script",
    "ScriptQueue",
    "SummitFacility",
    "Test",
    "TunableLaser",
    "Watcher",
    "WeatherStation",
    "WeatherForecast",
]

"""Define the list of Generic Commands."""

generic_commands = [
    "abort",
    "enable",
    "disable",
    "standby",
    "exitControl",
    "start",
    "enterControl",
    "setLogLevel",
    "setAuthList",
]

"""Define the list of Generic Events."""

generic_events = [
    "authList",
    "configurationApplied",
    "configurationsAvailable",
    "errorCode",
    "heartbeat",
    "logLevel",
    "logMessage",
    "simulationMode",
    "softwareVersions",
    "statusCode",
    "summaryState",
    "authList",
    "largeFileObjectAvailable",
]

generic_topics = set(
    [f"command_{val}" for val in generic_commands]
    + [f"logevent_{val}" for val in generic_events]
)

"""Define the list of AddedGenerics categories."""

added_generics_categories = ["configurable", "csc"]

"""Define the list of AddedGenerics commands that are not mandatory."""

added_generics_commands = ["abort", "enterControl"]

"""Define the list of AddedGenerics events that are not mandatory."""

added_generics_events = ["largeFileObjectAvailable", "statusCode"]

"""Define the list of AddedGenerics mandatory commands."""

added_generics_mandatory_commands = []

"""Define the list of AddedGenerics mandatory events."""

added_generics_mandatory_events = [
    "heartbeat",
    "logLevel",
    "logMessage",
    "softwareVersions",
]

"""Define the full set of mandatory topics not needed in AddedGenerics."""

added_generics_mandatory_topics = set(
    [f"command_{val}" for val in added_generics_mandatory_commands]
    + [f"logevent_{val}" for val in added_generics_mandatory_events]
)

"""Define list of commands for csc category."""

added_generics_csc_commands = [
    "disable",
    "enable",
    "exitControl",
    "setAuthList",
    "setLogLevel",
    "standby",
    "start",
]

"""Define list of events for csc category."""

added_generics_csc_events = [
    "authList",
    "errorCode",
    "simulationMode",
    "summaryState",
]

"""Define list of commands for configurable category."""

added_generics_configurable_commands = []

"""Define list of events for configurable category."""

added_generics_configurable_events = [
    "configurationApplied",
    "configurationsAvailable",
]

"""Define the full set of approved AddedGenerics items."""

added_generics_items = set(
    added_generics_categories
    + [f"command_{val}" for val in added_generics_commands]
    + [f"logevent_{val}" for val in added_generics_events]
    + [f"command_{val}" for val in added_generics_csc_commands]
    + [f"logevent_{val}" for val in added_generics_csc_events]
    + [f"command_{val}" for val in added_generics_configurable_commands]
    + [f"logevent_{val}" for val in added_generics_configurable_events]
)

"""Define the lists of IDL and MySQL Reserved Words"""

idl_reserved = [
    "ABSTRACT",
    "ANY",
    "ATTRIBUTE",
    "BOOLEAN",
    "CASE",
    "CHAR",
    "COMPONENT",
    "CONST",
    "CONSUMES",
    "CONTEXT",
    "CUSTOM",
    "DEC",
    "DEFAULT",
    "DOUBLE",
    "EMITS",
    "ENUM",
    "EVENTTYPE",
    "EXCEPTION",
    "EXIT",
    "FACTORY",
    "FALSE",
    "FINDER",
    "FIXED",
    "FLOAT",
    "GETRAISES",
    "HOME",
    "IMPORT",
    "IN",
    "INOUT",
    "INTERFACE",
    "LIMIT",
    "LOCAL",
    "LONG",
    "MODULE",
    "MULTIPLE",
    "NATIVE",
    "OBJECT",
    "OCTET",
    "ONEWAY",
    "OUT",
    "PRIMARYKEY",
    "PRIVATE",
    "PROVIDES",
    "PUBLIC",
    "PUBLISHES",
    "RAISES",
    "READONLY",
    "SEQUENCE",
    "SETRAISES",
    "SHORT",
    "STRING",
    "STRUCT",
    "SUPPORTS",
    "SWITCH",
    "TRUE",
    "TRUNCATABLE",
    "TYPEDEF",
    "TYPEID",
    "TYPEPREFIX",
    "UNION",
    "UNSIGNED",
    "USES",
    "VALUEBASE",
    "VALUETYPE",
    "VOID",
    "WCHAR",
    "WSTRING",
]

"""Define the list of IDL Types"""
idl_types = [
    "boolean",
    "byte",
    "octet",
    "short",
    "int",
    "long",
    "long long",
    "unsigned short",
    "unsigned int",
    "unsigned long",
    "unsigned long long",
    "float",
    "double",
    "string",
    "char",
]

db_critical_reserved = ["TIME"]

db_optional_reserved = [
    "ALL",
    "ALTER",
    "ANALYZE",
    "ANY",
    "AS",
    "ASC",
    "BEGIN",
    "BY",
    "CREATE",
    "CONTINUOUS",
    "DATABASE",
    "DATABASES",
    "DEFAULT",
    "DELETE",
    "DESC",
    "DESTINATIONS",
    "DIAGNOSTICS",
    "DISTINCT",
    "DROP",
    "DURATION",
    "END",
    "EVERY",
    "EXPLAIN",
    "FIELD",
    "FOR",
    "FROM",
    "GRANT",
    "GRANTS",
    "GROUP",
    "GROUPS",
    "IN",
    "INF",
    "INSERT",
    "INTO",
    "KEY",
    "KEYS",
    "KILL",
    "LIMIT",
    "SHOW",
    "MEASUREMENT",
    "MEASUREMENTS",
    "NAME",
    "OFFSET",
    "ON",
    "ORDER",
    "PASSWORD",
    "POLICY",
    "POLICIES",
    "PRIVILEGES",
    "QUERIES",
    "QUERY",
    "READ",
    "REPLICATION",
    "RESAMPLE",
    "RETENTION",
    "REVOKE",
    "SELECT",
    "SERIES",
    "SET",
    "SHARD",
    "SHARDS",
    "SLIMIT",
    "SOFFSET",
    "STATS",
    "SUBSCRIPTION",
    "SUBSCRIPTIONS",
    "TAG",
    "TO",
    "USER",
    "USERS",
    "VALUES",
    "WHERE",
    "WITH",
    "WRITE",
]

# Field names used by SAL, and so forbidden in ts_xml
sal_reserved = [
    "SALINDEX",
]

"""Define string attributes that are NOT unitless"""
strings_with_units = [
    "azPositions",
    "elPositions",
    "rotPositions",
    "localTimeString",
    "raString",
    "decString",
]

# =========
# Functions
# =========


def get_pkg_root():
    """Return the root directory of this package."""
    return pathlib.Path(__file__).resolve().parent / "data"


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
    if unit_str.isnumeric():
        raise TypeError(f"Units={unit_str!r} cannot be a number")

    try:
        return astropy.units.Quantity(1, unit_str)
    except ValueError:
        raise ValueError(f"Units={unit_str!r} is not a valid unit.")
    except Exception as e:
        raise Exception(f"Units={unit_str!r} error: {e!r}.")
