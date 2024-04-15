#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
import xml.etree.ElementTree as et

import lsst.ts.xml as ts_xml
import pytest


def check_for_issues(csc: str, topic: str) -> str:
    match f"{csc}-{topic}":
        case "ATAOS-Telemetry" | "ATAOS-Commands" | "ATAOS-Events":
            return "DM-43789"
        case "ATBuilding-Telemetry" | "ATBuilding-Events":
            return "DM-43792"
        case "ATCamera-Commands" | "ATCamera-Telemetry" | "ATCamera-Events":
            return "DM-43793"
        case "ATHexapod-Commands" | "ATHexapod-Telemetry" | "ATHexapod-Events":
            return "DM-43794"
        case "ATMonochromator-Telemetry":
            return "DM-43795"
        case "ATPneumatics-Commands":
            return "DM-43798"
        case "ATSpectrograph-Events" | "ATSpectrograph-Commands":
            return "DM-43803"
        case "CCCamera-Commands" | "CCCamera-Telemetry" | "CCCamera-Events":
            return "DM-43804"
        case "CBP-Telemetry":
            return "DM-43806"
        case "EAS-Events" | "EAS-Telemetry":
            return "DM-43809"
        case "Electrometer-Events":
            return "DM-43811"
        case "GIS-Events":
            return "DM-43812"
        case "LinearStage-Events" | "LinearStage-Commands" | "LinearStage-Telemetry":
            return "DM-43814"
        case "MTAirCompressor-Events":
            return "DM-43815"
        case "MTCamera-Telemetry" | "MTCamera-Commands" | "MTCamera-Events":
            return "DM-43816"
        case "MTEEC-Commands" | "MTEEC-Events":
            return "DM-43817"
        case "MTM1M3-Telemetry" | "MTM1M3-Events" | "MTM1M3-Commands":
            return "DM-43819"
        case "MTM1M3TS-Commands" | "MTM1M3TS-Telemetry" | "MTM1M3TS-Events":
            return "DM-43820"
        case "MTMount-Events" | "MTMount-Telemetry":
            return "DM-43821"
        case "MTOODS-Events":
            return "DM-43822"
        case "PMD-Events" | "PMD-Telemetry":
            return "DM-43825"
        case "SummitFacility-Telemetry":
            return "DM-43826"
        case "TunableLaser-Events" | "TunableLaser-Commands":
            return "DM-43827"
        case "WeatherForecast-Telemetry":
            return "DM-43828"
        case _:
            return ""


@pytest.mark.parametrize("xmlfile,csc,topic", ts_xml.get_xmlfile_csc_topic())
def test_topic_description(xmlfile: pathlib.Path, csc: str, topic: str) -> None:
    """Tests the <Description> field for topic attributes \
    is properly defined, i.e. it is not blank.

    Parameters
    ----------
    csc : `csc`
        Name of the CSC
    topic : `str`
        One of ['Commands','Events','Telemetry']
    xmlfile : `pathlib.Path`
        Full filepath to the Commands or Events XML file for the CSC.
    """
    saltype = "SAL" + topic.rstrip("s")

    # Test the topic <Description> fields.
    with open(str(xmlfile), "r", encoding="utf-8") as f:
        tree = et.parse(f)
    root = tree.getroot()
    faulty_descriptions = []
    for element in root.findall(f"./{saltype}"):
        name = element.find("EFDB_Topic")
        assert name is not None
        assert name.text is not None
        description = element.find("Description")
        if description is None:
            faulty_descriptions.append(f"Topic {name.text} requires a description.")
        elif description.text is None:
            faulty_descriptions.append(f"Description of {name.text} cannot be blank.")
        elif description.text.replace(" ", "") == "":
            faulty_descriptions.append(
                f"Description of {name.text} cannot contain only whitespace."
            )

    # Check for known issues.
    jira = check_for_issues(csc, topic)
    if jira:
        pytest.skip(
            f"{jira}: {csc}_{topic}.xml requires the following "
            f"description improvements: {faulty_descriptions}."
        )
    else:
        assert len(faulty_descriptions) == 0, f"{faulty_descriptions}"
