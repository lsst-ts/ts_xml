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

__all__ = ["get_field_and_global_enums"]

import dataclasses
import re
from xml.etree import ElementTree

from .sal_topic_utils import (
    FILE_SUFFIX_DICT,
    TopicType,
    find_optional_text,
    find_required_text,
)
from .utils import get_sal_interfaces_dir


@dataclasses.dataclass
class FieldEnumInfo:
    topic_name: str
    field_name: str
    items: list[str]

    def as_tuple(self) -> tuple[str, dict[str, list[str]]]:
        """Get as a dictionary of plain old data, for json encoding.

        Return (topic_name, field_name, items)
        """
        return (
            self.topic_name,
            {self.field_name: [item.strip() for item in self.items]},
        )


@dataclasses.dataclass
class GlobalEnumInfo:
    class_name: str
    items: list[str]

    def as_tuple(self) -> tuple[str, list[str]]:
        """Get as a tuple of plain old data, for json encoding.

        Return (class_name, items)
        """
        return (self.class_name, self.items)

    @classmethod
    def from_enum_text(cls, enum_text: str) -> GlobalEnumInfo:
        """Make GlobalEnumInfo from text for a global enum XML element."""
        enum_text = enum_text.strip()
        raw_enums = re.split(r" *, *\n? *", enum_text)
        prefix_item_list = [raw.split("_", 1) for raw in raw_enums]
        prefixes, items = zip(*prefix_item_list)
        if not all(prefix == prefixes[0] for prefix in prefixes):
            raise RuntimeError(f"One or more inconsistent prefixes in {enum_text}")
        return cls(class_name=prefixes[0], items=list(items))


def get_field_enums_from_file_root(
    topic_type: TopicType, file_root: ElementTree.Element
) -> list[FieldEnumInfo]:
    """Get global enum info from a component file's xmlroot.

    Parameters
    ----------
    topic_type : `TopicType`
        Type of topics defined in this file.
    file_root : `ElementTree.Element`
        Root of one XML file (e.g. the root for ATDome_Commands.xml).

    Returns
    -------
    global_enum_infos : `list[GlobalEnumInfo]`
        List of global enum info.
    """
    field_enums: list[FieldEnumInfo] = []
    sal_topic_tag_name = {
        TopicType.COMMAND: "SALCommand",
        TopicType.EVENT: "SALEvent",
        TopicType.TELEMETRY: "SALTelemetry",
    }[topic_type]
    topic_elements = file_root.findall(sal_topic_tag_name)
    for topic_element in topic_elements:
        field_enums += get_field_enums_from_topic_element(topic_element)
    return field_enums


def get_field_enums_from_topic_element(
    topic_element: ElementTree.Element,
) -> list[FieldEnumInfo]:
    """Find all field enums in a given topic's XML element"""
    field_enums: list[FieldEnumInfo] = []
    topic_name = find_required_text(topic_element, "EFDB_Topic")
    item_elements = topic_element.findall("item")
    for item_element in item_elements:
        enum_text = find_optional_text(item_element, "Enumeration", "")
        if not enum_text:
            continue
        field_name = find_required_text(item_element, "EFDB_Name")
        items = re.split(r" *, *\n? *", enum_text)
        field_enums.append(
            FieldEnumInfo(topic_name=topic_name, field_name=field_name, items=items)
        )
    return field_enums


def get_global_enums_from_file_root(
    file_root: ElementTree.Element,
) -> list[GlobalEnumInfo]:
    """Get global enum info from a component file's xmlroot.

    Parameters
    ----------
    file_root : `ElementTree.Element`
        Root of one XML file (e.g. the root for ATDome_Commands.xml).

    Returns
    -------
    global_enum_infos : `list[GlobalEnumInfo]`
        List of global enum info.
    """
    enum_elements = file_root.findall("Enumeration")
    return [
        GlobalEnumInfo.from_enum_text(enum_text=element.text)
        for element in enum_elements
        if element.text is not None
    ]


def get_field_and_global_enums(
    name: str,
) -> tuple[list[FieldEnumInfo], list[GlobalEnumInfo]]:
    """Parse ts_xml for enums for one SAL component.

    Parameters
    ----------
    name : `str`
        SAL component name.
    """
    interfaces_dir = get_sal_interfaces_dir()
    field_enums: list[FieldEnumInfo] = []
    global_enums: list[GlobalEnumInfo] = []
    for topic_type in TopicType:
        file_suffix = FILE_SUFFIX_DICT[topic_type]
        filepath = interfaces_dir / name / f"{name}_{file_suffix}.xml"
        if not filepath.is_file():
            continue
        file_root = ElementTree.parse(filepath).getroot()
        field_enums += get_field_enums_from_file_root(
            topic_type=topic_type, file_root=file_root
        )
        global_enums += get_global_enums_from_file_root(file_root)
    return field_enums, global_enums
