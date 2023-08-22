__all__ = ["DetailedState"]

import enum


class DetailedState(enum.IntEnum):
    NOTMOVINGSTATE = 1
    MOVINGSTATE = 2
