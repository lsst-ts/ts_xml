__all__ = ["LaserDetailedState", "OpticalConfiguration", "LaserErrorCode"]
import enum


class LaserDetailedState(enum.IntEnum):
    """An enumeration class for handling the TunableLaser's substates.

    These enumerations listed here correspond to the ones found in the
    detailedState enum located in ts_xml under the TunableLaser folder within
    the TunableLaser_Events.xml.

    Attributes
    ----------

    NONPROPAGATING_CONTINUOUS_MODE: `int`
        Corresponds to the nonpropgating state when in continuous mode
    NONPROPAGATING_BURST_MODE: `int`
        Corresponds to the nonpropgating state when in burst mode
    PROPAGATING_CONTINUOUS_MODE : `int`
        Corresponds to the propagating state when in continuous mode
    PROPAGATING_BURST_MODE : `int`
        Corresponds to the propagating state when in burst mode

    """

    NONPROPAGATING_CONTINUOUS_MODE = 1
    NONPROPAGATING_BURST_MODE = 2
    PROPAGATING_CONTINUOUS_MODE = 3
    PROPAGATING_BURST_MODE = 4


class OpticalConfiguration(enum.StrEnum):
    """Configuration of the optical output

    Attributes
    ----------

    SCU: `str`
        Pass the beam straight-through the SCU.
    F1_SCU: `str`
        Direct the beam through the F1 after passing through the SCU.
    F2_SCU: `str`
        Direct the beam through the F2 after passing through the SCU.
    NO_SCU: `str`
        Pass the beam straight-through.
    F1_NO_SCU: `str`
        Pass the beam to F1 output.
    F2_NO_SCU: `str`
        Pass the beam to F2 output.

    """

    SCU = "SCU"
    F1_SCU = "F1 SCU"
    F2_SCU = "F2 SCU"
    NO_SCU = "No SCU"
    F1_NO_SCU = "F1 No SCU"
    F2_NO_SCU = "F2 No SCU"


class LaserErrorCode(enum.IntEnum):
    """Laser error codes"""

    ASCII_ERROR = 7301
    GENERAL_ERROR = 7302
    TIMEOUT_ERROR = 7303
    HW_CPU_ERROR = 7304
