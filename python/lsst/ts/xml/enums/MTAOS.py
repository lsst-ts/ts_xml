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

__all__ = ["Mode", "FilterType", "ClosedLoopState"]

import enum


class Mode(enum.IntEnum):
    """MTAOS wavefront sensing mode.

    1 - LSST Camera full array mode.
    2 - LSST Camera corner wavefront sensors.
    3 - ComCam full array mode

    """

    LsstCamFAM = 1
    LsstCamCWS = enum.auto()
    ComCam = enum.auto()


class FilterType(enum.IntEnum):
    u = 1
    g = enum.auto()
    r = enum.auto()
    i = enum.auto()
    z = enum.auto()
    y = enum.auto()
    ref = enum.auto()


class ClosedLoopState(enum.IntEnum):
    IDLE = enum.auto()
    WAITING_IMAGE = enum.auto()
    PROCESSING = enum.auto()
    WAITING_APPLY = enum.auto()
    APPLYING_CORRECTION = enum.auto()
    ERROR = enum.auto()
