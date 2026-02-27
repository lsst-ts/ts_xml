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
    "OfflineDetailedState",
    "ImageReadinessDetailedState",
    "CalibrationDetailedState",
    "ShutterDetailedState",
    "CCSCommandState",
    "RaftsDetailedState",
    "CCDType",
]

import enum


class OfflineDetailedState(enum.IntEnum):
    AVAILABLE = 1
    PUBLISH_ONLY = 2


class ImageReadinessDetailedState(enum.IntEnum):
    READY = 1
    NOT_READY = 2
    GETTING_READY = 3


class CalibrationDetailedState(enum.IntEnum):
    DISABLED = 1
    ENABLED = 2
    INTEGRATING = 3


class ShutterDetailedState(enum.IntEnum):
    CLOSED = 1
    OPEN = 2
    CLOSING = 3
    OPENING = 4


class CCSCommandState(enum.IntEnum):
    IDLE = 1
    BUSY = 2


class RaftsDetailedState(enum.IntEnum):
    NEEDS_CLEAR = 1
    CLEARING = 2
    INTEGRATING = 3
    READING_OUT = 4
    QUIESCENT = 5


class CCDType(enum.IntEnum):
    E2V = 1
    ITL = 2
