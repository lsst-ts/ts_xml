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
    "OfflineSubstate",
    "EnabledSubstate",
    "FaultSubstate",
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

    STANDBY = 0
    DISABLED = enum.auto()  # Deprecated in rotator
    ENABLED = enum.auto()
    OFFLINE = enum.auto()  # Deprecated in rotator
    FAULT = enum.auto()


class OfflineSubstate(enum.IntEnum):
    """Controller substate for the OFFLINE state.

    Value reported in ``telemetry.offline_substate``.

    This is enum ``OfflineSubStates`` in Moog code.

    Deprecated in the rotator.

    TODO: Remove this after simplifying the state machine in hexapod, DM-39787.
    """

    PUBLISH_ONLY = 0
    AVAILABLE = enum.auto()


class EnabledSubstate(enum.IntEnum):
    """Controller substate for the ENABLED state.

    Value reported in ``telemetry.enabled_substate``.

    This is enum ``EnabledSubStates`` in Moog code.
    """

    STATIONARY = 0
    MOVING_POINT_TO_POINT = enum.auto()
    SLEWING_OR_TRACKING = enum.auto()
    CONTROLLED_STOPPING = enum.auto()
    INITIALIZING = enum.auto()  # Deprecated in rotator
    RELATIVE = enum.auto()  # Deprecated in rotator
    CONSTANT_VELOCITY = enum.auto()


class FaultSubstate(enum.IntEnum):
    """Controller substate for the FAULT state.

    Value reported in ``telemetry.fault_substate``.

    This is enum ``FaultSubStates`` in Simulink model.
    """

    EMERGENCY_STOPPING = 0
    WAIT_CLEAR_ERROR = enum.auto()
    NO_ERROR = enum.auto()


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
    """

    CONTROLLER_FAULT = 1
    CONNECTION_LOST = 2
    NO_CONFIG = 3
