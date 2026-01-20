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

__all__ = ["ControlFeature"]

import enum


class ControlFeature(enum.IntFlag):
    """EAS control features that can be disabled at runtime.

    Each enumeration is a control in EAS that can be turned on or off.
    """

    ROOM_SETPOINT = 0x1
    """The dome room setpoint controlled by the HVAC AHUs 1-4."""

    AHU = 0x2
    """Enabling/disabling the HVAC AHUs when the dome opens or closes."""

    VEC04 = 0x4
    """The VEC-04 exhaust fan on level 5."""

    GLYCOL_CHILLERS = 0x8
    """The EGW mixture chiller temperature regulated by the HVAC."""

    FANSPEED = 0x10
    """The M1M3 thermal system fan speed.

    This option also controls the tuning of the gap between the EGW temperature
    and heater setpoint in M1M3TS.
    """

    M1M3TS = 0x20
    """All M1M3TS control functions."""

    REQUIRE_DOME_OPEN = 0x40
    """Disable the dome open requirement.

    Applying this setting causes the system always to operate as if the dome
    were open.
    """
