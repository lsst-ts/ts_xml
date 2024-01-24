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

__all__ = ["ComponentInfo"]

import typing
from xml.etree import ElementTree

from .sal_topic_utils import (
    FILE_SUFFIX_DICT,
    TopicType,
    find_optional_text,
    find_required_text,
)
from .topic_info import TopicInfo, make_ackcmd_topic_info
from .utils import get_sal_interfaces_dir


class ComponentInfo:
    """Information about one SAL component.

    Parameters
    ----------
    name : `str`
        SAL component name.
    topic_subname : `str`
        Sub-namespace for Kafka topic names.
    use_simple_schema : `bool`, optional
        Use simple schema, without null support for float and double?

    Attributes
    ----------
    name : `str`
        SAL component name
    topic_subname : `str`
        Sub-namespace for Kafka topic names and schema namespace.
    description : `str`
        Description, from SALSubsystems.xml
    indexed : `bool`
        Is this component indexed (can there be different instances
        with different SAL indices)?
    added_generics : `list` [`str`]
        Added generic categories and/or SAL topic names
        (e.g. command_enterControl).
        This comes from the AddedGenerics field of SALSubsystems.xml
    topics : `dict` [`str`, `TopicInfo`]
        Dict of attr_name: TopicInfo.
    use_simple_schema : `bool`
        Use simple schema, without null support for float and double?
    """

    def __init__(
        self, name: str, topic_subname: str, use_simple_schema: bool = False
    ) -> None:
        self.name = name
        self.topic_subname = topic_subname
        self.use_simple_schema = use_simple_schema
        self._set_basics()
        self.topics = self._make_topics()

    def make_avro_schema_dict(self) -> dict[str, dict[str, typing.Any]]:
        """Create a dict of topic attr name: Avro schema dict."""
        return {
            topic_info.attr_name: topic_info.make_avro_schema()
            for topic_info in self.topics.values()
        }

    def _get_topic_elements(self) -> list[ElementTree.Element]:
        """Get component-specific topic elements.

        The ``name`` attribute must have been set.
        """
        interfaces_dir = get_sal_interfaces_dir()
        topic_elts: list[ElementTree.Element] = []
        for topic_type in TopicType:
            file_suffix = FILE_SUFFIX_DICT[topic_type]
            filepath = interfaces_dir / self.name / f"{self.name}_{file_suffix}.xml"
            if not filepath.is_file():
                continue
            topic_root = ElementTree.parse(filepath).getroot()
            topic_elts += topic_root.findall(f"SAL{topic_type.value}")
        return topic_elts

    def _make_topics(self) -> dict[str, TopicInfo]:
        """Set the ``topics`` attribute.

        The ``name``, ``indexed``, and ``added_generics`` fields must be
        set before calling this.
        """
        # Dict of topic_name: topic element
        # The topic name has no subsystem prefix,
        # e.g. logevent_logMessage
        generic_topic_element_dict, generic_category_dict = parse_sal_generics()
        component_topic_elements = self._get_topic_elements()

        # Dict of topic name: topic element
        topic_element_dict: dict[str, ElementTree.Element] = dict()

        def add_topic(elt: ElementTree.Element) -> None:
            """Add a topic element to topic_element_dict"""
            topic_name = find_required_text(elt, "EFDB_Topic")
            topic_name = topic_name.split("_", 1)[1]
            if topic_name in topic_element_dict:
                raise RuntimeError(f"topic {topic_name} already found")
            topic_element_dict[topic_name] = elt

        for generic_name in self.added_generics:
            if "_" in generic_name:
                # generic_name is a topic name
                topic_elt = generic_topic_element_dict.get(generic_name)
                if topic_elt is None:
                    raise ValueError(f"Unrecognized generic topic name {generic_name}")
                add_topic(topic_elt)
            else:
                # generic_name is a category name
                generic_elt_list = generic_category_dict.get(generic_name)
                if generic_elt_list is None:
                    raise ValueError(f"Unrecognized generic category {generic_name}")
                for elt in generic_elt_list:
                    add_topic(elt)

        for topic_elt in component_topic_elements:
            add_topic(topic_elt)

        topics_list: list[TopicInfo] = [
            TopicInfo.from_xml_element(
                topic_element,
                component_name=self.name,
                topic_subname=self.topic_subname,
                indexed=self.indexed,
                use_simple_schema=self.use_simple_schema,
            )
            for topic_element in topic_element_dict.values()
        ]
        topics_list.append(
            make_ackcmd_topic_info(
                component_name=self.name,
                topic_subname=self.topic_subname,
                indexed=self.indexed,
                use_simple_schema=self.use_simple_schema,
            )
        )
        return {info.attr_name: info for info in topics_list}

    def _set_basics(self) -> None:
        """Parse SALSubystems.xml and set the added_generics, indexed,
        and description fields

        The ``name`` field must be set before calling this.
        """
        interfaces_dir = get_sal_interfaces_dir()
        subsystems_root = ElementTree.parse(
            interfaces_dir / "SALSubsystems.xml"
        ).getroot()
        elements = [
            elt
            for elt in subsystems_root
            if find_required_text(elt, "Name") == self.name
        ]
        if not elements:
            raise ValueError(f"No such component {self.name}")
        if len(elements) > 1:
            raise ValueError(f"Multiple components found with Name={self.name!r}")
        element = elements[0]

        self.description = find_optional_text(element, "Description", "")
        self.added_generics = ["mandatory"] + [
            item.strip()
            for item in find_required_text(element, "AddedGenerics").split(",")
        ]
        self.indexed = find_required_text(element, "IndexEnumeration").strip() != "no"


def parse_sal_generics() -> (
    tuple[
        dict[str, ElementTree.Element],
        dict[str, list[ElementTree.Element]],
    ]
):
    """Parse SALGenerics.xml.

    Return two dicts:
    * topic_element_dict: topic name: XML topic element
        where topic name is missing the SALGeneric_ prefix
    * category_dict: category: list of XML topic elements
    """
    interfaces_dir = get_sal_interfaces_dir()
    generics = ElementTree.parse(interfaces_dir / "SALGenerics.xml").getroot()

    topic_element_dict: dict[str, ElementTree.Element] = dict()
    category_dict: dict[str, list[ElementTree.Element]] = dict()
    for gen in generics.findall("*/"):
        if gen.tag == "Enumeration":
            continue
        topic_name = find_required_text(gen, "EFDB_Topic")
        brief_name = topic_name[len("SALGeneric_") :]
        topic_element_dict[brief_name] = gen
        category_elt = gen.find("Category")
        if category_elt is None or category_elt.text is None:
            continue
        category = category_elt.text
        if category not in category_dict:
            category_dict[category] = []
        category_dict[category].append(gen)
    return topic_element_dict, category_dict
