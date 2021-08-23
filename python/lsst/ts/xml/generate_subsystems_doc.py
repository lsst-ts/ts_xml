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

from xml.etree import ElementTree

from . import utils


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


def topic_sort_key(child):
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
        second_value = topic.text.split("_")[-1]
    return (child.tag, second_value)


def write_heading(f, name, char="-", overline=False):
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


def add_generics(cf, subsystem, set_name, has_generics, has_specific_topic_type):
    """Adds generic topics to the rst file in the appropriate section.

    Parameters
    ----------
    cf : `file object`
        SAL component rst documentation file.
    subsystem : `str`
        The name of the SAL subsystem.
    set_name : `str`
        The name of the topic set.
    has_generics : `bool` or `List` of `str`
        True if it has all generic topics.
        False if it has no generic topics.
        A list of generic topic names if it has some generic topics.
    has_specific_topic_type : `List` of `str`
        A list containing the names of a type of topic, name must be
        capitalized.
        For example, ["Command", "Event", "Telemetry"].

    """
    xml_dir = utils.get_sal_interfaces_dir()
    if has_generics is True:
        gen_tree = ElementTree.parse(xml_dir / "SALGenerics.xml")
        gen_root = gen_tree.getroot()
        for gen_set in gen_root:
            gen_set[:] = sorted(gen_set, key=topic_sort_key)
            gen_set_name = gen_set.tag
            if gen_set_name == set_name:
                # Remove SAL and Set from the string in order to compare topic
                # set name correctly.
                if gen_set_name[3:-3] not in has_specific_topic_type:
                    write_heading(cf, name=f"{gen_set_name[3:-3]}s")
                for gen_topic in gen_set:
                    topic_name = gen_topic.find("EFDB_Topic").text
                    short_name = topic_name.split("_")[-1]
                    write_heading(cf, name=short_name, char="~")
                    gen_topic_description = gen_topic.find("Description")
                    if gen_topic_description is not None:
                        cf.write(f"**Description**: {gen_topic_description.text}\n\n")
                    for gen_field in gen_topic:
                        if gen_field.tag == "item":
                            gen_field_name = gen_field.find("EFDB_Name")
                            gen_field_description = gen_field.find("Description")
                            cf.write(
                                f"\n.. _{subsystem}:{short_name}:{gen_field_name.text}:\n\n"
                            )
                            write_heading(cf, gen_field_name.text, char="*")
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
                            cf.write(
                                f"\n**Description**: {gen_field_description.text}\n\n"
                            )
                        elif gen_field.tag in IGNORED_FIELDS:
                            pass
                        else:
                            cf.write(f":{gen_field.tag}: {gen_field.text}\n")
                        cf.write("\n")
            else:
                pass

    elif has_generics is False:
        pass
    else:
        gen_tree = ElementTree.parse(xml_dir / "SALGenerics.xml")
        gen_root = gen_tree.getroot()
        for gen_set in gen_root:
            # Sorts xml file using the topic name(without the subsystem name)
            # as the key, if the topic name exists otherwise just add the tag
            # as is.
            gen_set[:] = sorted(gen_set, key=topic_sort_key)
            gen_set_name = gen_set.tag
            if gen_set_name == set_name:
                if gen_set_name[3:-3] not in has_specific_topic_type:
                    write_heading(cf, f"{gen_set_name[3:-3]}s")
                for gen_topic in gen_set:
                    gen_topic_name = gen_topic.find("EFDB_Topic")
                    gen_topic_short_name_array = gen_topic_name.text.split("_")[1:]
                    gen_topic_short_name = "_".join(gen_topic_short_name_array)
                    if gen_topic_short_name in has_generics:
                        topic_name = gen_topic.find("EFDB_Topic").text
                        short_name = topic_name.split("_")[-1]
                        write_heading(cf, name=short_name, char="~")
                        gen_topic_description = gen_topic.find("Description")
                        if gen_topic_description is not None:
                            cf.write(
                                f"**Description**: {gen_topic_description.text}\n\n"
                            )
                        for gen_field in gen_topic:
                            if gen_field.tag == "item":
                                gen_field_name = gen_field.find("EFDB_Name")
                                gen_field_description = gen_field.find("Description")
                                cf.write(
                                    f"\n.. _{subsystem}:{short_name}:{gen_field_name.text}:\n\n"
                                )
                                write_heading(cf, gen_field_name.text, char="*")
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
                                cf.write(
                                    f"\n**Description**: {gen_field_description.text}\n\n"
                                )
                            elif gen_field.tag in IGNORED_FIELDS:
                                pass
                            else:
                                cf.write(f":{gen_field.tag}: {gen_field.text}\n")
                            cf.write("\n")
                    else:
                        pass


def generate_subsystems_doc():
    """Generates SAL subsystem rst documentation from XML.

    Subsystem-specific topics are listed first, then generic topics.
    Topics are alphabetized within each group.
    """
    rst_dir = utils.get_pkg_root() / "doc" / "sal_interfaces"
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
    xml_dir = utils.get_sal_interfaces_dir()
    subsystem_tree = ElementTree.parse(xml_dir / "SALSubsystems.xml")
    subsystem_tree_root = subsystem_tree.getroot()
    for subsystem_elt in subsystem_tree_root:
        subsystem = subsystem_elt.find("Name").text
        # has_specific_topic_type starts empty for each CSC because it is
        # unknown if it has a topic file.
        has_specific_topic_type = []
        has_generics = False
        generics_text = subsystem_elt.find("Generics").text
        if generics_text == "yes":
            has_generics = True
        elif generics_text == "no":
            has_generics = False
        else:
            has_generics = generics_text

        with open(rst_dir / f"{subsystem}.rst", "w") as cf:
            cf.write(":tocdepth: 3\n\n")
            write_heading(cf, name=subsystem, char="#", overline=True)
            cf.write(
                f"""
.. note:: This page is generated by python script ``generate_cet.py``.

:ref:`Back to table <index:master-csc-table:{subsystem.lower()}>`

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
                        states = topic.text.split(",")
                        state_name = states[0].split("_")[0].lstrip()
                        cf.write(f":{state_name}:\n")
                        for state in states:
                            cf.write(
                                f"  * :any:`{state.split('_')[1]} <lsst.ts.idl.enums.{subsystem}.{state_name}.{state.split('_')[1].upper()}>`\n"  # noqa
                            )
                        cf.write("\n")
                        continue
                    if dds_type == "Events" and first_event:
                        write_heading(cf, name="Events")
                        first_event = False
                    topic_name = topic.find("EFDB_Topic").text
                    if dds_type in ["Commands", "Events"]:
                        short_name = topic_name.split("_", 2)[-1]
                    else:
                        short_name = topic_name.split("_", 1)[-1]
                    cf.write(f".. _{subsystem}:{dds_type}:{short_name}:\n\n")
                    write_heading(cf, name=short_name, char="~")
                    if topic.find("Description") is not None:
                        cf.write(
                            f"**Description**: {topic.find('Description').text}\n\n"
                        )
                    for field in topic:
                        if field.tag == "item":
                            efdb_name = field.find("EFDB_Name").text
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
                            cf.write(
                                f"\n**Description**: {field.find('Description').text}\n\n"
                            )
                        elif field.tag in IGNORED_FIELDS:
                            pass
                        else:
                            cf.write(f":{field.tag}: {field.text}\n")
                        cf.write("\n")
                add_generics(
                    cf, subsystem, set_name, has_generics, has_specific_topic_type
                )
