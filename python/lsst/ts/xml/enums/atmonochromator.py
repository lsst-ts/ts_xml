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
    "Grating",
    "Slit",
    "LightStatus",
    "Device",
    "DetailedState",
    "Status",
    "ErrorCode",
]

import enum


class Grating(enum.IntEnum):
    MIRROR = 0
    RED = 1
    BLUE = 2


class Slit(enum.IntEnum):
    ENTRY = 1
    EXIT = 2


class LightStatus(enum.IntEnum):
    ON = 1
    OFF = 2


class Device(enum.IntEnum):
    MONOCHROMATOR = 1
    LIGHTSOURCE = 2
    THERMOELECTRICCOOLER = 3


class DetailedState(enum.IntEnum):
    NOT_ENABLED = 1
    READY = 2
    CHANGING_WAVELENGTH = 3
    CALIBRATING_WAVELENGTH = 4
    POWERING = 5
    SELECTING_GRATING = 6
    CHANGING_SLIT_WIDTH = 7
    UPDATING_SETUP = 8


class Status(enum.IntEnum):
    SETTING_UP = 0
    READY = 1
    OFFLINE = 2
    FAULT = 3


class ErrorCode(enum.IntEnum):
    """ATMonochromator error codes.

    • CONNECTION_FAILED: could not connect to low-level controller
    • HARDWARE_NOT_READY: low-level controller reported "not ready"
    • HARDWARE_ERROR: low-level controller reported "fault"
    • MISC: other error, probably a communication failure
    """

    CONNECTION_FAILED = 1
    HARDWARE_NOT_READY = 2
    HARDWARE_ERROR = 3
    MISC = 10
