# This file is part of ts_xml.
#
# Developed for the LSST Telescope & Site.
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
    "DetailedStates",
    "BumpTest",
    "HardpointActuatorMotionState",
    "HardpointTest",
    "ILCState",
]

import enum


class DetailedStates(enum.IntEnum):
    DISABLED = 1
    FAULT = 2
    OFFLINE = 3
    STANDBY = 4
    PARKED = 5
    RAISING = 6
    ACTIVE = 7
    LOWERING = 8
    PARKEDENGINEERING = 9
    RAISINGENGINEERING = 10
    ACTIVEENGINEERING = 11
    LOWERINGENGINEERING = 12
    LOWERINGFAULT = 13
    PROFILEHARDPOINTCORRECTIONS = 14


class BumpTest(enum.IntEnum):
    NOTTESTED = 1
    TESTINGPOSITIVE = 2
    TESTINGPOSITIVEWAIT = 3
    TESTINGNEGATIVE = 4
    TESTINGNEGATIVEWAIT = 5
    PASSED = 6
    FAILED = 7


class HardpointActuatorMotionState(enum.IntEnum):
    STANDBY = 0
    CHASING = 1
    STEPPING = 2
    QUICKPOSITIONING = 3
    FINEPOSITIONING = 4
    WAITINGTENSION = 5


class HardpointTest(enum.IntEnum):
    NOTTESTED = 1
    MOVINGNEGATIVE = 2
    TESTINGPOSITIVE = 3
    TESTINGNEGATIVE = 4
    MOVINGREFERENCE = 5
    PASSED = 6
    FAILED = 7


class ILCState(enum.IntEnum):
    STANDBY = 0
    DISABLED = 1
    ENABLED = 2
    FIRMWAREUPDATE = 3
    FAULT = 4


class EnableDisableForceComponent(enum.IntEnum):
    ACCELERATIONFORCE = 1
    ACTIVEOPTICFORCE = 2
    AZIMUTHFORCE = 3
    BALANCEFORCE = 4
    OFFSETFORCE = 5
    STATICFORCE = 6
    THERMALFORCE = 7
    VELOCITYFORCE = 8


class SetSlewControllerSettings(enum.IntEnum):
    ACCELERATIONFORCES = 1
    BALANCEFORCES = 2
    BOOSTERVALVES = 3
    VELOCITYFORCES = 4
