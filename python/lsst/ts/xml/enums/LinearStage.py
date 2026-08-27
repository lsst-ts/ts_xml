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

__all__ = ["DetailedState", "ErrorCode"]

import enum


class DetailedState(enum.IntEnum):
    NOTMOVINGSTATE = 1
    MOVINGSTATE = 2


class ErrorCode(enum.IntEnum):
    """Error codes that indicate why the CSC went to fault state."""

    CONNECTION_FAILED = 1
    """Connection to the device failed."""
    DISABLE_MOTOR = 2
    """Disabling the motor failed."""
    ENABLE_MOTOR = 3
    """Enabling the motor failed."""
    HOME = 4
    """Homing the stage failed."""
    MOVE_ABSOLUTE = 5
    """The absolute move failed."""
    MOVE_RELATIVE = 6
    """The relative move failed."""
    POSITION = 7
    """Failed to get the position."""
    TELEMETRY = 8
    """The telemetry loop failed."""
    STOP = 9
