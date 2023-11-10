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

import typing
import unittest

from lsst.ts.xml.component_info import ComponentInfo
from lsst.ts.xml.field_info import AVRO_TYPES, PYTHON_TYPES

#: Generic topic attr names used by the Test SAL component.
GENERIC_TOPICS = {
    "ack_ackcmd",
    "cmd_disable",
    "cmd_enable",
    "cmd_exitControl",
    "cmd_setAuthList",
    "cmd_setLogLevel",
    "cmd_standby",
    "cmd_start",
    "evt_authList",
    "evt_configurationApplied",
    "evt_configurationsAvailable",
    "evt_configurationsAvailable",
    "evt_errorCode",
    "evt_heartbeat",
    "evt_logLevel",
    "evt_logMessage",
    "evt_simulationMode",
    "evt_softwareVersions",
    "evt_summaryState",
}

#: Topic attr names specific to the Test SAL component.
TEST_SPECIFIC_TOPICS = {
    "cmd_fault",
    "cmd_setArrays",
    "cmd_setScalars",
    "cmd_wait",
    "evt_arrays",
    "evt_scalars",
    "tel_arrays",
    "tel_scalars",
}

#: All topic attr names for the Test topic (generic and specific).
ALL_TEST_TOPICS = GENERIC_TOPICS | TEST_SPECIFIC_TOPICS

# Make sure there is no overlap between generic and specific topics
assert GENERIC_TOPICS & TEST_SPECIFIC_TOPICS == set()

#: Generic fields for an indexed SAL component, such as Test.
GENERIC_FIELDS = {
    "private_sndStamp",
    "private_rcvStamp",
    "private_efdStamp",
    "private_kafkaStamp",
    "private_seqNum",
    "private_revCode",
    "private_identity",
    "private_origin",
    "salIndex",
}


# Dict of field name: SAL type (as appears in the XML) for the
# scalars and arrays Test topics: cmd_setArrays, cmd_setScalars,
# evt_arrays, evt_scalars, tel_arrays, and tel_scalars.
ARRAYS_AND_SCALARS_SAL_FIELD_TYPES = dict(
    salIndex="long",
    private_sndStamp="double",
    private_rcvStamp="double",
    private_efdStamp="double",
    private_kafkaStamp="double",
    private_seqNum="long",
    private_revCode="string",
    private_identity="string",
    private_origin="long",
    boolean0="boolean",
    byte0="byte",
    int0="int",
    short0="short",
    long0="long",
    longLong0="long long",
    string0="string",
    unsignedShort0="unsigned short",
    unsignedInt0="unsigned int",
    float0="float",
    double0="double",
)

# List of (attr_name, isarray) for all arrays and scalars topics.
ARRAYS_AND_SCALARS_TOPICS = (
    ("cmd_setArrays", True),
    ("evt_arrays", True),
    ("tel_arrays", True),
    ("cmd_setScalars", False),
    ("evt_scalars", False),
    ("tel_scalars", False),
)

# Set of field names for the scalars Test topics.
SCALARS_FIELD_NAMES = set(ARRAYS_AND_SCALARS_SAL_FIELD_TYPES.keys())

# Set of field names for the arrays Test topics.
ARRAYS_FIELD_NAMES = SCALARS_FIELD_NAMES - {"string0"}


def topic_sal_from_attr_name(attr_name: str) -> str:
    """Get a SAL topic name from a topic attr name."""
    attr_prefix = attr_name[0:4]
    base_name = attr_name[4:]
    sal_prefix = {
        "ack_": "",
        "cmd_": "command_",
        "evt_": "logevent_",
        "tel_": "",
    }[attr_prefix]
    return sal_prefix + base_name


class ComponentInfoTestCase(unittest.TestCase):
    def test_component_info_for_test(self) -> None:
        """Test ComponentInfo for the Test SAL component."""
        topic_subname = "arbitrary_subname"
        component_info = ComponentInfo(name="Test", topic_subname=topic_subname)

        assert component_info.indexed
        assert component_info.name == "Test"
        assert component_info.topic_subname == topic_subname
        assert set(component_info.added_generics) == {
            "mandatory",
            "csc",
            "configurable",
        }
        assert "test" in component_info.description.lower()
        assert set(component_info.topics.keys()) == ALL_TEST_TOPICS
        for attr_name, topic_info in component_info.topics.items():
            with self.subTest(attr_name=attr_name):
                assert topic_info.component_name == "Test"
                assert topic_info.topic_subname == topic_subname
                assert topic_info.attr_name == attr_name
                assert topic_info.sal_name == topic_sal_from_attr_name(attr_name)
                assert isinstance(topic_info.description, str)
                if attr_name in TEST_SPECIFIC_TOPICS:
                    # Some generic topics do not yet have a description.
                    assert topic_info.description != ""
                assert topic_info.partitions >= 1
                assert topic_info.fields.keys() >= GENERIC_FIELDS

    def test_arrays_and_scalars_field_info(self) -> None:
        topic_subname = "arbitrary_subname"
        component_info = ComponentInfo(name="Test", topic_subname=topic_subname)

        # Test field information for the arrays and scalars Test topics.
        for attr_name, isarray in ARRAYS_AND_SCALARS_TOPICS:
            with self.subTest(isarray=isarray, attr_name=attr_name):
                topic_info = component_info.topics[attr_name]
                if isarray:
                    expected_field_names = ARRAYS_FIELD_NAMES
                else:
                    expected_field_names = SCALARS_FIELD_NAMES

                assert topic_info.fields.keys() == expected_field_names
                for field_name, field_info in topic_info.fields.items():
                    assert field_info.name == field_name
                    if field_info.name.endswith("Stamp"):
                        expected_units: str = "second"
                    else:
                        expected_units = "unitless"
                    assert field_info.units == expected_units
                    assert isinstance(field_info.description, str)
                    assert (
                        field_info.sal_type
                        == ARRAYS_AND_SCALARS_SAL_FIELD_TYPES[field_name]
                    )
                    if isarray and field_name.endswith("0"):
                        expected_count = 5
                    else:
                        expected_count = 1
                    assert field_info.count == expected_count

    def test_avro_schemas(self) -> None:
        topic_subname = "arbitrary_subname"
        component_info = ComponentInfo(name="Test", topic_subname=topic_subname)
        avro_schema_dict = component_info.make_avro_schema_dict()
        assert avro_schema_dict.keys() == ALL_TEST_TOPICS
        for attr_name, avro_schema in avro_schema_dict.items():
            topic_info = component_info.topics[attr_name]
            assert avro_schema == topic_info.make_avro_schema()

        for attr_name, isarray in ARRAYS_AND_SCALARS_TOPICS:
            topic_info = component_info.topics[attr_name]
            avro_schema = avro_schema_dict[attr_name]
            assert avro_schema.keys() == {
                "type",
                "name",
                "namespace",
                "fields",
                "description",
            }
            assert avro_schema["type"] == "record"
            assert avro_schema["name"] == topic_sal_from_attr_name(attr_name)
            assert avro_schema["namespace"] == "lsst.sal.Test"
            assert isinstance(avro_schema["description"], str)
            assert avro_schema["description"] != ""
            fields = avro_schema["fields"]
            field_names = {field["name"] for field in fields}
            # Check for duplicate entries in fields
            assert len(field_names) == len(fields)
            if isarray:
                assert field_names == ARRAYS_FIELD_NAMES
            else:
                assert field_names == SCALARS_FIELD_NAMES
            for field in fields:
                assert field.keys() == {
                    "name",
                    "type",
                    "default",
                    "description",
                    "units",
                }
                field_name = field["name"]
                field_info = topic_info.fields[field_name]
                expected_avro_item_type = AVRO_TYPES[field_info.sal_type]
                expected_item_default = dict(
                    string="",
                    boolean=False,
                ).get(field_info.sal_type, 0)
                if isarray and field_name.endswith("0"):
                    expected_type = dict(type="array", items=expected_avro_item_type)
                    expected_default: typing.Any = [expected_item_default] * 5
                else:
                    expected_type = expected_avro_item_type
                    expected_default = expected_item_default
                assert field["type"] == expected_type
                assert field["default"] == expected_default
                assert field["units"] == field_info.units

    def test_topic_info_make_dataclass(self) -> None:
        topic_subname = "arbitrary_subname"
        component_info = ComponentInfo(name="Test", topic_subname=topic_subname)
        for attr_name, isarray in ARRAYS_AND_SCALARS_TOPICS:
            topic_info = component_info.topics[attr_name]
            dataclass = topic_info.make_dataclass()
            assert isinstance(dataclass, type)
            instance = dataclass()
            instance_dict = vars(instance)
            if isarray:
                assert instance_dict.keys() == ARRAYS_FIELD_NAMES
            else:
                assert instance_dict.keys() == SCALARS_FIELD_NAMES
            avro_schema = topic_info.make_avro_schema()
            expected_default_values = {
                field["name"]: field["default"] for field in avro_schema["fields"]
            }
            for field_name, value in instance_dict.items():
                field_info = topic_info.fields[field_name]
                assert value == expected_default_values[field_name]
                expected_python_type = PYTHON_TYPES[field_info.sal_type]
                if isarray and field_name.endswith("0"):
                    assert all(isinstance(item, expected_python_type) for item in value)
                else:
                    assert isinstance(value, expected_python_type)
