#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib

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

"""Define the lists of IDL and MySQL Reserved Words"""

idl_reserved = [ 'ABSTRACT', 'ANY', 'ATTRIBUTE', 'BOOLEAN', 'CASE', 'CHAR', 'COMPONENT', 'CONST', \
				'CONSUMES', 'CONTEXT', 'CUSTOM', 'DEC', 'DEFAULT', 'DOUBLE', 'EMITS', 'ENUM' 'EVENTTYPE', \
				'EXCEPTION', 'EXIT', 'FACTORY', 'FALSE', 'FINDER', 'FIXED', 'FLOAT' 'GETRAISES', 'HOME', \
				'IMPORT', 'IN', 'INOUT', 'INTERFACE', 'LIMIT', 'LOCAL', 'LONG', 'MODULE', 'MULTIPLE', \
				'NATIVE', 'OBJECT', 'OCTET', 'ONEWAY', 'OUT', 'PRIMARYKEY', 'PRIVATE', 'PROVIDES', \
				'PUBLIC', 'PUBLISHES', 'RAISES', 'READONLY', 'SEQUENCE', 'SETRAISES', 'SHORT', 'STRING', \
				'STRUCT', 'SUPPORTS', 'SWITCH', 'TRUE', 'TRUNCATABLE', 'TYPEDEF', 'TYPEID', 'TYPEPREFIX', \
				'UNION', 'UNSIGNED', 'USES', 'VALUEBASE', 'VALUETYPE', 'VOID', 'WCHAR', 'WSTRING' ]

db_reserved = [ 'ACCESSIBLE', 'ADD', 'ALL', 'ALTER', 'ANALYZE', 'AND', 'AS', 'ASC', 'ASENSITIVE', \
				'BEFORE', 'BETWEEN', 'BIGINT', 'BINARY', 'BLOB', 'BOTH', 'BY', 'CALL', 'CASCADE', \
				'CASE', 'CATALOG_NAME', 'CHANGE', 'CHAR', 'CHARACTER', 'CHECK', 'COLLATE', 'COLUMN', \
				'CONDITION', 'CONSTRAINT', 'CONTINUE', 'CONVERT', 'CREATE', 'CROSS', 'CURRENT_DATE', \
				'CURRENT_TIME', 'CURRENT_TIMESTAMP', 'CURRENT_USER', 'CURSOR', 'DATABASE', 'DATABASES', \
				'DAY_HOUR', 'DAY_MICROSECOND', 'DAY_MINUTE', 'DAY_SECOND', 'DEC', 'DECIMAL', 'DECLARE', \
				'DEFAULT', 'DELAYED', 'DELAY_KEY_WRITE', 'DELETE', 'DESC', 'DESCRIBE', 'DETERMINISTIC', \
				'DISTINCT', 'DISTINCTROW', 'DIV', 'DOUBLE', 'DROP', 'DUAL', 'EACH', 'ELSE', 'ELSEIF', \
				'ENCLOSED', 'ESCAPED', 'EXISTS', 'EXIT', 'EXPLAIN', 'FALSE', 'FETCH', 'FLOAT', 'FLOAT4', \
				'FLOAT8', 'FOR', 'FORCE', 'FOREIGN', 'FROM', 'FULLTEXT', 'GENERATED',  'GET', 'GRANT', \
				'GROUP', 'HAVING', 'HIGH_PRIORITY', 'HOUR_MICROSECOND', 'HOUR_MINUTE', 'HOUR_SECOND', \
				'IF', 'IGNORE', 'IN', 'INDEX', 'INFILE', 'INITIAL_SIZE', 'INNER', 'INOUT', 'INSENSITIVE', \
				'INSERT', 'INSERT_METHOD', 'INT', 'INT1', 'INT2', 'INT3', 'INT4', 'INT8', 'INTEGER', \
				'INTERVAL', 'INTO', 'IO_AFTER_GTIDS', 'IO_BEFORE_GTIDS', 'IS', 'ITERATE', 'JOIN', 'KEY', \
				'KEYS', 'KEY_BLOCK_SIZE', 'KILL', 'LEADING', 'LEAVE', 'LEAVES', 'LEFT', 'LIKE', 'LIMIT', \
				'LINEAR', 'LINES', 'LOAD', 'LOCALTIME', 'LOCALTIMESTAMP', 'LOCK', 'LONG', 'LONGBLOB', \
				'LONGTEXT', 'LOOP', 'LOW_PRIORITY', 'MASTER_BIND', 'MASTER_SSL_VERIFY_SERVER_CERT', \
				'MATCH', 'MAXVALUE', 'MEDIUMBLOB', 'MEDIUMINT', 'MEDIUMTEXT', 'MIDDLEINT', \
				'MINUTE_MICROSECOND', 'MINUTE_SECOND', 'MOD', 'MODIFIES', 'NATURAL', 'NOT', \
				'NO_WRITE_TO_BINLOG', 'NULL', 'NUMERIC', 'ON', 'OPTIMIZE', 'OPTIMIZER_COSTS', 'OPTION', \
				'OPTIONALLY', 'OR', 'ORDER', 'OUT', 'OUTER', 'OUTFILE', 'PARTITION', 'PRECISION', \
				'PRIMARY', 'PROCEDURE', 'PURGE', 'RANGE', 'READ', 'READS', 'READ_WRITE', 'REAL', \
				'REFERENCES', 'REGEXP', 'RELEASE', 'RENAME', 'REPEAT', 'REPEATABLE', 'REPLACE', 'REQUIRE', \
				'RESIGNAL', 'RESTRICT', 'RETURN', 'REVOKE', 'RIGHT', 'RLIKE', 'SCHEMA', 'SCHEMAS', \
				'SECOND_MICROSECOND', 'SELECT', 'SENSITIVE', 'SEPARATOR', 'SET', 'SHOW', 'SIGNAL', \
				'SMALLINT', 'SPATIAL', 'SPECIFIC', 'SQL', 'SQLEXCEPTION', 'SQLSTATE', 'SQLWARNING', \
				'SQL_BIG_RESULT', 'SQL_CALC_FOUND_ROWS', 'SQL_SMALL_RESULT', 'SSL', 'STARTING', 'STORED', \
				'STRAIGHT_JOIN', 'TABLE', 'TERMINATED', 'THEN', 'TINYBLOB', 'TINYINT', 'TINYTEXT', 'TO', \
				'TRAILING', 'TRIGGER', 'TRUE', 'UNDO', 'UNION', 'UNIQUE', 'UNLOCK', 'UNSIGNED', 'UPDATE', \
				'USAGE', 'USE', 'USING', 'UTC_DATE', 'UTC_TIME', 'UTC_TIMESTAMP', 'VALUES', 'VARBINARY', \
				'VARCHAR', 'VARCHARACTER', 'VARYING', 'VIRTUAL',  'WHEN', 'WHERE', 'WHILE', 'WITH', \
				'WRITE', 'XOR', 'YEAR_MONTH', 'ZEROFILL' ]

# =========
# Functions
# =========

def get_xmlfile_csc_topic():
	pkgroot = pathlib.Path(__file__).resolve().parents[1]
	arguments = []
	for csc in subsystems:
		xml_path = pkgroot / "sal_interfaces" / csc
		for xmlfile in xml_path.glob(f"{csc}_*.xml"):
			topic = xmlfile.stem.split("_")[1]
			arguments.append((xmlfile,csc,topic))
	return arguments

