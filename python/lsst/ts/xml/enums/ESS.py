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

__all__ = ["ErrorCode"]

from enum import IntEnum


class ErrorCode(IntEnum):
    """Error codes that can be used by the ESS CSC.

    Values:

    * ConnectionFailed: a model could not connect its data server.
      Perhaps the model configuration is wrong or the server is down.
    * ConnectionLost: a model lost its connection to its data server.
    * StartFailed: one or more models failed to start.
    * RunFailed: one or more models failed while running.
    """

    ConnectionFailed = 1
    ConnectionLost = 2
    StartFailed = 3
    RunFailed = 4
