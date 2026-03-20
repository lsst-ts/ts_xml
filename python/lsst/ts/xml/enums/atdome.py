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

__all__ = [
    "AzimuthCommandedState",
    "AzimuthState",
    "ShutterDoorCommandedState",
    "ShutterDoorState",
]

import enum


class AzimuthCommandedState(enum.IntEnum):
    UNKNOWN = 1
    GOTOPOSITION = 2
    HOME = 3
    STOP = 4


class AzimuthState(enum.IntEnum):
    NOTINMOTION = 1
    MOVINGCW = 2
    MOVINGCCW = 3


class ShutterDoorCommandedState(enum.IntEnum):
    UNKNOWN = 1
    CLOSED = 2
    OPENED = 3
    STOP = 4


class ShutterDoorState(enum.IntEnum):
    CLOSED = 1
    OPENED = 2
    PARTIALLYOPENED = 3
    OPENING = 4
    CLOSING = 5
