__all__ = ["MTReflectorStatus"]
import enum


class MTReflectorStatus(enum.IntEnum):
    """An enumeration class for handling the MTReflectorStatus's substates.

    These enumerations listed here correspond to the ones found in the
    detailedState enum located in ts_xml under the MTReflectorStatus
    folder within the MTReflectorStatus_Events.xml.

    Attributes
    ----------
    CONNECTED: `int`
        Corresponds to the state when labjack controller is connected
    DISCONNECTED: `int`
        Corresponds to the state when labjack controller is disconnected
    UNKNOWN : `int`
        Corresponds to the state when labjack controller state is not known
    CONNECTION_ERROR : `int`
        Corresponds to the state when labjack controller has errored

    """

    CONNECTED = 0
    DISCONNECTED = 1
    OPEN = 2
    CLOSE = 3
    UNKNOWN = 4
    CONNECTION_ERROR = 5
