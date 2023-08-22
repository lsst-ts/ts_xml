__all__ = [
    "InclinationTelemetrySource",
    "PowerType",
    "PowerSystemState",
    "ClosedLoopControlMode",
    "InnerLoopControlMode",
]

import enum


class InclinationTelemetrySource(enum.IntEnum):
    ONBOARD = 1
    MTMOUNT = 2


class PowerType(enum.IntEnum):
    """Type of the power."""

    Motor = 1
    Communication = 2


class PowerSystemState(enum.IntEnum):
    """State of the power system. This is copied from the ts_mtm2_cell."""

    Init = 1
    PoweredOff = 2
    PoweringOn = 3
    ResettingBreakers = 4
    PoweredOn = 5
    PoweringOff = 6


class ClosedLoopControlMode(enum.IntEnum):
    """Closed loop control mode. This is copied from the ts_mtm2_cell."""

    Idle = 1
    TelemetryOnly = 2
    OpenLoop = 3
    ClosedLoop = 4


class InnerLoopControlMode(enum.IntEnum):
    """Inner-loop control mode. This is copied from the ts_mtm2_cell."""

    Standby = 1
    Disabled = 2
    Enabled = 3
    FirmwareUpdate = 4
    Fault = 5
    ClearFaults = 6
    NoChange = 7
    Unknown = 8
