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

__all__ = ["ExposureState", "SalIndex"]

import enum


class ExposureState(enum.IntEnum):
    """The event issued by the FiberSpectrograph CSC when exposures are
    started and/or stopped.
    """

    INTEGRATING = 1
    DONE = 2
    CANCELLED = 3
    TIMEDOUT = 4
    FAILED = 5


class SalIndex(enum.IntEnum):
    """Allowed SAL indices."""

    BLUE = 1
    RED = 2
    BROAD = 3
