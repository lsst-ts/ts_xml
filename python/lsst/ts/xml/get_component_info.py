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

__all__ = ["get_component_info"]

import argparse
import json
import pathlib
import shutil
from xml.etree import ElementTree

from . import subsystems
from .component_info import ComponentInfo
from .get_enums_from_xml import get_field_and_global_enums
from .utils import get_sal_interfaces_dir

VALID_COMPONENT_NAMES = set(subsystems)


def get_component_info() -> None:
    """Get information about a SAL component, using the command line."""
    parser = argparse.ArgumentParser(
        description="""Get information about a SAL component.

    Write the information to stdout as a json-encoded dict with three items: {
        "topics": topics
        "global_enums": [global_enum_info],
        "topic_enums": [field_enum_info],
    }, where:
    * topics is a dict: {SAL topic name: topic_info}
    * topic_info is a dict with two items: {
        "avro_schema": Avro schema,
        "array_fields": array_fields_info
      }
    * array_fields_info is a dict: {field name: array length}.
    * global_enum_info is a tuple with 2 items:
      (enum class name: [enum_items]).
    * field_enum_info is a tuple with 3 items:
      (topic name, field name, [enum_info]).
    * enum_info an enum item name with an optional specified value,
      for example: "Enabled", "UNKNOWN=-1", or "LOW_AMBIENT_TEMP = 0x80".

    Write errors to stderr.""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "components",
        nargs="*",
        help="Names of SAL components, e.g. 'Script ScriptQueue'. "
        "Ignored if --all is specified",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Make all components except those listed in --exclude.",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Name of the directory to write the schema files (default=avro-templates).",
        default="avro-templates",
    )
    args = parser.parse_args()

    output_dir = pathlib.PosixPath(args.output)
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    for name in args.components if not args.all else VALID_COMPONENT_NAMES:
        if name not in VALID_COMPONENT_NAMES:
            parser.error(f"Unknown {name=}")

        generate_component_info(name=name, output_dir=output_dir)


def generate_component_info(name: str, output_dir: pathlib.PosixPath) -> None:
    """Generate component info.

    Parameters
    ----------
    name : `str`
        Name of the component.
    output_dir : `pathlib.PosixPath`
        Directory to store component info.
    """
    component_info = ComponentInfo(name=name, topic_subname="")
    field_enums, global_enums = get_field_and_global_enums(name=name)
    result = {
        "topics": {
            topic_info.sal_name: dict(
                avro_schema=topic_info.make_avro_schema_as_json(),
                array_fields=topic_info.array_fields,
            )
            for topic_info in component_info.topics.values()
        },
        "field_enums": [info.as_tuple() for info in field_enums],
        "global_enums": [info.as_tuple() for info in global_enums],
        "hash_table": {
            topic_info.sal_name: topic_info.get_revcode()
            for topic_info in component_info.topics.values()
        },
    }

    component_output_dir = output_dir / name
    if not component_output_dir.exists():
        component_output_dir.mkdir(parents=True)

    for topic in result["topics"]:
        schema_path = component_output_dir / f"{name}_{topic}.json"
        print(f"Writing {schema_path} ...")
        with open(schema_path, "w") as fp:
            assert isinstance(result["topics"], dict)
            avro_schema = result["topics"].get(topic, dict()).get("avro_schema", "")
            fp.write(avro_schema)

    field_enums_dict: dict[str, dict[str, list[str]]] = dict()
    for field_enum in result["field_enums"]:
        topic_name: str = str(field_enum[0])
        field_enum_value: dict[str, list[str]] = field_enum[1]  # type: ignore
        if topic_name in field_enums_dict:
            field_enums_dict[topic_name].update(field_enum_value)
        else:
            field_enums_dict[topic_name] = field_enum_value

    if field_enums_dict:
        field_enums_path = component_output_dir / f"{name}_field_enums.json"
        print(f"Writing {field_enums_path} ...")
        with open(field_enums_path, "w") as fp:
            fp.write(json.dumps(field_enums_dict, indent=4))
    else:
        print(f"No field enumerations for {name}.")

    global_enums_dict: dict[str, str] = dict(result["global_enums"])  # type: ignore
    if global_enums_dict:
        global_enums_path = component_output_dir / f"{name}_global_enums.json"

        print(f"Writing {global_enums_path} ...")
        with open(global_enums_path, "w") as fp:
            fp.write(json.dumps(global_enums_dict, indent=4))
    else:
        print(f"No global enumerations for {name}.")

    # Generate the hash table (table with the rev_code for all topics).
    hash_table_path = component_output_dir / f"{name}_hash_table.json"
    print(f"Writing {hash_table_path} ...")

    with open(hash_table_path, "w") as fp:
        fp.write(json.dumps(result["hash_table"], indent=4))

    # Copy the xml files
    print("Generating xml.")

    sal_interfaces_dir = get_sal_interfaces_dir()

    component_interface_dir = sal_interfaces_dir / name

    for xml_file in component_interface_dir.glob("*.xml"):
        print(f"{xml_file} -> {component_output_dir}")
        shutil.copy(xml_file, component_output_dir)

    # Generate the generics.
    generics = ElementTree.parse(sal_interfaces_dir / "SALGenerics.xml")
    generics_root = generics.getroot()

    for set_index in range(len(generics_root)):
        elements_to_delete = []
        for element in generics_root[set_index]:
            if element.tag == "Enumeration":
                continue
            topic_name_sub_element = element.find("EFDB_Topic")
            assert isinstance(topic_name_sub_element, ElementTree.Element)
            topic_name_str = topic_name_sub_element.text

            category_element = element.find("Category")
            category = (
                category_element.text
                if category_element is not None
                else topic_name_str
            )

            if (
                category not in component_info.added_generics
                and category != "mandatory"
            ):
                elements_to_delete.append(element)

        for element in elements_to_delete:
            generics_root[set_index].remove(element)

        for topic_index in range(len(generics_root[set_index])):
            for attr_index in range(len(generics_root[set_index][topic_index])):
                if generics_root[set_index][topic_index][attr_index].tag in {
                    "Subsystem",
                    "EFDB_Topic",
                }:
                    new_text = generics_root[set_index][topic_index][attr_index].text
                    if new_text is not None:
                        new_text = new_text.replace("SALGeneric", f"{name}")
                        generics_root[set_index][topic_index][
                            attr_index
                        ].text = new_text

    generics.write(
        component_output_dir / f"{name}_Generics.xml",
        encoding="utf-8",
        xml_declaration=True,
    )
