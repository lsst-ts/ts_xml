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
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
"""WARNING:

As of 2019-10-31 these enumeration values match the values actually output
by the ATPneumatics CSC, but they DO NOT MATCH the enumeration values in
ATPneumatics_Events.xml in ts_xml. The XML file is missing the unwanted
summary states (DISABLED through STANDBY).

Our long range plan is to change the CSC (and these enums) to match
ATPneumatics_Events.xml in ts_xml.
"""

__all__ = ["MirrorCoverState", "CellVentState", "AirValveState", "VentsPosition"]

import enum


class MirrorCoverState(enum.IntEnum):
    DISABLED = 1
    ENABLED = 2
    FAULT = 3
    OFFLINE = 4
    STANDBY = 5
    CLOSED = 6
    OPENED = 7
    INMOTION = 8
    INVALID = 9


class CellVentState(enum.IntEnum):
    DISABLED = 1
    ENABLED = 2
    FAULT = 3
    OFFLINE = 4
    STANDBY = 5
    OPENED = 6
    CLOSED = 7
    INMOTION = 8


class AirValveState(enum.IntEnum):
    DISABLED = 1
    ENABLED = 2
    FAULT = 3
    OFFLINE = 4
    STANDBY = 5
    OPENED = 6
    CLOSED = 7


class VentsPosition(enum.IntEnum):
    OPENED = 0
    CLOSED = 1
    PARTIALLYOPENED = 2
