__all__ = ["TimeSynchronization"]

import enum


class TimeSynchronization(enum.IntEnum):
    NotStarted = 0
    ResponderWaiting = 1
    ResponderSynced = 2
    ControllerReady = 3
    ControllerRunning = 4
    SynchronizationFailed = 5
