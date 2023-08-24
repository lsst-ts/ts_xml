# This file is part of ts_xml
#
# Developed for the LSST Data Management System.
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

__all__ = ["generate_subsystems_doc"]

from typing import TextIO
from xml.etree import ElementTree

from . import testutils
from .utils import find_text_in_xml, get_pkg_root, get_sal_interfaces_dir

# XML attributes to ignore.
IGNORED_ATTRIBUTES = ["EFDB_Name", "Description"]

# XML fields to ignore.
IGNORED_FIELDS = [
    "Description",
    "Alias",
    "Device",
    "Property",
    "Action",
    "Value",
    "Subsystem",
    "Version",
    "Author",
    "Explanation",
]


def topic_sort_key(child: ElementTree.Element) -> tuple[str, str]:
    """Sort key for generics.

    Parameters
    ----------
    child : `xml.etree.ElementTree.Element`
        Child element from an XML file.
    """
    topic = child.find("EFDB_Topic")
    if topic is None:
        second_value = child.tag
    else:
        assert topic.text is not None
        second_value = topic.text.split("_")[-1]
    return (child.tag, second_value)


def write_heading(
    f: TextIO, name: str, char: str = "-", overline: bool = False
) -> None:
    """Write a heading with specified underline and optional overline.

    Parameters
    ----------
    f : `file`
        File to which to write
    name : `str`
        Heading name
    char : `str`
        Underline character
    overline : `bool`
        Also write an overline?

    Notes
    -----
    Examples::

        write_heading(f=f, name="Minor_Heading")
        f.write("\n")
        write_heading(f=f, name="Major_Heading", char="#", overline=True)

    writes:

        Minor_Heading
        -------------

        #############
        Major_Heading
        #############
    """
    if len(char) != 1:
        raise ValueError(f"char={char!r} must be exactly one character long")
    marker = char * len(name) + "\n"
    if overline:
        f.write(marker)
    f.write(name + "\n")
    f.write(marker)


def create_generics_dict(generics: str | None) -> dict[str, list[str]]:
    """Create a dictionary of needed generic commands and events.

    Parameters
    ----------
    generics : `str` or `None`
        Comma-separated list of added generics, from SalSubsystems.xml
        AddedGenerics. Ignored if blank or None.

    Returns
    -------
    `dict`
        The needed set of generic commands and events.
    """
    commands = []
    events = []

    commands.extend(testutils.added_generics_mandatory_commands)
    events.extend(testutils.added_generics_mandatory_events)

    if generics:
        for generic in generics.split(","):
            generic = generic.strip()
            try:
                commands.extend(
                    getattr(testutils, f"added_generics_{generic}_commands")
                )
                events.extend(getattr(testutils, f"added_generics_{generic}_events"))
            except AttributeError:
                if generic.startswith("command"):
                    commands.append(generic.split("_")[-1])
                elif generic.startswith("logevent"):
                    events.append(generic.split("_")[-1])
                else:
                    pass

    generic_dict = {"Command": sorted(commands), "Event": sorted(events)}
    return generic_dict


def add_generics(
    cf: TextIO,
    subsystem: str,
    set_name: str,
    has_generics: dict[str, list[str]],
    has_specific_topic_type: list[str],
) -> None:
    """Adds generic topics to the rst file in the appropriate section.

    Parameters
    ----------
    cf : `file object`
        SAL component rst documentation file.
    subsystem : `str`
        The name of the SAL subsystem.
    set_name : `str`
        The name of the topic set.
    has_generics : `dict`
        The set of generic topics.
    has_specific_topic_type : `List` of `str`
        A list containing the names of a type of topic, name must be
        capitalized.
        For example, ["Command", "Event", "Telemetry"].

    """
    xml_dir = get_sal_interfaces_dir()

    gen_tree = ElementTree.parse(xml_dir / "SALGenerics.xml")
    gen_root = gen_tree.getroot()
    for gen_set in gen_root:
        gen_set[:] = sorted(gen_set, key=topic_sort_key)
        gen_set_name = gen_set.tag
        if gen_set_name == set_name:
            # Remove SAL and Set from the string in order to compare topic
            # set name correctly.
            topic_type = gen_set_name[3:-3]
            if topic_type not in has_specific_topic_type:
                write_heading(cf, name=f"{topic_type}s")
            for gen_topic in gen_set:
                if gen_topic.tag == "Enumeration":
                    continue
                topic_text = find_text_in_xml(gen_topic, "EFDB_Topic")
                short_name = topic_text.split("_")[-1]
                if short_name not in has_generics[topic_type]:
                    continue
                write_heading(cf, name=short_name, char="~")
                gen_topic_description = gen_topic.find("Description")
                if gen_topic_description is not None:
                    assert gen_topic_description.text is not None
                    cf.write(f"**Description**: {gen_topic_description.text}\n\n")
                for gen_field in gen_topic:
                    if gen_field.tag == "item":
                        gen_field_name_text = find_text_in_xml(gen_field, "EFDB_Name")
                        gen_field_description_text = find_text_in_xml(
                            gen_field, "Description"
                        )
                        cf.write(
                            f"\n.. _{subsystem}:{short_name}:{gen_field_name_text}:\n\n"
                        )
                        write_heading(cf, gen_field_name_text, char="*")
                        for gen_attribute in gen_field:
                            if gen_attribute.tag in ["Count", "IDL_Size"]:
                                if gen_attribute.text == "1":
                                    pass
                                else:
                                    cf.write(
                                        f":{gen_attribute.tag}: {gen_attribute.text}\n"
                                    )
                            elif gen_attribute.tag in IGNORED_ATTRIBUTES:
                                pass
                            else:
                                cf.write(
                                    f":{gen_attribute.tag}: {gen_attribute.text}\n"
                                )
                        cf.write(f"\n**Description**: {gen_field_description_text}\n\n")
                    elif gen_field.tag in IGNORED_FIELDS:
                        pass
                    else:
                        cf.write(f":{gen_field.tag}: {gen_field.text}\n")
                    cf.write("\n")
        else:
            pass


def generate_subsystems_doc() -> None:
    """Generates SAL subsystem rst documentation from XML.

    Subsystem-specific topics are listed first, then generic topics.
    Topics are alphabetized within each group.
    """
    rst_dir = get_pkg_root() / "doc" / "sal_interfaces"
    rst_dir.mkdir(parents=True, exist_ok=True)

    # Write the rst table of contents.
    with open(rst_dir / "index.rst", "w") as f:
        write_heading(f, name="SAL Interfaces", char="#", overline=True)
        f.write(
            """
.. note:: This page is generated by python script ``generate_cet.py``.

SAL Interfaces for all CSCs and other SAL components.

.. toctree::
  :glob:
  :maxdepth: 1

  *

"""
        )

    # Write one rst file for each SAL component.
    xml_dir = get_sal_interfaces_dir()
    subsystem_tree = ElementTree.parse(xml_dir / "SALSubsystems.xml")
    subsystem_tree_root = subsystem_tree.getroot()
    for subsystem_elt in subsystem_tree_root:
        subsystem = find_text_in_xml(subsystem_elt, "Name")
        # has_specific_topic_type starts empty for each CSC because it is
        # unknown if it has a topic file.
        has_specific_topic_type = []
        generics = find_text_in_xml(subsystem_elt, "AddedGenerics")
        has_generics = create_generics_dict(generics)

        with open(rst_dir / f"{subsystem}.rst", "w") as cf:
            cf.write(":tocdepth: 3\n\n")
            write_heading(cf, name=subsystem, char="#", overline=True)
            cf.write(
                f"""
.. note:: This page is generated by python script ``generate_cet.py``.

:ref:`Back to table <index:csc-table:{subsystem.lower()}>`

"""
            )
            for dds_type in ["Commands", "Events", "Telemetry"]:
                try:
                    tree = ElementTree.parse(
                        xml_dir / subsystem / f"{subsystem}_{dds_type}.xml"
                    )
                    has_specific_topic_type.append(dds_type[:-1])
                except FileNotFoundError:
                    add_generics(
                        cf,
                        subsystem,
                        set_name=f"SAL{dds_type[:-1]}Set",
                        has_generics=has_generics,
                        has_specific_topic_type=has_specific_topic_type,
                    )
                    continue
                if dds_type != "Events":
                    write_heading(cf, name=dds_type)
                root = tree.getroot()
                set_name = root.tag
                root[:] = sorted(root, key=topic_sort_key)
                enumeration_seen = False
                first_event = True
                for topic in root:
                    if topic.tag == "Enumeration":
                        if dds_type == "Events" and not enumeration_seen:
                            write_heading(cf, name="Enumerations")
                            enumeration_seen = True
                        assert topic.text is not None
                        states = topic.text.split(",")
                        state_name = states[0].split("_")[0].lstrip()
                        cf.write(f":{state_name}:\n")
                        for state in states:
                            # enum item format `\n enumClassName_itemName
                            # [=value]`
                            # where itemName may include underscores,
                            # and all whitespace is optional and of
                            # arbitrary length.
                            state = state.split("_", 1)[
                                1
                            ]  # strip the beginning through the first underscore.
                            cf.write(f"  * {state}\n")  # noqa
                        cf.write("\n")
                        continue
                    if dds_type == "Events" and first_event:
                        write_heading(cf, name="Events")
                        first_event = False
                    topic_name = find_text_in_xml(topic, "EFDB_Topic")
                    if dds_type in ["Commands", "Events"]:
                        short_name = topic_name.split("_", 2)[-1]
                    else:
                        short_name = topic_name.split("_", 1)[-1]
                    cf.write(f".. _{subsystem}:{dds_type}:{short_name}:\n\n")
                    write_heading(cf, name=short_name, char="~")
                    topic_description = topic.find("Description")
                    if topic_description is not None:
                        cf.write(f"**Description**: {topic_description.text}\n\n")
                    for field in topic:
                        if field.tag == "item":
                            efdb_name = find_text_in_xml(field, "EFDB_Name")
                            cf.write(
                                f"\n.. _{subsystem}:{dds_type}:{short_name}:{efdb_name}:\n\n"
                            )
                            write_heading(cf, name=efdb_name, char="*")
                            for attribute in field:
                                if attribute.tag in IGNORED_ATTRIBUTES:
                                    pass
                                elif attribute.tag in ["Count", "IDL_Size"]:
                                    if attribute.text == "1":
                                        pass
                                    else:
                                        cf.write(
                                            f":{attribute.tag}: {attribute.text}\n"
                                        )
                                else:
                                    cf.write(f":{attribute.tag}: {attribute.text}\n")
                            description = find_text_in_xml(field, "Description")
                            cf.write(f"\n**Description**: {description}\n\n")
                        elif field.tag in IGNORED_FIELDS:
                            pass
                        else:
                            cf.write(f":{field.tag}: {field.text}\n")
                        cf.write("\n")
                add_generics(
                    cf, subsystem, set_name, has_generics, has_specific_topic_type
                )
