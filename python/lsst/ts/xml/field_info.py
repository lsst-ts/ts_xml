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

__all__ = ["FieldInfo"]

import dataclasses
import typing
from xml.etree import ElementTree

from .sal_topic_utils import find_optional_text, find_required_text

# Dict of SAL type: python type
PYTHON_TYPES = {
    "boolean": bool,
    "byte": int,
    "short": int,
    "int": int,
    "long": int,
    "long long": int,
    "unsigned short": int,
    "unsigned int": int,
    "float": float,
    "double": float,
    "string": str,
}

# Dict of SAL type: Avro type
# SAL-long (this is 4 byte integer) -> AVRO-int: 32-bit signed integer
# SAL-long long (8 byte integer) -> AVRO-long: 64-bit signed integer
# AVRO has no unsigned types so all unsigned values are converted to the
# signed equivalent.
AVRO_TYPES = {
    "boolean": "boolean",
    "byte": "int",
    "short": "int",
    "int": "int",
    "long": "int",
    "long long": "long",
    "unsigned short": "int",
    "unsigned int": "long",
    "float": ["float", "null"],
    "double": ["double", "null"],
    "string": "string",
}


@dataclasses.dataclass
class FieldInfo:
    """Information about one field of a topic.

    Parameters
    ----------
    name : `str`
        Field name
    sal_type : `str`
        SAL data type.
    count : `int`
        For arrays: the number of elements. Specify 1 for scalars.
    units : `str`
        Units, "unitless" if none.
    description : `str`
        Description (arbitrary text)

    Attributes
    ----------
    default_scalar_value : `typing.Any`
        For a scalar: the default value.
        For an array: the default value of one element.
    """

    name: str
    sal_type: str
    count: int = 1
    units: str = "unitless"
    description: str = ""
    default_scalar_value: typing.Any = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        if self.sal_type == "string":
            if self.count > 1:
                # string fields cannot be arrays; emulate ts_sal
                # and ignore count > 1 for string fields
                self.count = 1
        python_type = PYTHON_TYPES[self.sal_type]
        self.default_scalar_value = python_type()

    @classmethod
    def from_xml_element(cls, element: ElementTree.Element) -> FieldInfo:
        """Construct a FieldInfo from an XML element."""
        name = find_required_text(element, "EFDB_Name")
        description = find_optional_text(element, "Description", "")
        count = int(find_optional_text(element, "Count", "1"))
        units = find_optional_text(element, "Units", "unitless")
        sal_type = find_required_text(element, "IDL_Type")
        return FieldInfo(
            name=name,
            sal_type=sal_type,
            count=count,
            units=units,
            description=description,
        )

    def make_dataclass_tuple(
        self,
    ) -> tuple[str, typing.Type[typing.Any], dataclasses.Field]:
        """Create field data for topic_info.make_dataclasses."""
        scalar_type = PYTHON_TYPES[self.sal_type]
        if self.count > 1:
            dtype: typing.Type[typing.Any] = list[scalar_type]  # type: ignore
            field: dataclasses.Field = dataclasses.field(
                default_factory=lambda: [self.default_scalar_value] * self.count  # type: ignore
            )
        else:
            dtype = scalar_type
            field = dataclasses.field(default=self.default_scalar_value)
        return (self.name, dtype, field)

    def make_avro_schema(self) -> dict[str, typing.Any]:
        """Return an Avro schema for this field."""
        scalar_type = AVRO_TYPES[self.sal_type]
        if self.count > 1:
            avro_type: typing.Any = {"type": "array", "items": scalar_type}
            default: typing.Any = [self.default_scalar_value] * self.count
        else:
            avro_type = scalar_type
            default = self.default_scalar_value
        return dict(
            name=self.name,
            type=avro_type,
            default=default,
            description=self.description,
            units=self.units,
        )
