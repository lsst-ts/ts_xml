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

__all__ = [
    "InclinationTelemetrySource",
    "PowerType",
    "PowerSystemState",
    "ClosedLoopControlMode",
    "InnerLoopControlMode",
    "BumpTest",
]

import enum

# Use the same enum of "BumpTest" in MTM1M3
from .MTM1M3 import BumpTest


class InclinationTelemetrySource(enum.IntEnum):
    ONBOARD = 1
    MTMOUNT = 2


class PowerType(enum.IntEnum):
    """Type of the power."""

    Motor = 1
    Communication = 2


class PowerSystemState(enum.IntEnum):
    """State of the power system. This is copied from the ts_mtm2_cell."""

    Init = 1
    PoweredOff = 2
    PoweringOn = 3
    ResettingBreakers = 4
    PoweredOn = 5
    PoweringOff = 6


class ClosedLoopControlMode(enum.IntEnum):
    """Closed loop control mode. This is copied from the ts_mtm2_cell."""

    Idle = 1
    TelemetryOnly = 2
    OpenLoop = 3
    ClosedLoop = 4


class InnerLoopControlMode(enum.IntEnum):
    """Inner-loop control mode. This is copied from the ts_mtm2_cell."""

    Standby = 1
    Disabled = 2
    Enabled = 3
    FirmwareUpdate = 4
    Fault = 5
    ClearFaults = 6
    NoChange = 7
    Unknown = 8
