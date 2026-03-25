# This file is part of ts_xml.
#
# Developed for the LSST Telescope and Site Systems.
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

__all__ = ["AlarmRuleState"]

import enum


class AlarmRuleState(enum.IntEnum):
    """AlarmRuleState constants."""

    UNKNOWN = 0
    UNCONFIGURED = 1
    CONFIGURING = 2
    CONFIGURED = 3
    RUNNING = 4
    ENDING = 5
    STOPPING = 6
    FAILING = 7
    STOPPED = 8
    FAILED = 9
    CONFIGURE_FAILED = 10
