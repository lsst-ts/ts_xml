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
# the Free Software Foundation either version 3 of the License or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License

__all__ = [
    "AxisMotionState",
    "Commander",
    "DeployableMotionState",
    "ElevationLockingPinMotionState",
    "LimitsMask",
    "PowerState",
    "System",
    "ThermalCommandState",
    "ParkPosition",
]

import enum


class AxisMotionState(enum.IntEnum):
    """Motion state of azimuth elevation and camera cable wrap."""

    STOPPING = 0
    STOPPED = 1
    MOVING_POINT_TO_POINT = 2
    JOGGING = 3
    TRACKING = 4
    TRACKING_PAUSED = 5


class Commander(enum.IntEnum):
    """Who commands the low-level controller."""

    NONE = 0
    CSC = 1
    EUI = 2
    HDD = 3


class DeployableMotionState(enum.IntEnum):
    """Motion state of deployable systems.

    These include the deployable platform, mirror covers,
    and mirror cover locks.
    """

    RETRACTED = 0
    DEPLOYED = 1
    RETRACTING = 2
    DEPLOYING = 3
    LOST = 4


class ElevationLockingPinMotionState(enum.IntEnum):
    """Position of elevation locking pin."""

    LOCKED = 0
    TEST = 1
    UNLOCKED = 2
    MOVING = 3
    MISMATCH = 4


class LimitsMask(enum.IntFlag):
    """Bit masks for the various limits.

    * L1 = software limit
    * L2 = direction inhibit
    * L3 = cut power

    The ADJUSTABLE_L1 limits apply to the elevation and azimuth axes.
    The OPERATIONAL_L2 limits only apply to the elevation axis.
    These limits may be enabled or disabled, and that is reported in the
    azimuthControllerSettings and elevationControllerSettings events.

    The CAMERA_CABLE_WRAP_FOLLOW_L3 limits protect the cables in the camera
    cable wrap; they detect excessive difference between camera rotator and
    camera cable wrap position. CAMERA_CABLE_WRAP_FOLLOW_L3_MIN means
    the camera cable wrap is too negative compared to the rotator.
    """

    L1_MIN = 0x1
    L1_MAX = 0x2
    L2_MIN = 0x4
    L2_MAX = 0x8
    L3_MIN = 0x10
    L3_MAX = 0x20
    ADJUSTABLE_L1_MIN = 0x40
    ADJUSTABLE_L1_MAX = 0x80
    OPERATIONAL_L2_MIN = 0x100
    OPERATIONAL_L2_MAX = 0x200
    CAMERA_CABLE_WRAP_FOLLOW_L3_MIN = 0x400
    CAMERA_CABLE_WRAP_FOLLOW_L3_MAX = 0x800


class PowerState(enum.IntEnum):
    """Power state of a system or motion controller.

    Also used for motion controller state.

    Note that only a few systems (and no motion controllers)
    use TURNING_ON and TURNING_OFF. The oil supply system is one.
    """

    OFF = 0
    ON = 1
    FAULT = 2
    TURNING_ON = 3
    TURNING_OFF = 4
    UNKNOWN = 15


class System(enum.IntEnum):
    """Subsystem ID: the subsystem field in error and warning events."""

    AZIMUTH = 0
    ELEVATION = 1
    CAMERA_CABLE_WRAP = 2
    BALANCE = 3
    MIRROR_COVERS = 4
    MIRROR_COVER_LOCKS = 5
    AZIMUTH_CABLE_WRAP = 6
    LOCKING_PINS = 7
    DEPLOYABLE_PLATFORMS = 8
    OIL_SUPPLY_SYSTEM = 9
    AZIMUTH_DRIVES_THERMAL = 10
    ELEVATION_DRIVES_THERMAL = 11
    CABINET_0101_THERMAL = 12
    AZ0101_CABINET_THERMAL = 12  # deprecated alias
    AUXILIARY_CABINETS_THERMAL = 13
    MODBUS_TEMPERATURE_CONTROLLERS = 13  # deprecated alias
    MAIN_CABINET_THERMAL = 14
    MAIN_AXES_POWER_SUPPLY = 15
    TOP_END_CHILLER = 16


class ThermalCommandState(enum.IntEnum):
    """State for the setThermal command."""

    NO_CHANGE = 0
    OFF = 1
    ON = 2


class ParkPosition(enum.IntEnum):
    """Park positions."""

    ZENITH = enum.auto()
    HORIZON = enum.auto()
