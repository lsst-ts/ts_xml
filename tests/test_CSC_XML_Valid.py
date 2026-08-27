#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of ts_xml.
#
# Developed for the Vera C. Rubin Observatory Telescope and Site Systems.
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import pathlib

import lsst.ts.xml as ts_xml
import pytest
from lxml import etree


def check_for_issues(csc: str, topic: str) -> str:
    jira = ""
    return jira


def get_xml_schema(saltype: str) -> etree.XMLSchema:
    datadir = ts_xml.get_data_dir()
    xmlschema_doc = etree.parse(f"{datadir}/schema/{saltype}Set.xsd")
    xmlschema = etree.XMLSchema(xmlschema_doc)
    return xmlschema


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_csc_xml_valid(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Test that the CSC XML files are valid and conform to the schema.

    Parameters
    ----------
    csc : `csc`
        Name of the CSC
    topic : `str`
        One of ['Commands','Events','Telemetry']
    xmlfile : `pathlib.Path`
        Full filepath to each XML file for the CSC.
    xmlschema : `pathlib.Path`
        Full filepath to schema XSD file for the xmlfile.
    """
    saltype = "SAL" + topic.rstrip("s")
    xmlschema = get_xml_schema(saltype)
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(f"{jira}: {xmlfile.name} Does not conform to XML schema.")
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = etree.parse(f)
    try:
        xmlschema.assertValid(tree)
    except etree.DocumentInvalid as err:
        assert False, f"{xmlfile.name}: {err}"
