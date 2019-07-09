***********************************
SAL Constraints and Recommendations
***********************************

.. important::
    When updating(not typos) a policy in this document.
    Please add a description to the :ref:`sal_constraints_and_recommendations:Changes` section.

Changes
=======

* New policy added :ref:`sal_constraints_and_recommendations:SAL Topic and Parameter <Description> and <Unit> fields`. *June 19th, 2019*

The XML SAL object definitions have the following constraints:

Definitions
===========

CSC
    Commandable SAL Component

Naming Convention
=================

Types (name of CSC): UpperCamelCase
    Handling abbreviations and acronyms: Capitalize all letters of an abbreviation or acronym: Hence ATAOS, MTM1M3.
        For TCS components, use prefix AT for AuxiliaryTelescope and MT for MainTelescope CSCs.
Methods/Topics: lowerCamelCase (note that these names are constructed of 2/3 parts


1. CSC
2. Optional
3. Topic separated by underscores e.g Hexapod_command_someInterestingThing)

attributes: lowerCamelCase

Enumerations:
    Type name: UpperCamelCase (also known as PascalCase).
        Also, recommend use of "Selector" at the end of the type name when creating *new* Enumeration types.
    Literals: Also UpperCamelCase


.. note::
    Already established CSCs will NOT need to update their names; they are grandfathered in.
    This naming convention applies to all CSCs created *June 1, 2018* and forward.

Reserved words
==============

The following list of words are reserved either by IDL or SQL parsing and may not be used as *<EFDB_Name>*'s in SAL topic definitions.

- ABSTRACT
- ACCESSIBLE
- ADD
- ALL
- ALTER
- ANALYZE
- AND 
- ANY 
- AS 
- ASC 
- ASENSITIVE
- ATTRIBUTE 
- BEFORE
- BETWEEN 
- BIGINT
- BINARY
- BLOB
- BOOLEAN
- BOTH
- BY 
- CALL 
- CASCADE 
- CASE 
- CATALOG_NAME
- CHANGE 
- CHAR 
- CHARACTER
- CHECK
- COLLATE 
- COLUMN 
- COMPONENT 
- CONDITION 
- CONST 
- CONSTRAINT 
- CONSUMES
- CONTEXT 
- CONTINUE 
- CONVERT 
- CREATE
- CROSS 
- CURRENT_DATE
- CURRENT_TIME
- CURRENT_TIMESTAMP
- CURRENT_USER
- CURSOR
- CUSTOM
- DATABASE
- DATABASES
- DAY_HOUR
- DAY_MICROSECOND
- DAY_MINUTE
- DAY_SECOND
- DEC
- DECIMAL
- DECLARE
- DEFA
- DEFAULT
- DELAYED
- DELAY_KEY_WRITE
- DELETE 
- DESC 
- DESCRIBE 
- DETERMINISTIC 
- DISTINCT
- DISTINCTROW
- DIV
- DOUBLE
- DROP
- DUAL
- EACH
- ELSE
- ELSEIF 
- EMITS 
- ENCLOSED 
- ENUM 
- ESCAPED 
- EVENTTYPE 
- EXCEPTION 
- EXISTS
- EXIT 
- EXPLAIN
- FACTORY
- FALSE
- FETCH
- FINDER
- FIXED 
- FLOAT 
- FLOAT4
- FLOAT8 
- FOR 
- FORCE
- FOREIGN 
- FROM 
- FULLTEXT
- GENERATED 
- GET
- GETRAISES 
- GRANT 
- GROUP 
- HAVING 
- HIGH_PRIORITY
- HOME 
- HOUR_MICROSECOND
- HOUR_MINUTE
- HOUR_SECOND 
- I 
- IF 
- IGNORE 
- IMPORT
- IN 
- INDEX
- INFILE 
- INITIAL_SIZE 
- INNER
- INOUT
- INSENSITIVE 
- INSERT 
- INSERT_METHOD
- INT 
- INT1
- INT2
- INT3 
- INT4
- INT8
- INTEGER
- INTERFACE
- INTERVAL
- INTO
- IO_AFTER_GTIDS
- IO_BEFORE_GTIDS
- IS 
- ITERATE
- JOIN
- KEY 
- KEYS 
- KEY_BLOCK_SIZE
- KILL
- LEADING
- LEAVE 
- LEAVES 
- LEFT 
- LIKE 
- LIMIT 
- LINEAR 
- LINES 
- LOAD 
- LOCAL 
- LOCALTIME 
- LOCALTIMESTAMP 
- LOCK 
- LONG 
- LONGBLOB
- LONGTEXT
- LOOP
- LOW_PRIORITY
- MASTER_BIND
- MASTER_SSL_VERIFY_SERVER_CERT
- MATCH
- MAXVALUE
- MEDIUMBLOB
- MEDIUMINT 
- MEDIUMTEXT 
- MIDDLEINT
- MINUTE_MICROSECOND
- MINUTE_SECOND 
- MOD 
- MODIFIES 
- MODULE 
- MULTIPLE 
- NATIVE 
- NATURAL 
- NOT 
- NOUT 
- NO_WRITE_TO_BINLOG
- NULL 
- NUMERIC 
- OBJECT 
- OCTET 
- ON 
- ONEWAY 
- OPTIMIZE 
- OPTIMZER_COSTS 
- OPTION 
- OPTIONALLY
- OR 
- ORDER 
- OUT 
- OUTER 
- OUTFILE 
- PARTITION
- PRECISION
- PRIMARY
- PRIMARYKEY 
- PRIVATE
- PROCEDURE 
- PROVIDES 
- PUBLIC 
- PUBLISHES 
- PURGE 
- RAISES 
- RANGE 
- READ 
- READONLY 
- READS 
- READ_WRITE
- REAL 
- REFERENCES 
- REGEXP 
- RELEASE
- RENAME 
- REPEAT 
- REPEATABLE 
- REPLACE 
- REQUIRE 
- RESIGNAL 
- RESTRICT 
- RETURN 
- REVOKE 
- RIGHT 
- RLIKE
- SCHEMA 
- SCHEMAS
- SECOND_MICROSECOND 
- SELECT 
- SENSITIVE 
- SEPARATOR 
- SEQUENCE 
- SET 
- SETRAISES 
- SHORT 
- SHOW 
- SIGNAL 
- SMALLINT 
- SPATIAL
- SPECIFIC
- SQL 
- SQLEXCEPTION
- SQLSTATE 
- SQL_BIG_RESULT 
- SQL_CALC_FOUND_ROWS
- SQL_SMALL_RESULT 
- SSL 
- STARTING 
- STORED 
- STRAIGHT_JOIN
- STRING 
- STRUCT 
- SUPPORTS 
- SWITCH 
- TABLE 
- TERMINATED 
- THEN
- TINYBLOB
- TINYINT
- TINYTEXT
- TO 
- TRAILING 
- TRIGGER
- TRUE 
- TRUNCATABLE 
- TYPEDEF
- TYPEID
- TYPEPREFIX
- ULT
- UNDO 
- UNION
- UNIQUE 
- UNLOCK 
- UNSIGNED 
- UPDATE 
- USAGE 
- USE 
- USES 
- USING
- UTC_DATE 
- UTC_TIME 
- UTC_TIMESTAMP
- VALUEBASE
- VALUES 
- VALUETYPE
- VARBINARY
- VARCHAR 
- VARCHARACTER
- VARYING 
- VIRTUAL
- VOID 
- WCHAR 
- WHEN 
- WHERE
- WHILE
- WITH
- WRITE
- WSTRING
- XOR
- YEAR_MONTH
- ZEROFILL

Format of *<EFDB_Name>* names: These should not have any embedded no alphanumeric characters or spaces, use _ as a delimiter if required (do not use +-.,:# etc)
    e.g. *myImportant_data_x* is allowed
        myImportant-data.x is NOT allowed

Format of *<EFDB_Topic>* names: These should not have any embedded non alphanumeric characters or spaces, use _ as a delimiter if required (do not use +-.,:# etc)

The first part of the name must be the subsystem involved, separated by a _ delimiter from the rest of the name.
    e.g. *MyImportantSubsystem_device1* is allowed
        MyImportant_Subsystem.device1 is NOT allowed

Format of <Subsystem> names: These should not have any embedded non alphanumeric characters or spaces (only a-z, A-Z, 0-9)
    e.g. *ATHexaderService* is allowed
        AT_Header_Service is NOT allowed

Subsystem names (CSC aka Commandable SAL Component) must be listed in *SALSubsystems.xml* in *ts_xml* (at one time they needed to added to a file in *ts_sal* but that is no longer the case.).

The *<Subsystem>* and *<Alias>* tags for command's and logevent's must be consistent with the *<EFDB_Name>*
    e.g.
        *<Subsystem>MyBut</Subsystem>*
        <Alias>myCommand</Alias>
        <EFDB_Topic>MyBit_command_myCommand</EFDB_Topic>

ALL names must be less than 64 characters in length.

Timestamps
==========

If a time-of-data is to be associated with an item it should be named
    * *timestamp* - for a single time applying to all data in a topic
    * *timestampName1, timestampName2* etc - for specific times associated with more than one item in the topic
    * *timestamp[n]* - for an array of times associated with the array item(s) in a topic
    * *timestampName1[n], timestampName2[m]* - for multiple arrays of different times for different array sizes

The time(s) should be obtained using the SAL getCurrentTime() method, which returns a double precision value of TAI time with a resolution of at least 0.001 seconds.

Ignored Attributes in Topics
============================

Many generic commands have an ignored attribute.
This is due to a requirement from the API to not have empty topics.
If you are adding a command to your CSC that does not require an attribute, it still must contain a "dummy" one.
In order to maintain consistency across this use case, the attribute must be called *value*, be of type *boolean*, be given the following description: "Attribute required by the API, but is unused." and have the following units: *unitless*.

Generic Commands and Events
===========================

The standard set of commands and events are included in the `MagicDraw/EA UML SAL Template <https://confluence.lsstcorp.org/display/LTS/Create+SAL+XML+interfaces+from+UML>`_,

Each new CSC should use this template as a starting point.

State Enumeration
=================

The following state transition enumerations are globally defined:

* DisabledState = 1
* EnabledState = 2
* FaultState = 3
* OfflineState = 4
* StandbyState = 5

and are generated automatically by SAL and accessible via the language-specific library.

**What this means:** You do **NOT** need to generate a SummaryState enumeration in your Events xml file.
You **ONLY** need to generate a DetailState enumeration in your Event xml file IF you are adding new states to your detail states.
If you add new detail states to the DetailState enumeration, **YOU MUST** keep the original detail states in the enumeration.
If this is not clear, please ask `@ Dave Mills <https://confluence.lsstcorp.org/display/~dmills>`_ `@Rob Bovill <https://confluence.lsstcorp.org/display/~rbovill>`_ or `@Andy Clements <https://confluence.lsstcorp.org/display/~aclements>`_

After the salgenerator creates the code, you will have the following constants:
    e.g. 
        SAL__STATE_DISABLED (C++, Java, and Python)
        SummaryState.ctl & DetailState.ctl (LabVIEW)

Custom Enumerations
===================

Enumerations may also be declared on a per CSC basis, and will appear in the namespace of that CSC

e.g. for ATTCS in C++:
    ATTCS_shared_SimpleSetA (declared globally)
    ATTCS_someEvent_SpecificSetA (datum specific)

Current SAL object tables
=========================

Can be found at http://project.lsst.org/ts/sal_objects

Generic commands
================

The following command set is defined for all CSC's (although it is not mandatory to implement them all)

.. note::
    The spelling must be exact as it is used for code generation
    
    *start, stop, enable, disable, standby, enterControl, exitControl, abort, setValue*

Generic events
==============

The following event set is defined for all CSC's 

.. note::
    The spelling must be exact as it is used for code generation
    
    *appliedSettingsMatchStart, errorCode, settingVersions, summaryState*

Standard Events
===============

A LargeFileAnnouncement event consist off the following items:

* long byteSize - size of file in bytes 
* string checkSum - md5 checksum of file contents
* string generator - Name of generating application
* string mimeType - Mime type of file
* string url - cURL compatible URL used to reference the file
* float version - x.y version of file Format
* string<32> id - Extra identifying information about format/application

SAL Topic sizes
===============

In the rare case that absolute maximum performance and minimum latency are required, then the size of the SAL topic payload could be limited to
    1500 (mtu) - 240 (RTPS/DDS overhead) - 52 (SAL overhead) = 1208 bytes

This would ensure that every DDS message for that topic would fit in a single layer 3 ethernet package.

THIS IS NOT CURRENTLY NECESSARY FOR ANY OF LSST'S APPLICATIONS

The maximum SAL topic size is limited by the fact that each topic instance is also stored in an SQL database which limits both the size-in-bytes and column-count overhead used per row.

In practice both the length of the field name and the data format (int, double etc) affect this.
    e.g. Using 32 character names and double floating data items there would be an ~800 item limit
        Using 16 character names and double floating data items the limit is ~950.

.. note::
    Arrays in topics are stored as one element per column in the database for efficiency of data access over the network.
    
    e.g. *myDataArrayWithVeryLongName[800]* would be close to the limit.

To check if the XML for a CSC is compliant, use the following commands

.. code::
    
    salgenerator MySubsystem validate
    salgenerator MySubsystem html
    cat sql/MySubsystem*.sqldef > testingest.sql

if you have access to a local EFD instance, then

.. code::
    
    mysql EFD < testingests.sql

will report any errors.

Alternatively, upload the *testingest.sql* using the TBD webpage.

`Proposed method of recording subsystem "Settings" data <https://confluence.lsstcorp.org/pages/viewpage.action?pageId=58949768>`_

SAL Topic and Parameter <Description> and <Unit> fields
=======================================================

Changes
-------

* Added error notice about check_unit issue *July 9th, 2019*
* Policy added *June 19th, 2019*

Policy
------

* XML will have the <Units> and <Description> fields defined for each parameter in a topic

    * Dimensionless parameters (e.g. IP Address, Humidity, any string-type, etc) will use **unitless** as the <Units> field value.

* Units will be SI
* We will use astropy names for the names of the units in the topics
* We will use astropy unit format - when possible, going forward
* We will use astropy unit format - when possible, going forward
* For Complex units - they must be able to be parsed by astropy

There is a table in the EFD where the topic/parameter and units are paired up - this will be generated from the XML (via salgenerator)

It will not be possible to enforce the same units for each CSC (i.e. the cryostat uses Kelvins, EAS using celsius) - we will "try" to make them the same

For a list of the astropy's SI, please go here: http://docs.astropy.org/en/stable/units/index.html#module-astropy.units.si

Astrophysics units: http://docs.astropy.org/en/stable/units/index.html#module-astropy.units.astrophys

Many units may be used with prefixes, which are documented here:
http://docs.astropy.org/en/stable/units/standard_units.html#prefixes

An easy way to tell if a particular unit is valid is to try to make an astropy.units.Quantity:

.. code::
    
    import astropy.units

    def check_unit(unit_str):
        astropy.units.Quantity(f"1 {unit_str}")

    check_unit("deg") # OK
    check_unit("not_a_unit") # raises ValueError

.. error::
    There appears to be a problem with unit checking such that one can have a unit "deg22" pass the check without actually being a unit.
    Please be vigilant about this discrepancy.

SAL Interface Template
======================

Currently there's a template that includes all generic events and command, current design is in the repository: https://stash.lsstcorp.org/projects/TS/repos/ts_xml/browse/scripts/SAL_Interface_TemplateMD.mdzip

Commands:

.. image:: /images/command_uml.png 

Events:

.. image:: /images/event_uml.png

Datatype and Enumerations:

.. image:: /images/data_type_and_enumeration_uml.png 
