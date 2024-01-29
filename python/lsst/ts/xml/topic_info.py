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

__all__ = ["make_ackcmd_topic_info", "TopicInfo"]

import dataclasses
import hashlib
import json
import typing
from xml.etree import ElementTree

from .field_info import FieldInfo
from .sal_topic_utils import find_optional_text, find_required_text
from .type_hints import BaseMsgType

_PRIVATE_FIELD_LIST = [
    FieldInfo(
        name="salIndex",
        description="SAL index (only present for indexed SAL components)",
        count=1,
        sal_type="long",
        units="unitless",
    ),
    FieldInfo(
        name="private_sndStamp",
        description="Time of instance publication",
        count=1,
        sal_type="double",
        units="second",
    ),
    FieldInfo(
        name="private_rcvStamp",
        description="Time of instance reception",
        count=1,
        sal_type="double",
        units="second",
    ),
    FieldInfo(
        name="private_efdStamp",
        description="UTC time for EFD timestamp. "
        "An integer (the number of leap seconds) "
        "different from private_sndStamp.",
        count=1,
        sal_type="double",
        units="second",
    ),
    FieldInfo(
        name="private_kafkaStamp",
        description="TAI time at which the Kafka message was created.",
        count=1,
        sal_type="double",
        units="second",
    ),
    FieldInfo(
        name="private_seqNum",
        description="Sequence number",
        count=1,
        sal_type="long",
        units="unitless",
    ),
    FieldInfo(
        name="private_revCode",
        description="Revision hashcode",
        count=1,
        sal_type="string",
        units="unitless",
    ),
    FieldInfo(
        name="private_identity",
        description="Identity of publisher: "
        "SAL component name for a CSC or user@host for a user",
        count=1,
        sal_type="string",
        units="unitless",
    ),
    FieldInfo(
        name="private_origin",
        description="Process ID of publisher",
        count=1,
        sal_type="long",
        units="unitless",
    ),
]
# Dict of field_name: FieldInfo for all private fields
# (including salIndex, which is only present for indexed components).
PRIVATE_FIELDS = {info.name: info for info in _PRIVATE_FIELD_LIST}

_ACKCMD_FIELDS_LIST = [
    FieldInfo(
        name="ack",
        description="Acknowledgement code",
        count=1,
        sal_type="long",
        units="unitless",
    ),
    FieldInfo(
        name="error",
        description="An error code; only relevant if ack=FAILED",
        count=1,
        sal_type="long",
        units="unitless",
    ),
    FieldInfo(
        name="result",
        description="Message",
        count=1,
        sal_type="string",
        units="unitless",
    ),
    FieldInfo(
        name="identity",
        description="private_identity field of the command being acknowledged",
        count=1,
        sal_type="string",
        units="unitless",
    ),
    FieldInfo(
        name="origin",
        description="private_origin field of the command being acknowledged",
        count=1,
        sal_type="long",
        units="unitless",
    ),
    FieldInfo(
        name="cmdtype",
        description="Index of command in alphabetical list of commands, with 0 being the first",
        count=1,
        sal_type="long",
        units="unitless",
    ),
    FieldInfo(
        name="timeout",
        description="Estimated remaining duration of command; only relevant if ack=INPROGRESS",
        count=1,
        sal_type="double",
        units="second",
    ),
]
# Dict of field_name: FieldInfo for the public fields of the ackcmd topic
ACKCMD_FIELDS = {info.name: info for info in _ACKCMD_FIELDS_LIST}


def make_ackcmd_topic_info(
    component_name: str,
    topic_subname: str,
    indexed: bool,
    use_simple_schema: bool = False,
) -> TopicInfo:
    """Make an ackcmd topic for a given component.

    Parameters
    ----------
    component_name : `str`
        SAL component name, e.g. MTMount
    topic_subname : `str`
        Sub-namespace for topic names and schema subject and namespace.
    indexed : `str`
        Is this component indexed?

    Returns
    -------
    topic_info : TopicInfo
        Info for the ackcmd topic.
    """
    fields = PRIVATE_FIELDS.copy()
    if not indexed:
        del fields["salIndex"]
    fields.update(ACKCMD_FIELDS)
    return TopicInfo(
        component_name=component_name,
        topic_subname=topic_subname,
        sal_name="ackcmd",
        fields=fields,
        description="Command acknowledgement",
        use_simple_schema=use_simple_schema,
    )


class TopicInfo:
    """Information about one topic.

    Parameters
    ----------
    component_name : `str`
        SAL component name
    topic_subname : `str`
        Sub-namespace for topic names and schema subject and namespace.
    sal_name : `str`
        SAL topic name, e.g. logevent_summaryState
    fields : `dict` [`str`, `FieldInfo`]
        Dict of field name: field info
    description : `str`, optional
        Description of topic.
    partitions : `int`, optional
        Number of Kafka partitions.
        Must be 1 for events, since that makes it easier to get
        reliable historical data.
    use_simple_schema : `bool`, optional
        Use simple schema, without null support for float and double?

    Attributes
    ----------
    attr_name : `str`
        Topic name used by salobj for attributes, e.g. evt_summaryState
    kafka_name : `str`
        Topic name used by Kafka
    avro_subject : `str`
        Subject name for Avro schema
    fields : `dict` [`str`, `FieldInfo`]
        Dict of field name: field info
    array_fields : `dict` [`str`, `int`]
        Dict of field name: array length for array fields
    use_simple_schema : `bool`
        Use simple schema, without null support for float and double?

    Raises
    ------
    ValueError
        If partitions != 1 for an event,
        or if partitions < 0 for any topic.
    """

    # Cache of (component_name, attr_name): avro schema
    _avro_schema_cache: dict[tuple[str, str], dict[str, typing.Any]] = dict()

    # Cache of (component_name, attr_name): dataclass
    # This cache is necessary, so that different SalInfo instances
    # have the same data classes.
    _dataclass_cache: dict[tuple[str, str], typing.Type[BaseMsgType]] = dict()

    def __init__(
        self,
        component_name: str,
        topic_subname: str,
        sal_name: str,
        fields: dict[str, FieldInfo],
        description: str = "",
        partitions: int = 1,
        use_simple_schema: bool = False,
    ) -> None:
        if partitions != 1 and sal_name.startswith("logevent_"):
            raise ValueError(
                f"invalid partitions={partitions} for sal_name={sal_name}: "
                "must be 1 for events"
            )
        if partitions < 1:
            raise ValueError(
                f"invalid partitions={partitions} for sal_name={sal_name}: "
                "must be > 0"
            )

        self.component_name = component_name
        self.topic_subname = topic_subname
        self.sal_name = sal_name
        self.fields = fields
        self.description = description
        self.partitions = partitions
        self.use_simple_schema = use_simple_schema

        if sal_name == "ackcmd":
            attr_name = "ack_ackcmd"
        elif sal_name.startswith("logevent_"):
            attr_name = "evt_" + sal_name[9:]
        elif sal_name.startswith("command_"):
            attr_name = "cmd_" + sal_name[8:]
        else:
            attr_name = "tel_" + sal_name
        self.attr_name = attr_name
        self.kafka_name = (
            f"lsst.{self.topic_subname}.{self.component_name}.{self.sal_name}"
        )
        self.avro_subject = f"{self.kafka_name}-value"
        array_fields = dict()
        for field_info in self.fields.values():
            if field_info.count > 1:
                array_fields[field_info.name] = field_info.count
        self.array_fields = array_fields
        self._cache_key = (self.component_name, self.attr_name)

    @classmethod
    def from_xml_element(
        cls,
        element: ElementTree.Element,
        component_name: str,
        topic_subname: str,
        indexed: bool,
        use_simple_schema: bool = False,
    ) -> TopicInfo:
        """Construct a TopicInfo from a topic XML element.

        The result includes all info for all fields, including private ones.

        Parameters
        ----------
        element : `ElementTree.Element`
            XML topic element; an of SALCommand, SALEvent, or SALTelemetry.
        component_name : `str`
            SAL component name, e.g. MTMount
        topic_subname : `str`
            Sub-namespace for topic names and schema subject and namespace.
        indexed : `str`
            Is this component indexed?
        use_simple_schema : `bool`, optional
            Use simple schema, without null support for float and double?
        """
        full_name = find_required_text(element, "EFDB_Topic")
        sal_name = full_name.split("_", 1)[1]
        description = find_optional_text(element, "Description", "")

        fields = PRIVATE_FIELDS.copy()
        if not indexed:
            del fields["salIndex"]
        for field_element in element.findall("item"):
            field_info = FieldInfo.from_xml_element(field_element)
            if field_info.name in fields:
                raise RuntimeError(f"field {field_info.name} already found.")
            fields[field_info.name] = field_info
        return cls(
            component_name=component_name,
            topic_subname=topic_subname,
            sal_name=sal_name,
            description=description,
            fields=fields,
            use_simple_schema=use_simple_schema,
        )

    def make_dataclass(self) -> typing.Type[BaseMsgType]:
        """Create a dataclass."""
        dataclass = self._dataclass_cache.get(self._cache_key)

        if dataclass is None:
            field_args = [
                field_info.make_dataclass_tuple() for field_info in self.fields.values()
            ]

            def validate(
                model: typing.Any,
                fields: typing.KeysView[str] = self.fields.keys(),
                array_fields: dict[str, int] = self.array_fields,
            ) -> None:
                """Validate things Kafka does not: array length and str length.

                Parameters
                ----------
                model : dataclass
                    The data
                fields : List [str]
                    Field names
                array_fields : Dict [str, int]
                    Dict of field name: array length for array fields

                Raises
                ------
                ValueError
                    If the data fails validation.
                """
                bad_arrays = [
                    field_name
                    for field_name in fields & array_fields
                    if len(getattr(model, field_name)) != array_fields[field_name]
                ]
                if bad_arrays:
                    raise ValueError(
                        f"Array fields with incorrect length: {bad_arrays}"
                    )

            dataclass = dataclasses.make_dataclass(
                self.attr_name, field_args, namespace={"__post_init__": validate}
            )
            self._dataclass_cache[self._cache_key] = dataclass

        return dataclass

    def make_avro_schema(self) -> dict[str, typing.Any]:
        """Create an avro schema."""
        avro_schema = self._avro_schema_cache.get(self._cache_key)
        if avro_schema is None:
            avro_schema = dict(
                type="record",
                name=self.sal_name,
                namespace=f"lsst.sal.{self.component_name}",
                fields=[
                    field_info.make_avro_schema(self.use_simple_schema)
                    for field_info in self.fields.values()
                ],
                description=self.description,
            )

            self._avro_schema_cache[self._cache_key] = avro_schema

        return avro_schema

    def make_avro_schema_as_json(self) -> str:
        """Convert the avro schema to a json string.

        Returns
        -------
        `str`
            Avro schema as a json formatted string.
        """
        return json.dumps(self.make_avro_schema(), indent=4)

    def get_revcode(self) -> str:
        """Compute the revcode for this topic.

        Returns
        -------
        `str`
            Topic revcode.
        """
        avro_schema = self.make_avro_schema_as_json()
        rev_code = hashlib.md5(avro_schema.encode("utf-8")).hexdigest()[:8]
        return rev_code

    def __repr__(self) -> str:
        return f"TopicInfo({self.kafka_name})"
