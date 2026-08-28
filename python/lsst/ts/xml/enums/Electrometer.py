# This file is part of ts_xml.
#
# Developed for the Vera C. Rubin Observatory Telescope and Site Systems.
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

__all__ = ["DetailedState", "UnitToRead"]

import enum


class DetailedState(enum.IntEnum):
    DISABLEDSTATE = 1
    ENABLEDSTATE = 2
    FAULTSTATE = 3
    OFFLINESTATE = 4
    STANDBYSTATE = 5
    NOTREADINGSTATE = 6
    CONFIGURINGSTATE = 7
    MANUALREADINGSTATE = 8
    READINGBUFFERSTATE = 9
    SETDURATIONREADINGSTATE = 10


class UnitToRead(enum.IntEnum):
    CURRENT = 1
    CHARGE = 2
    VOLTAGE = 3
    RESISTANCE = 4
