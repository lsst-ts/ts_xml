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

__all__ = ["write_generic_page"]

from xml.etree import ElementTree

from . import utils
from .generate_subsystems_doc import write_heading


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


def write_generic_page():
    cf = open(utils.get_pkg_root() / "doc/sal_generics.rst", "w")
    write_heading(cf, "SAL Generics", char="*", overline=True)
    xml_dir = utils.get_sal_interfaces_dir()

    gen_tree = ElementTree.parse(xml_dir / "SALGenerics.xml")
    gen_root = gen_tree.getroot()
    for gen_set in gen_root:
        gen_set_name = gen_set.tag
        topic_type = gen_set_name[3:-3]
        write_heading(cf, name=f"{topic_type}s")
        cf.write("\n")
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
                    cf.write(f"\n.. _{short_name}:{gen_field_name.text}:\n\n")
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
                            cf.write(f":{gen_attribute.tag}: {gen_attribute.text}\n")
                    cf.write(f"\n**Description**: {gen_field_description.text}\n\n")
                elif gen_field.tag in IGNORED_FIELDS:
                    pass
                else:
                    cf.write(f":{gen_field.tag}: {gen_field.text}\n")
                cf.write("\n")
