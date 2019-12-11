******
ts_xml
******

Pages
=====

.. toctree::
    :maxdepth: 1

    sal_constraints_and_recommendations
    csc_information

The ``ts_xml`` package defines the data objects for all Commandable SAL
Components (CSC). These data objects are defined in XML. SAL consumes the XML to 
produce language specific libraries that enable communication over the DDS 
network. Below is a table overview of all the CSC's defined and a :ref:`index:Legend` to help
understand the table.

Master CSC Table
================

.. csv-table:: List of defined Commandable SAL Components (CSC)
   :file: orderedSubsystemData.csv
   :widths: auto
   :header-rows: 1

Legend
======

**Subsystem**
  Also known as the Commandable SAL Component. This is a subsystem that is 
  capable of subscribing or publishing topics over the DDS Domain network. Also,
  most contain a state machine that follow the requirements listed in :ref:`sal_constraints_and_recommendations:SAL Constraints and Recommendations`

**Active Developers**
  Current list of developers that are actively working on the Subsystem. This can
  be helpful when you are seeking for detailed questions of how the CSC works.

**Principal CSC Owner**
  Can also be thought of the acting manager of the CSC. The Principal CSC Owner
  works with Active developers to further progress on the CSC. Often meeting with
  each other on a regular basis to guide the Active Developers.

**Github**
  Repository for where the source code for the CSC can be found.

**Simulator**
  Y if there exists a simulator for this CSC, N if not.

**Jenkins Test Results**
  Link to where you can find the tests being ran on this CSC.

**LSST PoC**
  Point of contact on the LSST team. This person can be reached out to help answer
  any questions regarding the CSC.

**CSC DOc**
  Link to where there is documentation for this CSC.

**Product Owner**
  place holder, Michael I have a question for you. How is the product owner
  different than the principal CSC owner

**Related Documents**
  Documents that are related to this CSC. These can be design documents,
  requirement documents etc.

**Software Language**
  Software language that the CSC is being written in. 

**Runtime Languages**
  Comma seperated list of languages for which the CSC needs to produce libraries.
  With the intention to minimize build time by only producing the necessary 
  libraries. 

**Vendor PoC**
  Point of contact if the CSC is developed by a vendor.
