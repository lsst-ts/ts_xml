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

This must contain a brief description of the CSC.

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

Generics
========

**Data Type**: string or comma-delimited list of strings

This contains the listing of the supported generic events. Acceptable entries
are:

    * yes (this means ALL generics will be supported)
    * no (this mean NO generics will be supported)
    * comma delimited list of strings of generics supported by the CSC

The last variant names all of the generics explicitly that will be supported.
The example below is merely a demonstration of what needs to be done and is not
exhaustive. Whitespace is permitted after a comma.

*Example*: command_start, command_enable, command_disable,
logevent_summaryState, logevent_appliedSettingsMatchStart

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
    * LabView
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
