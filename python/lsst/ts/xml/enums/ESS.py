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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__all__ = ["BatteryStatus", "ErrorCode", "OnOff"]

import enum


class ErrorCode(enum.IntEnum):
    """Error codes that can be used by the ESS CSC.

    Values:

    * ConnectionFailed: a model could not connect its data server.
      Perhaps the model configuration is wrong or the server is down.
    * ConnectionLost: a model lost its connection to its data server.
    * StartFailed: one or more models failed to start.
    * RunFailed: one or more models failed while running.
    """

    ConnectionFailed = 1
    ConnectionLost = 2
    StartFailed = 3
    RunFailed = 4


class BatteryStatus(enum.IntEnum):
    """Battery statuses that can be used by the ESS CSC.

    Values:

    * Charging: The battery is charging.
    * Discharging: The battery is discharging.
    * Floating: The battery is charging to its float voltage.
    * Resting: The battery is fully charged and not
      charging/discharging/floating.
    """

    Charging = 1
    Discharging = 2
    Floating = 3
    Resting = 4


class OnOff(enum.IntEnum):
    """On/Off statuses that can be used by the ESS CSC.

    Values:

    * ON: The device is on.
    * OFF: The device is off.
    """

    ON = 1
    OFF = 2


class M1M3Thermocouple(enum.IntEnum):
    """M1M3 Thermocouple location.

    Values:

    * HONEYCOMB_TOP: Top of the mirror's honeycomb.
    * HONEYCOMB_MIDDLE: Middle in the mirror's honeycomb.
    * HONEYCOMB_BOTTOM: Bottom of the mirror's honeycomb.
    * PLENUM: Air plenum (area between the glass mirror and top of the mirror
      cell, where conditioned air enters).
    * CELL_TOP: Top of the mirror cell.
    * CELL_BOTTOMz: Bottom of the mirror cell.
    """

    HONEYCOMB_TOP = 1
    HONEYCOMB_MIDDLE = 2
    HONEYCOMB_BOTTOM = 3
    PLENUM = 4
    CELL_TOP = 5
    CELL_BOTTOM = 6
