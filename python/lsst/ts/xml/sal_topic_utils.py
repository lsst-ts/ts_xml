from __future__ import annotations

# This file is part of ts_xml.
#
# Developed for the Rubin Observatory Telescope and Site System.
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__all__ = [
    "TopicType",
    "FILE_SUFFIX_DICT",
    "find_optional_text",
    "find_required",
    "find_required_text",
]

import enum
from xml.etree import ElementTree


class TopicType(enum.Enum):
    COMMAND = "Command"
    EVENT = "Event"
    TELEMETRY = "Telemetry"


FILE_SUFFIX_DICT = {
    TopicType.COMMAND: "Commands",
    TopicType.EVENT: "Events",
    TopicType.TELEMETRY: "Telemetry",
}


def find_optional_text(element: ElementTree.Element, name: str, default: str) -> str:
    """Find an optional sub-element in an XML element and return the text.

    Parameters
    ----------
    element : `ElementTree.Element`
        XML element
    name : `str`
        Sub-element name.
    default : `str`
        Value to return if the field does not exist.
    """
    subelt = element.find(name)
    if subelt is None or subelt.text is None:
        return default
    return subelt.text


def find_required(element: ElementTree.Element, name: str) -> ElementTree.Element:
    """Find a required sub-element in an XML element.

    Parameters
    ----------
    element : `ElementTree.Element`
        XML element
    name : `str`
        Sub-element name.
    """
    subelt = element.find(name)
    if subelt is None:
        raise RuntimeError(f"Could not find required sub-element {name!r}")
    return subelt


def find_required_text(element: ElementTree.Element, name: str) -> str:
    """Find a required sub-element in an XML element and return the text.

    Parameters
    ----------
    element : `ElementTree.Element`
        XML element
    name : `str`
        Sub-element name.
    """
    subelt = find_required(element=element, name=name)
    if subelt.text is None:
        raise RuntimeError(f"Required sub-element {name!r} had no text")
    return subelt.text
