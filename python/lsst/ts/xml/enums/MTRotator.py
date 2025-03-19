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
    "ControllerState",
    "EnabledSubstate",
    "FaultSubstate",
    "MotionLockState",
    "ApplicationStatus",
    "ErrorCode",
]

import enum


class ControllerState(enum.IntEnum):
    """Controller state reported as ``telemetry.state``.

    The names and meanings are the same as SAL summary states
    but the numeric values are different.

    Value is ``telemetry.state``.

    Called ``States`` in Moog code.
    """

    # Use the following values to be consistent with the Simulink model as the
    # history reason.
    STANDBY = 0
    ENABLED = 2
    FAULT = 4


class EnabledSubstate(enum.IntEnum):
    """Controller substate for the ENABLED state.

    Value reported in ``telemetry.enabled_substate``.

    This is enum ``EnabledSubStates`` in Moog code.
    """

    # Use the following values to be consistent with the Simulink model as the
    # history reason.
    STATIONARY = 0
    MOVING_POINT_TO_POINT = 1
    SLEWING_OR_TRACKING = 2  # hexapod does not have this
    CONTROLLED_STOPPING = 3  # hexapod does not have this
    CONSTANT_VELOCITY = 6  # hexapod does not have this


class FaultSubstate(enum.IntEnum):
    """Controller substate for the FAULT state.

    Value reported in ``telemetry.fault_substate``.

    This is enum ``FaultSubStates`` in Simulink model.
    """

    NO_ERROR = 0
    EMERGENCY_STOPPING = enum.auto()
    WAIT_CLEAR_ERROR = enum.auto()


class MotionLockState(enum.IntEnum):
    """Motion lock state.

    This state is managed entirely by the CSC.
    """

    UNLOCKED = 0
    LOCKING = 1
    UNLOCKING = 2
    LOCKED = 3


class ApplicationStatus(enum.IntFlag):
    """Bit masks for the value reported in ``telemetry.application_status``.

    These are from https://github.com/lsst-ts/ts_rotator_controller/blob/\
main/include/actuatorTlm.h
    """

    EUI_CONNECTED = 0x4
    COMMAND_REJECTED = 0x20
    SAFETY_INTERLOCK = 0x40
    EXTEND_LIMIT_SWITCH = 0x80
    RETRACT_LIMIT_SWITCH = 0x100
    ETHERCAT_PROBLEM = 0x200
    DDS_COMMAND_SOURCE = 0x400
    DDS_CONNECTED = 0x1000
    DRIVE_FAULT = 0x2000
    SIMULINK_FAULT = 0x4000
    ENCODER_FAULT = 0x8000


class ErrorCode(enum.IntEnum):
    """Error codes.

    The values are:

    * CONTROLLER_FAULT: The low-level controller went to fault state.
      Note that the CSC will trigger this if the camera cable wrap is not
      following closely enough, or if a user issues the ``fault`` command.
    * CONNECTION_LOST: The CSC lost communication with the low-level
      controller.
    * NO_CONFIG: The CSC did not receive configuration from the low-level
      controller shortly after connecting to it.
    * NO_NEW_CCW_TELEMETRY: The CSC did not receive new telemetry from the
      camera cable wrapper (CCW) before the timeout.
    * OLD_CCW_TELEMETRY: The CCW telemetry was too old.
    * CCW_FOLLOWING_ERROR: The CCW did not follow the rotator's movement.
    * NO_NEW_TRACK_COMMAND: The CSC did not receive a new track command before
      the timeout.
    * FAIL_TO_LOCK: Fail to lock the rotator motion.
    * FAIL_TO_UNLOCK: Fail to unlock the rotator motion.
    """

    CONTROLLER_FAULT = 1
    CONNECTION_LOST = 2
    NO_CONFIG = 3
    NO_NEW_CCW_TELEMETRY = 4
    OLD_CCW_TELEMETRY = 5
    CCW_FOLLOWING_ERROR = 6
    NO_NEW_TRACK_COMMAND = 7
    FAIL_TO_LOCK = 8
    FAIL_TO_UNLOCK = 9
