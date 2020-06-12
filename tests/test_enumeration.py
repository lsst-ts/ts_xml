#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import pytest
import xml.etree.ElementTree as et
import lsst.ts.xml as ts_xml


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_enumeration(xmlfile, csc, topic):
    """Test that enumerations have the correct format.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Events XML file for the CSC.
    csc : `testutils.subsystems`
        Name of the CSC
    """
    # Test the topic <EFDB_Name> field.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()

    reg_exp = re.compile(r"^[A-Z][a-zA-Z0-9_]*(\s*=\s*((0[xX][0-9a-fA-F]+)|(\d+)))?$")

    for sal_enum in root.findall("Enumeration"):
        for enum_value in sal_enum.text.split(","):
            assert (
                reg_exp.match(enum_value.strip()) is not None
            ), f"Invalid enumeration in {csc}/{topic}: {enum_value.strip()} :: {sal_enum.text}."
