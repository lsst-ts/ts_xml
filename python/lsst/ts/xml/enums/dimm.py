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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__all__ = [
    "AmebaMode",
    "ScopeMotion",
    "Dome",
    "AmebaState",
    "ProgramControl",
    "SkyStatus",
]

import enum


class AmebaMode(enum.IntEnum):
    Off = 0
    Auto = 1
    Manual = 2


class ScopeMotion(enum.IntEnum):
    Park = 0
    Slew = 1
    Stand = 2
    Tracking = 3


class Dome(enum.IntEnum):
    Undefined = 0
    Opened = 1
    Closed = 2
    Stated = 3


class AmebaState(enum.IntEnum):
    Inactive = 0
    Waiting = 1
    Slewing = 2
    Tracking = 3
    Focusing = 4
    Monitoring = 5


class ProgramControl(enum.IntEnum):
    Stop = 0
    Start = 1
    Restart = 2
    NoAction = 3


class SkyStatus(enum.IntEnum):
    Clear = 0
    LightCoverage = 1
    Cloudy = 2
    Rain = 3
    Snow = 4
