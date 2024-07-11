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


class RadLockingPinState(enum.IntEnum):
    """Rear Access Door locking pin state."""

    ENGAGED = 1
    FLOATING = 2
    DISENGAGED = 3


class PowerManagementMode(enum.IntEnum):
    """Power management mode."""

    NO_POWER_MANAGEMENT = 1
    OPERATIONS = 2
    EMERGENCY = 3
    MAINTENANCE = 4


class SubSystemId(enum.IntEnum):
    """SubSystem ID bitmask."""

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
