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

TAI_REGEX = re.compile(r"\bTAI\b", re.IGNORECASE)


def text(element: et.Element | None) -> str:
    """Return the stripped text of an XML element, or empty string if missing.

    Parameters
    ----------
    element : `xml.etree.ElementTree.Element` | `None`
        The XML element whose text should be extracted. If `None`, or if
        the element has no text, an empty string is returned.

    Returns
    -------
    str
        The element text with leading and trailing whitespace removed,
        or an empty string.
    """
    if element is None:
        return ""
    return (element.text or "").strip()


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_no_float_timestamps(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Test that no timestamp topic attributes have type `float`.
    Timestamps should typically have a type of `double`, and `float`
    is never appropriate for a timestamp formatted as unix time.

    Timestamp attributes are detected by either of the following:

     * The EFDB_Name contains the substring "timestamp"
     * The Description contains the whole word "TAI"

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
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()

    violators = []
    for topic_tree in root.findall(f"./{saltype}"):
        topic_name = text(topic_tree.find("EFDB_Topic"))

        for item in topic_tree.findall("./item"):
            efdb_name = text(item.find("EFDB_Name"))
            description = text(item.find("Description"))
            idl_type = text(item.find("IDL_Type"))

            has_timestamp_in_name = "timestamp" in efdb_name.lower()
            has_tai_in_description = bool(TAI_REGEX.search(description))

            if (
                has_timestamp_in_name or has_tai_in_description
            ) and idl_type == "float":
                violators.append(f"{topic_name}:{efdb_name}")

    assert (
        not violators
    ), f"IDL_Type must not be `float` for timestamp. Use `double` instead: {'; '.join(violators)}"
