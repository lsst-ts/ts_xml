#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum
import xml.etree.ElementTree as et

import lsst.ts.xml as ts_xml
import pytest


class Restriction(enum.Enum):
    """Field naming restriction categories."""

    IDL = enum.auto()
    SAL = enum.auto()
    DB_CRITICAL = enum.auto()
    DB_OPTIONAL = enum.auto()


def check_for_issues(csc, topic, restriction):
    restriction = Restriction(restriction)  # check the argument
    if (
        csc == "ATAOS"
        and topic == "Commands"
        and restriction is Restriction.DB_OPTIONAL
    ):
        jira = "DM-22612"
    elif (
        csc == "ATMCS"
        and topic in ("Commands", "Events")
        and restriction is Restriction.DB_CRITICAL
    ):
        jira = "DM-22613"
    elif (
        csc == "ATSpectrograph"
        and topic in ("Commands", "Events")
        and restriction is Restriction.DB_OPTIONAL
    ):
        jira = "DM-22614"
    elif (
        csc == "FiberSpectrograph"
        and topic == "Commands"
        and restriction is Restriction.DB_OPTIONAL
    ):
        jira = "DM-22616"
    elif csc == "LOVE" and topic == "Events" and restriction is Restriction.DB_OPTIONAL:
        jira = "DM-22617"
    elif csc == "ATCamera" and restriction is Restriction.DB_OPTIONAL:
        jira = "CAP-793"
    elif csc == "MTCamera" and restriction is Restriction.DB_OPTIONAL:
        jira = "CAP-397"
    elif csc == "CCCamera" and restriction is Restriction.DB_OPTIONAL:
        jira = "CAP-402"
    elif (
        csc == "Scheduler"
        and topic == "Telemetry"
        and restriction is Restriction.DB_OPTIONAL
    ):
        jira = "DM-22625"
    elif (
        csc in ("Script", "ScriptQueue")
        and topic == "Events"
        and restriction is Restriction.DB_OPTIONAL
    ):
        jira = "DM-22626"
    elif (
        csc == "Test" and topic == "Commands" and restriction is Restriction.DB_OPTIONAL
    ):
        jira = "DM-22627"
    elif (
        csc == "Watcher"
        and topic in ("Commands", "Events")
        and restriction is Restriction.DB_OPTIONAL
    ):
        jira = "DM-22628"
    else:
        jira = ""
    return jira


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_reserved_words(xmlfile, csc, topic):
    """Control function to execute the IDL, and
    database reserved words tests.
    """
    for restriction in Restriction:
        reserved_words(xmlfile=xmlfile, csc=csc, topic=topic, restriction=restriction)


def reserved_words(xmlfile, csc, topic, restriction):
    """Test that the <EFDB_Name> field does not use any Reserved Words.

    Parameters
    ----------
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    csc : `testutils.subsystems`
        Name of the CSC
    topic : `xmlfile.stem`
        One of ['Commands', 'Events', 'Telemetry']
    restriction : `Restriction`
        Category of prohibited field names.
    """
    restriction = Restriction(restriction)  # check the argument
    saltype = "SAL" + topic.rstrip("s")
    # Check for known issues with database reserved words.
    # The IDL and SAL reserved words are non-negotiable.
    if restriction in {Restriction.DB_CRITICAL, Restriction.DB_OPTIONAL}:
        jira = check_for_issues(csc, topic, restriction)
        if jira:
            pytest.skip(
                f"{jira}: {xmlfile.name} <EFDB_Name> uses {restriction.name} reserved word."
            )
    # Test the <EFDB_Name> fields do not use Reserved Words.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    bad_names = []
    # Set the list based on the restriction type.
    word_list = {
        Restriction.IDL: ts_xml.idl_reserved,
        Restriction.SAL: ts_xml.sal_reserved,
        Restriction.DB_CRITICAL: ts_xml.db_critical_reserved,
        Restriction.DB_OPTIONAL: ts_xml.db_optional_reserved,
    }[restriction]
    for name in root.findall(f"./{saltype}/item/EFDB_Name"):
        if name.text.upper() in word_list:
            bad_names.append(name.text.upper())
    assert (
        bad_names == []
    ), f"{restriction.name} Reserved Words used one or more times: {(bad_names)}"
