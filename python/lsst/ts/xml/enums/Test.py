__all__ = ["Enum", "ValueEnum"]

import enum


class Enum(enum.IntEnum):
    One = enum.auto()
    Two = enum.auto()
    Three = enum.auto()


class ValueEnum(enum.IntFlag):
    Zero = 0
    Two = 2
    Four = 4
    Five = 0x05
