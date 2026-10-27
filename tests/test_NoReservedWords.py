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

import enum
import pathlib
import xml.etree.ElementTree as et

import lsst.ts.xml as ts_xml
import pytest


class Restriction(enum.Enum):
    """Field naming restriction categories."""

    SAL = enum.auto()
    DB_CRITICAL = enum.auto()
    DB_OPTIONAL = enum.auto()


def check_for_exemption(csc: str, topic: str, attribute: str) -> bool:
    """Function to check if the CSC has an exemption for the use
    of specific database reserved words. This is a static list of
    grandfathered exemptions and SHOULD NOT BE CHANGED.
    """
    if (
        (csc == "ATAOS" and topic == "Commands" and attribute == "OFFSET")
        or (
            csc == "ATSpectrograph"
            and topic in ("Commands", "Events")
            and attribute == "NAME"
        )
        or (
            csc == "FiberSpectrograph"
            and topic == "Commands"
            and attribute == "DURATION"
        )
        or (csc == "LOVE" and topic == "Events" and attribute == "USER")
        or (csc == "ATCamera" and topic == "Commands" and attribute == "NAME")
        or (
            csc == "ATCamera"
            and topic == "Events"
            and attribute in ("DURATION", "NAME", "OFFSET")
        )
        or (csc == "MTCamera" and topic == "Commands" and attribute == "NAME")
        or (
            csc == "MTCamera"
            and topic == "Events"
            and attribute in ("DURATION", "NAME", "OFFSET")
        )
        or (csc == "CCCamera" and topic == "Commands" and attribute == "NAME")
        or (
            csc == "CCCamera"
            and topic == "Events"
            and attribute in ("DURATION", "NAME", "OFFSET")
        )
        or (
            csc in ("Script", "ScriptQueue")
            and topic == "Events"
            and attribute == "DURATION"
        )
        or (csc == "Test" and topic == "Commands" and attribute == "DURATION")
        or (
            csc == "Watcher"
            and topic == "Commands"
            and attribute in ("DURATION", "NAME")
        )
        or (csc == "Watcher" and topic == "Events" and attribute == "NAME")
    ):
        exemption = True
    else:
        exemption = False
    return exemption


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_reserved_words(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Control function to execute the database
    reserved words tests.
    """
    for restriction in Restriction:
        reserved_words(xmlfile=xmlfile, csc=csc, topic=topic, restriction=restriction)


def reserved_words(
    xmlfile: pathlib.Path, csc: str, topic: str, restriction: Restriction
) -> None:
    """Test that the <EFDB_Name> field does not use any Reserved Words.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `str`
        Name of the CSC
    topic : `str`
        One of ['Commands', 'Events', 'Telemetry']
    restriction : `Restriction`
        Category of prohibited field names.
    """
    restriction = Restriction(restriction)  # check the argument
    saltype = "SAL" + topic.rstrip("s")
    # Check for known issues with database reserved words.
    # The DB_CRITICAL and SAL reserved words are non-negotiable.
    # f"""
    # """
    # Test the <EFDB_Name> fields do not use Reserved Words.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    bad_names: list[str] = []
    # Set the list based on the restriction type.
    word_list = {
        Restriction.SAL: ts_xml.sal_reserved,
        Restriction.DB_CRITICAL: ts_xml.db_critical_reserved,
        Restriction.DB_OPTIONAL: ts_xml.db_optional_reserved,
    }[restriction]
    for name in root.findall(f"./{saltype}/item/EFDB_Name"):
        assert name.text is not None
        if name.text.upper() in word_list:
            exemption = check_for_exemption(csc, topic, name.text.upper())
            if exemption:
                pytest.skip(
                    f"""Please see https://rubinobs.atlassian.net/browse/SSW-250 for details.
                    {xmlfile.name} has an exemption for the use of the {name.text.upper()} reserved word.
                    """
                )
            else:
                bad_names.append(name.text.upper())
    assert (
        bad_names == []
    ), f"{restriction.name} Reserved Words used one or more times: {(bad_names)}"
