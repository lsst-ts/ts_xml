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
    "LogLevel",
    "OffTypes",
    "OnOff",
    "Wraps",
    "CoordFrame",
    "RotFrame",
    "RotMode",
    "Planets",
    "Foci",
    "WarningLevel",
    "DetailedStates",
    "TargetTypes",
    "WrapStrategy",
]

import enum


class TargetInstances(enum.IntEnum):
    CURRENT = 1
    NEXT = 2
    PROSPECTIVE = 3


class LogLevel(enum.IntEnum):
    NONE = 1
    FATAL = 2
    ERROR = 3
    WARNING = 4
    INFO = 5
    DEBUG = 6
    VERBOSE = 7


class OffTypes(enum.IntEnum):
    SIMPLE = 1
    TPLANE = 2


class OnOff(enum.IntEnum):
    ON = 1
    OFF = 2


class Wraps(enum.IntEnum):
    CW = 1
    CCW = 2


class CoordFrame(enum.IntEnum):
    FK5 = 1
    ICRS = 2
    AZEL = 3
    PLANET = 4
    EPHEM = 5


class RotFrame(enum.IntEnum):
    TARGET = 1
    AZEL = 2
    FIXED = 3


class RotMode(enum.IntEnum):
    FIELD = 1
    SLIT = 2


class Planets(enum.IntEnum):
    MERCURY = 1
    VENUS = 2
    MOON = 3
    MARS = 4
    JUPITER = 5
    SATURN = 6
    URANUS = 7
    NEPTUNE = 8
    PLUTO = 9


class Foci(enum.IntEnum):
    PRIME = 1
    NASMYTH1 = 2
    NASMYTH2 = 3


class WarningLevel(enum.IntEnum):
    NONE = 1
    MINOR = 2
    MAJOR = 3


class DetailedStates(enum.IntEnum):
    NOTTRACKING = 1
    AZEL = 2
    OPENLOOP = 3
    GUIDING = 4


class TargetTypes(enum.IntEnum):
    RADEC = 1
    AZEL = 2
    PLANET = 3
    EPHEM = 4


class WrapStrategy(enum.IntEnum):
    """Defines wrap strategy enumeration.

    NOUNWRAP:
        Do not attempt to unwrap azimuth. If target is unreachable,
        reject the command.
    OPTIMIZE:
        Optimize wrap strategy based on ``raDecTarget.timeOnTarget``.
        It will only attempt to unwrap if time available on target is
        smaller then ``raDecTarget.timeOnTarget``.
    MAXTIMEONTARGET:
        Choose the wrap that maximises time on target.
    """

    NOUNWRAP = 1
    OPTIMIZE = 2
    MAXTIMEONTARGET = 3
