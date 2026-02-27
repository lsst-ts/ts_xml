__all__ = ["DetailedState", "ErrorCode"]

import enum


class DetailedState(enum.IntEnum):
    NOTMOVINGSTATE = 1
    MOVINGSTATE = 2


class ErrorCode(enum.IntEnum):
    """Error codes that indicate why the CSC went to fault state."""

    CONNECTION_FAILED = 1
    """Connection to the device failed."""
    DISABLE_MOTOR = 2
    """Disabling the motor failed."""
    ENABLE_MOTOR = 3
    """Enabling the motor failed."""
    HOME = 4
    """Homing the stage failed."""
    MOVE_ABSOLUTE = 5
    """The absolute move failed."""
    MOVE_RELATIVE = 6
    """The relative move failed."""
    POSITION = 7
    """Failed to get the position."""
    TELEMETRY = 8
    """The telemetry loop failed."""
    STOP = 9
