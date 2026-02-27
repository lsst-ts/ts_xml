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
    "Camera",
    "CameraServerMode",
    "DomeTargetState",
    "DomeState",
    "HeaterState",
    "PeltierState",
    "Warning",
    "Error",
    "Weather",
]


import enum


class Camera(enum.IntEnum):
    East = 0
    West = 1
    North = 2
    Central = 3
    South = 4


class CameraServerMode(enum.IntEnum):
    Auto = 0
    Idle = 1
    Standby = 2
    Blanks = 3
    Bias = 4
    Flats = 5
    Darks = 6
    Science = 7
    Shutdown = 8


class DomeTargetState(enum.IntEnum):
    Auto = 0
    Open = 1
    Closed = 2
    Stop = 3
    ForceOpen = 4


class DomeState(enum.IntEnum):
    Open = 0
    Closed = 1
    Opening = 2
    Closing = 3
    Stop = 4


class HeaterState(enum.IntEnum):
    Auto = 0
    On = 1
    Off = 2
    Unknown = 3


class PeltierState(enum.IntEnum):
    Auto = 0
    Cool = 1
    Heat = 2
    Off = 3
    Unknown = 4


class Warning(enum.IntFlag):
    PowersavingActivated = 0x01
    UpsOnBattery = 0x02
    DomeClosedByNogo = 0x04
    DomeClosedBySun = 0x08
    DomeClosedByEnv = 0x10
    DomeClosedByUps = 0x20
    DomeClosedByTimer = 0x40
    DomeStopped = 0x80
    DomeForcedOped = 0x100
    DomeClosedByDoor = 0x200
    RubinNoClient = 0x400
    RubinMultipleClients = 0x800
    RubinClientStale = 0x1000
    RubinWeatherTooOld = 0x2000
    RubinBadWeather = 0x4000
    RubinNogo = 0x8000
    ScriptClientActive = 0x10000
    InletHumWarning = 0x20000
    InletTempWarning = 0x40000
    CameraNNotConnected = 0x80000
    CameraSNotConnected = 0x100000
    CameraENotConnected = 0x200000
    CameraWNotConnected = 0x400000
    CameraCNotConnected = 0x800000
    SimulatedDome = 0x1000000
    SimulatedLeds = 0x2000000
    SimulatedUps = 0x4000000
    SimulatedPdu = 0x8000000
    SimulatedEnv = 0x10000000
    SimulatedSun = 0x20000000


class Error(enum.IntFlag):
    LimitSwitchError = 0x01
    DomeError = 0x02
    BackdoorOpen = 0x04
    DoorOpen = 0x08
    UpsError = 0x10
    Pdu1Error = 0x20
    Pdu2Error = 0x40
    TemphumError = 0x80
    PsuError = 0x100
    UpsBatteryNeedsReplace = 0x200
    CameraBayTempError = 0x400
    CameraBayHumError = 0x800
    ElectronicsHumidityError = 0x1000
    DomeHumidityError = 0x2000


class Weather(enum.IntFlag):
    WeatherBad = 0x001
    WindBad = 0x002
    HumidityBad = 0x004
    PrecipitationBad = 0x008
