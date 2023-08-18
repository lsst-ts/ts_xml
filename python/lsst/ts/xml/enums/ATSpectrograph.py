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

__all__ = ["FilterPosition", "DisperserPosition", "Status", "Error", "Port"]

import enum


class FilterPosition(enum.IntEnum):
    FILTER0 = 1
    FILTER1 = 2
    FILTER2 = 3
    FILTER3 = 4
    INBETWEEN = 5


class DisperserPosition(enum.IntEnum):
    DISPERSER0 = 1
    DISPERSER1 = 2
    DISPERSER2 = 3
    DISPERSER3 = 4
    INBETWEEN = 5


class Status(enum.IntEnum):
    HOMING = 1
    MOVING = 2
    STATIONARY = 3
    NOTINPOSITION = 4


class Error(enum.IntEnum):
    NONE = 1
    BUSY = 2
    NOTINITIALIZED = 3
    MOVETIMEOUT = 4


class Port(enum.IntEnum):
    Nasmyth1 = enum.auto()
    Nasmyth2 = enum.auto()
