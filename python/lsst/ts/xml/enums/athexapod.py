__all__ = ["DetailedState"]

import enum


class DetailedState(enum.IntEnum):
    INMOTION = 1
    NOTINMOTION = 2
