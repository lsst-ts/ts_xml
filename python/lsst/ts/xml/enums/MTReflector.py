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

__all__ = ["MTReflectorStatus"]
import enum


class MTReflectorStatus(enum.IntEnum):
    """An enumeration class for handling the MTReflectorStatus's substates.

    These enumerations listed here correspond to the ones found in the
    detailedState enum located in ts_xml under the MTReflectorStatus
    folder within the MTReflectorStatus_Events.xml.

    Attributes
    ----------
    CONNECTED: `int`
        Corresponds to the state when labjack controller is connected
    DISCONNECTED: `int`
        Corresponds to the state when labjack controller is disconnected
    UNKNOWN : `int`
        Corresponds to the state when labjack controller state is not known
    CONNECTION_ERROR : `int`
        Corresponds to the state when labjack controller has errored

    """

    CONNECTED = 0
    DISCONNECTED = 1
    OPEN = 2
    CLOSE = 3
    UNKNOWN = 4
    CONNECTION_ERROR = 5
