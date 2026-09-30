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

__all__ = ["LaserDetailedState", "OpticalConfiguration", "LaserErrorCode"]
import enum


class LaserDetailedState(enum.IntEnum):
    """An enumeration class for handling the TunableLaser's substates.

    These enumerations listed here correspond to the ones found in the
    detailedState enum located in ts_xml under the TunableLaser folder within
    the TunableLaser_Events.xml.

    Attributes
    ----------

    NONPROPAGATING_CONTINUOUS_MODE: `int`
        Corresponds to the nonpropgating state when in continuous mode
    NONPROPAGATING_BURST_MODE: `int`
        Corresponds to the nonpropgating state when in burst mode
    PROPAGATING_CONTINUOUS_MODE : `int`
        Corresponds to the propagating state when in continuous mode
    PROPAGATING_BURST_MODE : `int`
        Corresponds to the propagating state when in burst mode

    """

    NONPROPAGATING_CONTINUOUS_MODE = 1
    NONPROPAGATING_BURST_MODE = 2
    PROPAGATING_CONTINUOUS_MODE = 3
    PROPAGATING_BURST_MODE = 4


class OpticalConfiguration(enum.StrEnum):
    """Configuration of the optical output

    Attributes
    ----------

    SCU: `str`
        Pass the beam straight-through the SCU.
    F1_SCU: `str`
        Direct the beam through the F1 after passing through the SCU.
    F2_SCU: `str`
        Direct the beam through the F2 after passing through the SCU.
    NO_SCU: `str`
        Pass the beam straight-through.
    F1_NO_SCU: `str`
        Pass the beam to F1 output.
    F2_NO_SCU: `str`
        Pass the beam to F2 output.

    """

    SCU = "SCU"
    F1_SCU = "F1 SCU"
    F2_SCU = "F2 SCU"
    NO_SCU = "No SCU"
    F1_NO_SCU = "F1 No SCU"
    F2_NO_SCU = "F2 No SCU"


class LaserErrorCode(enum.IntEnum):
    """Laser error codes"""

    ASCII_ERROR = 7301
    GENERAL_ERROR = 7302
    TIMEOUT_ERROR = 7303
    HW_CPU_ERROR = 7304
