# This file is part of ts_xml.
#
# Developed for the Rubin Observatory Telescope and Site System.
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

__all__ = ["SalRetCode", "State", "as_salRetCode", "as_state"]

import enum


class SalRetCode(enum.IntEnum):
    """SAL return codes."""

    OK = 0
    ERR = -1
    ERROR = -1
    ILLEGAL_REVCODE = -2
    TOO_MANY_HANDLES = -3
    NOT_DEFINED = -4
    # Generic State machine states
    STATE_DISABLED = 1
    STATE_ENABLED = 2
    STATE_FAULT = 3
    STATE_OFFLINE = 4
    STATE_STANDBY = 5
    # Timeout return codes
    TIMEOUT = -5
    SIGNAL_INTERRUPT = -6
    # getSample timeout specifiers (+ve is a time in microseconds)
    WAIT_FOR_NEXT_UPDATE = -10000
    WAIT_FOR_CHANGE = -10001
    # telemetry stream update types
    NO_UPDATES = -100
    WAITING_FOR_NEXT = 100
    GOT_UPDATE = 101
    SYNC_IN = 102
    SYNC_OUT = 103
    SYNC_SET = 104
    SYNC_CLEAR = 105
    SYNC_READ = 106
    # generateAlert types
    EVENT_INFO = 200
    EVENT_WARN = -200
    EVENT_ERROR = -201
    EVENT_ABORT = -202
    # issueCommand/getResponse return codes
    CMD_ACK = 300
    CMD_INPROGRESS = 301
    CMD_STALLED = 302
    CMD_COMPLETE = 303
    CMD_NOPERM = -300
    CMD_NOACK = -301
    CMD_FAILED = -302
    CMD_ABORTED = -303
    CMD_TIMEOUT = -304
    # callback types for subscriptions
    DATA_AVAIL = 400
    DEADLINE_MISS = 401
    INCOMPAT_QOS = 402
    SAMPLE_REJ = 403
    LIVELINESS_CHG = 404
    SAMPLELOST = 405
    SUBSCR_MATCH = 406


class State(enum.IntEnum):
    """CSC summaryState constants."""

    OFFLINE = 4
    STANDBY = 5
    DISABLED = 1
    ENABLED = 2
    FAULT = 3


def as_salRetCode(value: int | SalRetCode) -> int | SalRetCode:
    """Convert an int (or SalRetCode) to a SalRetCode.

    Return the original value if no match.
    """
    try:
        return SalRetCode(value)
    except Exception:
        return value


def as_state(value: int | State) -> int | State:
    """Convert an int (or State) to a State.

    Return the original value if no match.
    """
    try:
        return State(value)
    except Exception:
        return value
