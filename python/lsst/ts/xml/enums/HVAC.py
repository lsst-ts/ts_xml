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
    "DynaleneTankLevel",
    "OperatingMode",
    "UnitState",
]

from enum import IntEnum


class DeviceId(IntEnum):
    glycolChiller03BoosterPump = 1
    ambientFloor1 = 2
    glycolChiller03SwitchValves = 3
    dynalene = 4
    glycolLineSensors = 5
    glycolChiller03SwitchValves01 = 6
    glycolChiller03SwitchValves02 = 7
    coldGlycolRecirculationPump = 8
    coldGlycolChiller01 = 101
    coldGlycolChiller02 = 102
    comfortGlycolChiller03 = 103
    coatingGlycolChiller04 = 104
    comfortGlycolSwitchValvesComputerRoom = 111
    airCompressor01 = 121
    airCompressor02 = 122
    crac01 = 201
    crac02 = 202
    fancoilUnit01ITOffice = 301
    fancoilUnit02BreakRoom = 302
    fancoilUnit03ControlRoom = 303
    fancoilUnit04ControlRoom = 304
    fancoilUnit05ControlRoom = 305
    fancoilUnit06ManagersOffice = 306
    fancoilUnit07SafetyOffice = 307
    fancoilUnit08ElectricalOffice = 308
    fancoilUnit09MeetingRoom = 309
    fancoilUnit10WorkRoom = 310
    fancoilUnit11WorkRoom = 311
    fancoilUnit12CoatingOffice = 312
    airHandlingUnit01Dome = 401
    airHandlingUnit02Dome = 402
    airHandlingUnit03Dome = 403
    airHandlingUnit04Dome = 404
    airHandlingUnit05WhiteRoom = 501
    airHandlingUnit06CleanRoom = 502
    airCirculationFan01Lab = 601
    airCirculationFan08Pier = 602
    airCirculationFan09Pier = 603
    airCirculationFan10Pier = 604
    airCirculationFan11Pier = 605
    airCirculationFan12Pier = 606
    airCirculationFan13Pier = 607
    airCirculationFan14Pier = 608
    airCirculationFan15Pier = 609
    airCirculationFan16Lab = 610
    airCirculationFan17Lab = 611
    airCirculationFan01ElectricalRoom = 701
    airExtractionFan01MRCR = 702
    airIntakeFan01MainBuilding = 703
    airExtractionFan03HighBay = 801
    airExtractionFan04Dome = 802


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
    MANUAL_MODE = 9
    OFF = 10
