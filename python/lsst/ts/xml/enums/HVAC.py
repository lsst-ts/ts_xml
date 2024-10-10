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

__all__ = [
    "DeviceId",
    "DynaleneState",
    "DynaleneTankLevel",
    "OperatingMode",
    "UnitState",
]

from enum import IntEnum


class DeviceId(IntEnum):
    bombaAguaFriaP01 = 1
    generalP01 = 2
    valvulaP01 = 3
    dynaleneP05 = 4
    glycolSensor = 5
    chiller01P01 = 101
    chiller02P01 = 102
    chiller03P01 = 103
    crack01P02 = 201
    crack02P02 = 202
    fancoil01P02 = 301
    fancoil02P02 = 302
    fancoil03P02 = 303
    fancoil04P02 = 304
    fancoil05P02 = 305
    fancoil06P02 = 306
    fancoil07P02 = 307
    fancoil08P02 = 308
    fancoil09P02 = 309
    fancoil10P02 = 310
    fancoil11P02 = 311
    fancoil12P02 = 312
    manejadoraLower01P05 = 401
    manejadoraLower02P05 = 402
    manejadoraLower03P05 = 403
    manejadoraLower04P05 = 404
    manejadoraSblancaP04 = 501
    manejadoraSlimpiaP04 = 502
    vea01P05 = 601
    vea08P05 = 602
    vea09P05 = 603
    vea10P05 = 604
    vea11P05 = 605
    vea12P05 = 606
    vea13P05 = 607
    vea14P05 = 608
    vea15P05 = 609
    vea16P05 = 610
    vea17P05 = 611
    vea01P01 = 701
    vec01P01 = 702
    vin01P01 = 703
    vex03LowerP04 = 801
    vex04CargaP04 = 802


class DynaleneState(IntEnum):
    """Dynalene state."""

    Initialized = 0
    ShuttingDown = 1
    PoweringOn = 2
    PoweredOn = 3
    PoweringOff = 4
    PoweredOff = 5
    Warning = 6
    Alarm = 7
    ShutOff = 8


class DynaleneTankLevel(IntEnum):
    """Dynalene Tank Level alarm state."""

    OK = 0
    Warning = 1
    Alarm = 2


class OperatingMode(IntEnum):
    """General operating mode."""

    AUTO = 0
    RECOVERY = 1
    CHILLER_RECOVERY = 2
    CHILLER = 3
    HEATPUMP = 4
    UNUSED_1 = 5
    UNUSED_2 = 6
    UNUSED_3 = 7
    CHILLER_FREE_COOLING = 8
    UNUSED_4 = 9
    SUMMER_AUTO = 10
    SUMMER_RECOVERY = 11
    SUMMER_CHILLER_RECOVERY = 12
    SUMMER_CHILLER = 13
    WINTER_HEATPUMP = 14
    WINTER_RECOVERY = 15
    WINTER_AUTO = 16


class UnitState(IntEnum):
    """General state of all units."""

    ON_FROM_KEYBOARD = 0
    ON_FROM_DIGITAL_INPUT = 1
    ON_FROM_TIME_BANDS = 2
    ON_FROM_SUPERVISOR = 3
    OFF_FROM_ALARM = 4
    OFF_FROM_SUPERVISOR = 5
    OFF_FROM_TIME_BANDS = 6
    OFF_FROM_DIGITAL_INPUTS = 7
    OFF_FROM_KEYBOARD = 8
    MANUALL_MODE = 9
    OFF = 10
