************************
SALSubsystems Attributes
************************

Below are the descriptions and content recommendations for SALSubsystems.xml
attributes.

Name
====

**Data Type**: string

This contains the name of the CSC as specified in the directory in 
`ts_xml/sal_interfaces`, in `ts_xml/python/lsst/ts/xml/testutils.py` and also in
the subsequently defined commands, events and telemetry.

Description
===========

**Data Type**: string

This **MUST** contain a brief description of the CSC.

IndexEnumeration
================

**Data Type**: comma-delimited list of names, key, value pairs or a string

This contains a listing of identifiers for indexed components. If the component
is not indexed the content "no" should be used. If the component has the
potential for a large number of non-zero indicies, the content should simply be
"any". For components with a few variants, the identifier may be specified via
names only: MT, AT or by key=value pairs (preferred): MT=1, AT=2. Spaces are
permitted after the comma. The value 0 must not be specified and SAL will
reject it because 0 has special meaning to SAL.

AddedGenerics
=============

**Data Type**: string or comma-delimited list of strings

This contains a list of generic topics or categories, excluding mandatory topics.
If a SAL component only uses mandatory topics then the AddedGenerics field should be empty.

The mandatory topics are:

  * logevent_heartbeat
  * logevent_logLevel
  * logevent_logMessage
  * logevent_softwareVersions

These topics *DO NOT* need to be listed in this attribute and are automatically provided to each CSC.

There are two categories supported by this attribute.
Each category has specific commands and events associated with it.
The categories are:

csc

  * command_setAuthList
  * command_disable
  * command_enable
  * command_exitControl
  * command_setLogLevel
  * command_standby
  * command_start
  * logevent_authList
  * logevent_errorCode
  * logevent_simulationMode
  * logevent_summaryState

configurable

  * logevent_appliedSettingsMatchStart
  * logevent_settingsApplied
  * logevent_settingVersions

The topics listed below must be defined separately.

  * command_abort (deprecated)
  * command_enterControl
  * logevent_largeFileObjectAvailable

For a configurable CSC:
*Example*: csc, log, configurable

For an OFFLINE-entry CSC:
*Example*: csc, command_enterControl

ActiveDevelopers
================

**Data Type**: (comma delimited list of) string(s)

This contains the name(s) of the developer(s) that is(are) responsible for
day-to-day code maintenance and feature enhancements.

Github
======

**Data Type**: string

This contains the URL for the Github code repository. If the repository is
privately held, the URL should be appended with a space and (private).

*Example*: https://github.com/lsst-ts/ts_cool_repo.git (private)

If the source code is not provided in a Github repository, the string should
represent a description of where the source code can be obtained.

.. note:: This reference should only be for code operating real systems.
          Simulators are handled in a separate entry.

JenkinsTestResults
==================

**Data Type**: string

This contains a URL that points to a Jenkins (or alternate CI system) job that
is responsible for running the CSC unit tests. If a CSC does not have an
associated Jenkins (or alternate CI system) job, the content should be
"Not Available".

*Example*: https://tssw-ci.lsst.org/view/Conda_Package/job/DSM%20conda%20package/

RubinObsContact
===============

**Data Type**: string

This contains the name of the Rubin Observatory person who can field questions
and provide information about the CSC.

CSCDocs
=======

**Data Type**: (comma delimited list of) URL(s)

This contains URLs to Docushare documents and/or collections, to technotes or
user guides describing the functionality and use of the CSC.

ProductOwner
============

**Data Type**: string

This contains the name of the product owner who is responsible for signing off
on the functional requirements, the quality, prioritization and acceptance of a
particular software product.

RelatedDocuments
================

**Data Type**: (comma delimited list of) string(s)

This contains Docushare document handles, URLs to technotes describing
supporting or ancillary information relating to the CSC. This could (not
exhaustive) include vendor contract information, design proposals and delivery
inspections and testing reports.

SoftwareLanguage
================

**Data Type**: string

This contains the name of the programming language in which the CSC code is
written. If more than one programming language is at work, a comma-delimited
list of strings must be used to capture all the languages used. This does not
cover the runtime library.

RuntimeLanguages
================

**Data Type**: (comma delimited list of) string(s)

This is the list of languages for which runtime support is required to
facilitate interaction with this CSC, i.e. Shared libraries and headers (SALPY,
C++, LabVIEW) or Jar archives for Java, or IDL for native dds Python (salobj)

Required Values (for EFD communication):

    * IDL

Additional Values (as needed):

    * CPP
    * LabVIEW
    * Java
    * SALPY

VendorContact
=============

**Data Type**: string

This contains the name of the person or organization outside the Rubin
Observatory project that is/was responsible for the original design,
implementation and delivery of the CSC code. Rubin Observatory project
personnel are NOT considered vendors and should not be listed here. If the code
was developed by the Rubin Observatory project the content should be
"Not Applicable".

Simulator
=========

**Data Type**: string

This contains the Github repository URL that contains the simulator code. If
the repository is privately held, the URL should be appended with a space and
(private). If the URL is the same repository as the main CSC code, this content
should be used: "Internal to CSC".  If the CSC does not require a simulator,
the content should be "Not Required". If the CSC could have a simulator but none
has been provided, the content should be "Not Provided". If the CSC has multiple
simulators, the content should be a comma-delimited list of content that
references each simulator. Whitespace after the commas is permitted.

Configuration
=============

**Data Type**: string

This contains the Github repository URL that contains the configuration
associated with the CSC. If the repository is privately held, the URL should be
appended with a space and (private). If a database is used, the content should
be "Database: URL" where the URL is a link to a document that covers the
location and access methodologies for the system. If a CSC is not configurable,
the content should be "Not Configurable".
