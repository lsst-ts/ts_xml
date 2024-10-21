# This file is part of ts_xml.
#
# Developed for Vera Rubin Observatory.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation either version 3 of the License or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import enum
from dataclasses import dataclass

__all__ = [
    "ThermalScanner",
    "ThermocoupleLocation",
    "ThermocoupleData",
    "ThermocoupleTable",
]

"""This module provides location and names for M1M3 thermocouples. Thermocouple
measurements are read by the M1M3 Thermal Scanner CSC.

Attributes
----------
ThermocoupleTable : `[ThermocoupleData]`
"""


class ThermalScanner(enum.IntEnum):
    """Thermal scanner measurement box location."""

    Y_PLUS = 1
    X_PLUS = 2
    Y_MINUS = 3
    X_MINUS = 4


class ThermocoupleLocation(enum.IntEnum):
    """Location of the mirror thermocouple. HC is for the mirror HoneyComb -
    the sensor is located in the glass mirror."""

    HC_BOTTOM = 1
    HC_MIDDLE = 2
    HC_TOP = 3


@dataclass
class ThermocoupleData:
    """Represent thermocouple index, name and location inside the mirror cell.

    Attributes
    ----------
    name : `str`
        Thermocouple name - e.g. MTC017B1.
    location : `ThermocoupleLocation`
        Location type
    scanner : `ThermalScanner`
        Scanner to which is the thermocouple connected.
    port : `int`
        Thermocouple 1-based port. Gives port where the termocouple is
        connected. Shall be integer in range 1-96.
    x_position : `float`
        X position in mirror cell.
    y_position : `float`
        Y position in mirror cell.
    z_position : `float`
        Z position in mirror cell.
    """

    name: str
    location: ThermocoupleLocation
    scanner: ThermalScanner
    port: int
    x_position: float
    y_position: float
    z_position: float


ThermocoupleTable = [
    ThermocoupleData(
        "MTC038B1",
        ThermocoupleLocation.HC_BOTTOM,
        ThermalScanner.Y_PLUS,
        1,
        0.1,
        0.1,
        -0.1,
    ),
    ThermocoupleData(
        "MTC038F", ThermocoupleLocation.HC_TOP, ThermalScanner.Y_PLUS, 2, 0.1, 0.1, 0.1
    ),
]
