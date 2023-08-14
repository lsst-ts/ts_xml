# LSST Interface Definitions

## Glossary

- CSC  -   Commandable SAL Component
- DDS  -   Data Distribution Services
- LSST -   Large Synoptic Survey Telescope
- SAL  -   Service Abstraction Layer
- TSSW -   LSST Telescope & Site Software
- XML  -   eXtensible Markup Language

## Description

This repository contains all the interface definition files for all the CSCs of the LSST.  All of the CSCs communicate using the DDS protocol.  TSSW provides a wrapper utility around DDS, called the Service Abstraction Layer or SAL.

* (https://github.com/lsst-ts/ts_sal) 

The SAL produces libraries in C++, LabVIEW, Java, PyDDS, and Python, for each CSC.  These libraries are then used by all the CSCs that need to publish or subscribe to any message topic.

### Installation and Usage

This repo is primarily a single location for all the definition files.  This repo in conjuction with the SAL are used to produce the code libraries.  Please refer to the documentation in the ts_sal project for instructions on manually producing those libraries.

### Build Documentation

To build the documentation::

    cd doc
    make
    package-docs clean
    package-docs build

### Testing

To ensure the successful build of your libraries, there are unit tests contained in the tests/ directory.  To run them, first setup the test environment

```
pip install -r test_requirements.txt -e .
```

This will install the pytest, pytest-flake8 and astropy modules used to verify the XML files are correct.  Then execute:

```
pytest -ra
```

from anywhere in the repository.  This will run the tests and print out a short summary of the results, including tests that are skipped for known reasons.  The messages associated with the skipped tests include Jira ticket numbers to track the issues.  Please navigate to 

* [LSST Jira](https://jira.lsstcorp.org/secure/Dashboard.jspa)

to find the specific ticket.

### XML formatting, XML linting

xmllint (http://xmlsoft.org) is used in GitHub action to check committed files format. Two spaces ("  ") are used for indentation (xmllint default). The files can be reformatted running xmllint --format, such as:

```bash
for f in $(find python/lsst/ts/xml/data -name "*.xml"); do xmllint --format $f > /tmp/$$lint; cp /tmp/$$lint $f; done && rm /tmp/$$lint
```

Xmllint is usually part of the libxml2 package, so to install it on Mac, do:

```bash
brew install libxml2
```

Linting is enforced on GitHub through github action (.github/workflows/xml-format.yaml). If you have xmllint installed locally, you can copy .githooks/pre-commit to .git/hooks/pre-commit to have XML formating checked before every commit.

#### Test Utilities

The testutils.py file, located in python/lsst/ts/xml, contains functions and variables used throughout the testing.  The lists of generic Commands and Events, as well as Reserved Words, imposed by third party tools, are all defined in testutils.py.  Most importantly, the independent list of expected CSCs is also defined here.  If these lists change, the corresponding list in testutils.py **must** also be updated, for example, if a CSC is added, removed or renamed, the tests will produce the following error:

```
AssertionError: There is an unexpected number of CSCs.
```

In case this error occurs, the subsystems list in testutils.py should be updated accordingly.

### Add, Rename or Delete a CSC

Adding, renaming or deleting a CSC, involve operations on files and directories within python/lsst/ts/xml. To add a CSC:

* Add an entry in data/sal_interfaces/SALSubsystems.xml
* Add directory in data/sal_interfaces for the CSC
* Add necessary topic type XML files in the new CSC directory
* Add entry in CSC list in testutils.py

To rename a CSC:

* Rename the entry in data/sal_interfaces/SALSubsystems.xml
* Rename CSC in dependency entries if applicable
* Rename directory in data/sal_interfaces
* Rename files in CSC directory making sure to update the contents too
* Rename CSC entry in testutils.py list

To delete a CSC:

* Delete entry in data/sal_interfaces/SALSubsystems.xml
* Delete CSC in dependency entries if applicable 
* Delete directory and files in data/sal_interfaces corresponding to CSC
* Delete CSC entry from testutils.py list

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/lsst-ts/ts_xml/tags). 

## Contact Information

Please contact <rbovill@lsst.org> with any questions or concerns.
