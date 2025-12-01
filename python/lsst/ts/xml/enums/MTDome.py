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
    "AzimuthMotor",
    "AzimuthMotorSensor",
    "Brake",
    "CabinetSensor",
    "ControlMode",
    "EnabledState",
    "Louver",
    "MotionState",
    "OnOff",
    "OpenClose",
    "OperationalMode",
    "PowerManagementMode",
    "RadLockingPinState",
    "SubSystemId",
]

import enum


class AzimuthMotor(enum.IntEnum):
    """Azimuth motor."""

    Motor1 = 1
    Motor2 = 2
    Motor3 = 3
    Motor4 = 4
    Motor5 = 5


class AzimuthMotorSensor(enum.IntEnum):
    """Azimuth motor sensor."""

    Sensor1Motor1_104T4 = 1
    Sensor2Motor1_104T5 = 2
    Sensor1Motor2_104T6 = 3
    Sensor2Motor2_104T7 = 4
    Sensor1Motor3_106T1 = 5
    Sensor2Motor3_106T2 = 6
    Sensor1Motor4_106T3 = 7
    Sensor2Motor4_106T4 = 8
    Sensor1Motor5_106T5 = 9
    Sensor2Motor5_106T6 = 10


class Brake(enum.IntEnum):
    """Engagable brakes.

    Each item represents multiple brakes that are always engaged at the same
    time.
    """

    AMCS = 1
    APSCS_LEFT_DOOR = 2
    APSCS_RIGHT_DOOR = 3
    LWSCS = 4
    LOUVER_A1 = 5
    LOUVER_A2 = 6
    LOUVER_B1 = 7
    LOUVER_B2 = 8
    LOUVER_B3 = 9
    LOUVER_C1 = 10
    LOUVER_C2 = 11
    LOUVER_C3 = 12
    LOUVER_D1 = 13
    LOUVER_D2 = 14
    LOUVER_D3 = 15
    LOUVER_E1 = 16
    LOUVER_E2 = 17
    LOUVER_E3 = 18
    LOUVER_F1 = 19
    LOUVER_F2 = 20
    LOUVER_F3 = 21
    LOUVER_G1 = 22
    LOUVER_G2 = 23
    LOUVER_G3 = 24
    LOUVER_H1 = 25
    LOUVER_H2 = 26
    LOUVER_H3 = 27
    LOUVER_I1 = 28
    LOUVER_I2 = 29
    LOUVER_I3 = 30
    LOUVER_L1 = 31
    LOUVER_L2 = 32
    LOUVER_L3 = 33
    LOUVER_M1 = 34
    LOUVER_M2 = 35
    LOUVER_M3 = 36
    LOUVER_N1 = 37
    LOUVER_N2 = 38
    CSCS = 39
    RAD_LEFT_DOOR = 40
    RAD_RIGHT_DOOR = 41


class CabinetSensor(enum.IntEnum):
    """Cabinet sensor."""

    Sensor1_104T1 = 1
    Sensor2_104T2 = 2
    Sensor3_104T3 = 3


class ControlMode(enum.IntEnum):
    """Control mode."""

    Remote = 1
    LocalPushButtons = 2
    LocalKeba = 3
    LocalEui = 4


class EnabledState(enum.IntEnum):
    """Drive enabled state."""

    DISABLED = 1
    ENABLED = 2
    FAULT = 3


class Louver(enum.IntEnum):
    """Louver name and associated array index."""

    A1 = 1
    A2 = 2
    B1 = 3
    B2 = 4
    B3 = 5
    C1 = 6
    C2 = 7
    C3 = 8
    D1 = 9
    D2 = 10
    D3 = 11
    E1 = 12
    E2 = 13
    E3 = 14
    F1 = 15
    F2 = 16
    F3 = 17
    G1 = 18
    G2 = 19
    G3 = 20
    H1 = 21
    H2 = 22
    H3 = 23
    I1 = 24
    I2 = 25
    I3 = 26
    L1 = 27
    L2 = 28
    L3 = 29
    M1 = 30
    M2 = 31
    M3 = 32
    N1 = 33
    N2 = 34


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
    # Technically speaking these next states are regarded intermediary states,
    # but they are added here to avoid too much hassle dealing with two enums.
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
    FINAL_LOW_CLOSE_LS_ENGAGED = enum.auto()
    FINAL_LOW_OPEN_LS_ENGAGED = enum.auto()
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


class OpenClose(enum.StrEnum):
    """Aperture shutter home command OPEN or CLOSE direction."""

    OPEN = "OPEN"
    CLOSE = "CLOSED"


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
    # Software Control System
    CONTROL = 0x400
