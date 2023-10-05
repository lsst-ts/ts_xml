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
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License

__all__ = [
    "SalIndex",
    "LaserStatus",
    "AlignComponent",
    "T2SAStatus",
    "Target",
]

import enum


class SalIndex(enum.IntEnum):
    """Allowed SAL indices."""

    MTAlignment = 1
    OTHER = 2


class LaserStatus(enum.IntEnum):
    NOT_CONNECTED = enum.auto()
    OFF = enum.auto()
    WARMING = enum.auto()
    ON = enum.auto()


class AlignComponent(enum.IntEnum):
    M2 = enum.auto()
    Camera = enum.auto()


class T2SAStatus(enum.IntEnum):
    READY = enum.auto()
    TWO_FACE = enum.auto()
    DRIFT = enum.auto()
    BUSY = enum.auto()


class Target(enum.IntEnum):
    M2 = enum.auto()
    M1M3 = enum.auto()
    Camera = enum.auto()
    Dome = enum.auto()
