# This file is part of ts_xml.
#
# Developed for the LSST Telescope and Site Systems.
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

__all__ = ["Location", "SalIndex", "ScriptProcessState"]

import enum


class Location(enum.IntEnum):
    """Location constants for adding and moving scripts."""

    FIRST = 1
    LAST = 2
    BEFORE = 3
    AFTER = 4


class SalIndex(enum.IntEnum):
    """Allowed SAL indices for the bin scripts.

    The CSC allows other positive values, as well,
    but those should only be used for unit testing.
    """

    MAIN_TEL = 1
    AUX_TEL = 2


class ScriptProcessState(enum.IntEnum):
    """ScriptQueue script.processState event constants."""

    UNKNOWN = 0
    LOADING = 1
    CONFIGURED = 2
    RUNNING = 3
    DONE = 4
    LOADFAILED = 5
    CONFIGURE_FAILED = 6
    TERMINATED = 7
    CONFIGUREFAILED = 6  # deprecated alias for CONFIGURE_FAILED
