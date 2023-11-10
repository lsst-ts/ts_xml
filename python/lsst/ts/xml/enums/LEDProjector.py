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
    "LEDBasicState",
]

import enum


class LEDBasicState(enum.IntEnum):
    """LED basic state.

    Meanings:

    * UNKNOWN: no connection to the labjack controller.
    * OFF: LED is off.
    * ON: LED is on.
    * ERROR: Any kind of error happening with either switching the LEDs or
        Labjack communication.
    * LABJACK_CONNECTED: Connection established with Labjack.
    * LABJACK_DISCONNECTED: Connection terminated with Labjack.
    """

    UNKNOWN = 0
    OFF = 1
    ON = 2
    ERROR = 3
    LABJACK_CONNECTED = 4
    LABJACK_DISCONNECTED = 5
