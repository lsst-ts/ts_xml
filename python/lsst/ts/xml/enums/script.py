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

__all__ = ["ScriptState", "MetadataCoordSys", "MetadataRotSys", "MetadataDome"]

import enum


class ScriptState(enum.IntEnum):
    """ScriptState constants."""

    UNKNOWN = 0
    UNCONFIGURED = 1
    CONFIGURED = 2
    RUNNING = 3
    PAUSED = 4
    ENDING = 5
    STOPPING = 6
    FAILING = 7
    DONE = 8
    STOPPED = 9
    FAILED = 10
    CONFIGURE_FAILED = 11


class MetadataCoordSys(enum.IntEnum):
    """Constants for the Script metadata.coordinateSystem event field"""

    NONE = 1
    ICRS = 2
    OBSERVED = 3
    MOUNT = 4


class MetadataRotSys(enum.IntEnum):
    """Constants for the Script metadata.rotationSystem event field"""

    NONE = 1
    SKY = 2
    HORIZON = 3
    MOUNT = 4


class MetadataDome(enum.IntEnum):
    """Constants for the Script metadata.dome event field"""

    CLOSED = 1
    OPEN = 2
    EITHER = 3
