# LSST Interface Definitions

## Glossary

- CSC  -   Commandable SAL Component
- DDS  -   Data Distriubtion Services
- LSST -   Large Synoptic Survey Telescope
- SAL  -   Service Abstraction Layer
- TSSW -   LSST Telescope & Site Software
- XML  -   eXtensible Markup Language

## Description

This repository contains all the interface defintion files for all the CSCs of the LSST.  All of the CSCs communicate using the DDS protocol.  TSSW provides a wrapper utility around DDS, called the Service Abstraction Layer or SAL.

* (https://github.com/lsst-ts/ts_sal) 

The SAL produces libraries in C++, LabVIEW, Java, PyDDS, and Python, for each CSC.  These libraries are then used by all the CSCs that need to publish or subscribe to any message topic.

### Installation and Usage

This repo is primarily a single location for all the definition files.  This repo in conjuction with the SAL are used to produce the code libraries.  Please refer to the documentation in the ts_sal project for instructions on manually producing those libraries.

### Testing

To ensure the successful build of your libraries, there are unit tests contained in the tests/ directory.  To run them, first setup the test environment

```
pip install -r test_requirements.txt -e .
```

This will install the pytest, pytest-flake8 and astropy modules used to verify the XML files are correct.  Then execute:

```
pytest -ra
```

from anywhere in the repository.  This will run the tests and print out a short summary of the results, including tests that are skipped for known reasons.  The messages associated with the skiped tests include Jira ticket numbers to track the issues.  Please navigate to 

* [LSST Jira](https://jira.lsstcorp.org/secure/Dashboard.jspa)

to find the specific ticket.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/lsst-ts/ts_xml/tags). 
