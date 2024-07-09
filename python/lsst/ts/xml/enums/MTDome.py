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
    "EnabledState",
    "Louver",
    "MotionState",
    "OnOff",
    "OperationalMode",
    "PowerManagementMode",
    "RadLockingPinState",
    "ResponseCode",
    "SubSystemId",
]

import enum


class EnabledState(enum.IntEnum):
    """Drive enabled state."""

    DISABLED = 1
    ENABLED = 2
    FAULT = 3


class Louver(enum.IntEnum):
    """Louver name and associated array index."""

    A1 = 0
    A2 = 1
    B1 = 2
    B2 = 3
    B3 = 4
    C1 = 5
    C2 = 6
    C3 = 7
    D1 = 8
    D2 = 9
    D3 = 10
    E1 = 11
    E2 = 12
    E3 = 13
    F1 = 14
    F2 = 15
    F3 = 16
    G1 = 17
    G2 = 18
    G3 = 19
    H1 = 20
    H2 = 21
    H3 = 22
    I1 = 23
    I2 = 24
    I3 = 25
    L1 = 26
    L2 = 27
    L3 = 28
    M1 = 29
    M2 = 30
    M3 = 31
    N1 = 32
    N2 = 33


class MotionState(enum.IntEnum):
    """Motion state.

    The values are reported by the control software as strings. The control
    software may emit values not present in this enum, which get translated
    into values in this enum by the CSC. One example is STATIONARY which gets
    translated into STOPPED_BRAKED.
    """

    ERROR = enum.auto()
    CLOSED = enum.auto()
    CLOSING = enum.auto()
    CRAWLING = enum.auto()
    MOVING = enum.auto()
    OPEN = enum.auto()
    OPENING = enum.auto()
    PARKED = enum.auto()
    PARKING = enum.auto()
    STOPPED = enum.auto()
    STOPPING = enum.auto()
    STOPPING_BRAKING = enum.auto()
    STOPPED_BRAKED = enum.auto()
    # Technically speaking these next states are regarded intermediary states
    # but they are added here to avoid too much hassle dealing with two enums
    BRAKE_DISENGAGED = enum.auto()
    BRAKES_DISENGAGED = enum.auto()
    BRAKE_ENGAGED = enum.auto()
    BRAKES_ENGAGED = enum.auto()
    DEFLATED = enum.auto()
    DEFLATING = enum.auto()
    DISABLING_MOTOR_POWER = enum.auto()
    DISENGAGING_BRAKE = enum.auto()
    DISENGAGING_BRAKES = enum.auto()
    ENABLING_MOTOR_POWER = enum.auto()
    ENGAGING_BRAKE = enum.auto()
    ENGAGING_BRAKES = enum.auto()
    FINAL_DOWN_CLOSE_LS_ENGAGED = enum.auto()
    FINAL_DOWN_OPEN_LS_ENGAGED = enum.auto()
    FINAL_UP_CLOSE_LS_ENGAGED = enum.auto()
    FINAL_UP_OPEN_LS_ENGAGED = enum.auto()
    GLYCOL_FLOWING = enum.auto()
    GO_DEGRADED = enum.auto()
    GO_NORMAL = enum.auto()
    GO_STATIONARY = enum.auto()
    INCLINED = enum.auto()
    INFLATED = enum.auto()
    INFLATING = enum.auto()
    LP_DISENGAGED = enum.auto()
    LP_DISENGAGING = enum.auto()
    LP_ENGAGED = enum.auto()
    LP_ENGAGING = enum.auto()
    MOTOR_COOLING_OFF = enum.auto()
    MOTOR_COOLING_ON = enum.auto()
    MOTOR_POWER_OFF = enum.auto()
    MOTOR_POWER_ON = enum.auto()
    PROXIMITY_CLOSED_LS_ENGAGED = enum.auto()
    PROXIMITY_OPEN_LS_ENGAGED = enum.auto()
    STARTING_MOTOR_COOLING = enum.auto()
    STOPPING_MOTOR_COOLING = enum.auto()
    UNDETERMINED = enum.auto()
    VERTICAL = enum.auto()
    WAITING_AMCS_STATIONARY = enum.auto()
    DISABLED = enum.auto()
    DISABLING = enum.auto()
    ENABLED = enum.auto()
    ENABLING = enum.auto()


class OnOff(enum.Enum):
    """ON or OFF."""

    ON = True
    OFF = False


class OperationalMode(enum.IntEnum):
    """Operational Modes."""

    NORMAL = 1
    DEGRADED = 2


class PowerManagementMode(enum.IntEnum):
    """Power management mode."""

    NO_POWER_MANAGEMENT = 1
    OPERATIONS = 2
    EMERGENCY = 3
    MAINTENANCE = 4


class RadLockingPinState(enum.IntEnum):
    """Rear Access Door locking pin state."""

    ENGAGED = 1
    FLOATING = 2
    DISENGAGED = 3


class ResponseCode(enum.IntEnum):
    """Response codes.

    The codes mean

        * 0, "OK", "Command received correctly and is being executed."
        * 1, Not used.
        * 2, "Unsupported", "A command was sent that is not supported by the
          lower level component, for instance park is sent to LCS or 'mooveAz'
          instead of 'moveAz' to AMCS."
        * 3, "Incorrect parameter(s)", "The command that was sent is supported
          by the lower level component but the parameters for the command are
          incorrect. This can mean not enough parameters, too many parameters
          or one or more parameters with the wrong name."
        * 4, "Incorrect source", "The current command source is not valid, e.g.
          a remote command arrives while the system is operated in local mode,
          like the push buttons for the Aperture Shutters."
        * 5, "Incorrect state", "The current command cannot be executed in
          current state, e.g. moveAz when the AMCS is in fault state."
        * 6, "Rotating part did not receive", "It was not possible to forward
          the command to the rotating part."
        * 7, "Rotating part did not reply", "The command was sent to the
          rotating part, but it did not send a reply before a timeout."
        * 8, "Duplicate command", "A moveAz command was sent with identical
          parameters as the previously executed one."
    """

    OK = 0
    UNSUPPORTED = 2
    INCORRECT_PARAMETERS = 3
    INCORRECT_SOURCE = 4
    INCORRECT_STATE = 5
    ROTATING_PART_NOT_RECEIVED = 6
    ROTATING_PART_NOT_REPLIED = 7
    DUPLICATE_COMMAND = 8


class SubSystemId(enum.IntEnum):
    """SubSystem ID bitmask."""

    # This is a generic cRIO value.
    CRIO = 0x0
    # Azimuth Motion Control System
    AMCS = 0x1
    # Light and Wind Screen Control System
    LWSCS = 0x2
    # APerture Shutter Control System
    APSCS = 0x4
    # Louvers Control System
    LCS = 0x8
    # THermal Control System
    THCS = 0x10
    # MONitoring Control System
    MONCS = 0x20
    # Rear Access Door
    RAD = 0x40
    # Calibration Screen Control System
    CSCS = 0x80
    # Overhead Bridge Crane
    OBC = 0x100
    # Capacitor Banks Control System
    CBCS = 0x200
