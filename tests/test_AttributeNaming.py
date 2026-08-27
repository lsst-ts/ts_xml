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
import re
import xml.etree.ElementTree as et

import lsst.ts.xml as ts_xml
import pytest


def check_for_issues(csc: str, topic: str) -> str:
    jira = ""
    return jira


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_attribute_naming(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Test that the <EFDB_Name> field for topic attributes is properly formed,
    i.e. it begins with a lowercase letter and contains only alphanumeric
    and underscore characters.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `csc`
        Name of the CSC
    topic : `str`
        One of ['Commands','Events','Telemetry']
    """
    saltype = "SAL" + topic.rstrip("s")
    # Check for known issues.
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(f"{jira}: {xmlfile.name} <EFDB_Name> is not properly formed.")
    # Test the attribute <Description> fields.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    for name in root.findall(f"./{saltype}/item/EFDB_Name"):
        assert name.text is not None
        # re.match() returns None if the string does not match the regex.
        assert re.match(r"^[a-z]([a-zA-Z0-9_]*$)", name.text) is not None, (
            f"{name.text} in {xmlfile.name} does not begin with a lowercase "
            "letter and/or contains non-alphanumeric characters."
        )
