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

__all__ = ["LouverData", "LouverTable", "LouverType", "find_louver"]


class LouverType(enum.StrEnum):
    """Louver type identifier. The enum value is the manufacturer part
    number. See EIE-DWG-45-10-00-00.
    """

    PART_4511 = "45-11-00-00"
    PART_4512 = "45-12-00-00"
    PART_4513 = "45-13-00-00"
    PART_4514 = "45-14-00-00"
    PART_4515 = "45-15-00-00"
    PART_4516 = "45-16-00-00"
    PART_4517 = "45-17-00-00"
    PART_4518 = "45-18-00-00"


@dataclass
class LouverData:
    """Represent a single dome louver and its properties.

    Attributes
    ----------
    index : int
        Position of the louver in `LouverTable`, 0 - 33.
    name : str
        Louver name, e.g. "A1", "B2", "N2".
    azimuth : float
        Angular offset (degrees) of the louver normal relative to the dome
        azimuth.
    louver_type : LouverType
        Louver type. The enum value carries the manufacturer part number.
    surface_area : float
        Surface area of the louver in m^2.
    actuator_type : str
        Actuator model used to drive the louver.
    """

    index: int
    name: str
    azimuth: float
    louver_type: LouverType
    surface_area: float
    actuator_type: str


LouverTable = [
    LouverData(0, "A1", 53.10, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(1, "A2", 53.10, LouverType.PART_4517, 5.04, "ATL63-950"),
    LouverData(2, "B1", 67.50, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(3, "B2", 67.50, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(4, "B3", 67.50, LouverType.PART_4514, 9.03, "ATL63-800"),
    LouverData(5, "C1", 95.50, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(6, "C2", 95.50, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(7, "C3", 95.50, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(8, "D1", 120.75, LouverType.PART_4512, 9.87, "ATL63-950"),
    LouverData(9, "D2", 120.75, LouverType.PART_4512, 9.87, "ATL63-950"),
    LouverData(10, "D3", 120.75, LouverType.PART_4512, 9.87, "ATL63-950"),
    LouverData(11, "E1", 120.75, LouverType.PART_4512, 9.87, "ATL63-950"),
    LouverData(12, "E2", 120.75, LouverType.PART_4512, 9.87, "ATL63-950"),
    LouverData(13, "E3", 120.75, LouverType.PART_4513, 6.59, "ATL63-950"),
    LouverData(14, "F1", 180.00, LouverType.PART_4518, 2.97, "ATL63-950"),
    LouverData(15, "F2", 180.00, LouverType.PART_4515, 11.61, "ATL63-950"),
    LouverData(16, "F3", 180.00, LouverType.PART_4516, 7.21, "ATL63-800"),
    LouverData(17, "G1", 180.00, LouverType.PART_4518, 2.97, "ATL63-950"),
    LouverData(18, "G2", 180.00, LouverType.PART_4515, 11.61, "ATL63-950"),
    LouverData(19, "G3", 180.00, LouverType.PART_4516, 7.21, "ATL63-800"),
    LouverData(20, "H1", 239.25, LouverType.PART_4512, 9.87, "ATL63-950"),
    LouverData(21, "H2", 239.25, LouverType.PART_4512, 9.87, "ATL63-950"),
    LouverData(22, "H3", 239.25, LouverType.PART_4513, 6.59, "ATL63-950"),
    LouverData(23, "I1", 239.25, LouverType.PART_4512, 9.87, "ATL63-950"),
    LouverData(24, "I2", 239.25, LouverType.PART_4512, 9.87, "ATL63-950"),
    LouverData(25, "I3", 239.25, LouverType.PART_4512, 9.87, "ATL63-950"),
    LouverData(26, "L1", 264.50, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(27, "L2", 264.50, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(28, "L3", 264.50, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(29, "M1", 292.50, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(30, "M2", 292.50, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(31, "M3", 292.50, LouverType.PART_4514, 9.03, "ATL63-800"),
    LouverData(32, "N1", 306.90, LouverType.PART_4511, 13.00, "ATL63-950"),
    LouverData(33, "N2", 306.90, LouverType.PART_4517, 5.04, "ATL63-950"),
]


def find_louver(name: str) -> LouverData | None:
    """Return LouverData with the given louver name.

    Parameters
    ----------
    name : str
        Louver name, e.g. "A1".

    Returns
    -------
    louver : LouverData | None
        LouverData associated with the given name, or None if no louver
        with that name exists.
    """
    try:
        return next(louver for louver in LouverTable if louver.name == name)
    except StopIteration:
        return None
