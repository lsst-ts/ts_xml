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
    "ChillerControllerState",
    "ChillerL1Alarms",
    "ChillerL21Alarms",
    "ChillerL22Alarms",
    "ChillerWarnings",
    "LampBasicState",
    "LampControllerError",
    "LampControllerState",
    "ShutterState",
]

import enum


class ChillerControllerState(enum.IntEnum):
    """State of the chiller controller."""

    UNKNOWN = -1
    AUTOSTART = 0
    STANDBY = 1
    RUN = 2
    SAFETY = 3
    TEST = 4


class ChillerL1Alarms(enum.IntFlag):
    """Level 1 chiller alarms.

    Notes
    -----
    These codes are from ThermoTek manual "TTK Serial Communication Protocol
    Release II", specifically from a table in the ALARMS & WARNINGS section.

    Unfortunately, the table is published in order left-most alarm char first.
    In order to make it easier to transcribe the table, the CSC code
    reverses the alarm code string before parsing it as a hex integer.
    In other words if the chiller reports alarm state "123ABC"
    the CSC reports this as 0xCBA321.
    This was a difficult decision, but it proved very awkward to transcribe
    the table entries in the order needed to avoid reversing the alarm
    state string.
    """

    AMBIENT_TEMP_SENSOR = 0x1
    HIGH_CONTROL_TEMP = 0x2
    PT7_HIGH_TEMP = 0x4
    LOW_CONTROL_TEMP = 0x8

    SUPPLY_TEMP_SENSOR = 0x10
    EXTERNAL_RTD_SENSOR = 0x20
    RETURN_TEMP_SENSOR = 0x40
    EXTERNAL_THERMISTOR_SENSOR = 0x80

    LOW_COOLANT_LEVEL = 0x100
    LOW_COOLANT_FLOW = 0x200
    LOW_PLANT_FLOW = 0x400
    CURRENT_SENSOR_1 = 0x800

    PT7_LOW_TEMP = 0x1000
    HIGH_AMBIENT_TEMP = 0x2000
    LOW_AMBIENT_TEMP = 0x4000
    EXTERNAL_CONNECTOR_NOT_INSTALLED = 0x8000

    DEFAULT_HIGH_TEMP = 0x1_0000
    DEFAULT_LOW_TEMP = 0x2_0000
    NO_COOLANT_FLOW = 0x4_0000
    FAN_FAILURE = 0x8_0000

    CURRENT_SENSOR_2 = 0x10_0000
    INTERNAL_2_5V_REFERENCE = 0x20_0000
    INTERNAL_5V_REFERENCE = 0x40_0000
    SYSTEM_ERROR = 0x80_0000


class ChillerL21Alarms(enum.IntFlag):
    """Level 2-1 chiller alarms.

    See the note in ChillerL1Alarms about provenance and order.
    """

    # not used: 0x01
    # not used: 0x02
    # not used: 0x04
    # not used: 0x08

    ADC_SYSTEM_ERROR = 0x10
    I2C_SYSTEM_ERROR = 0x20
    EEPROM_SYSTEM_ERROR = 0x40
    WATCHDOG_SYSTEM_ERROR = 0x80

    # not used: 0x100
    # not used: 0x200
    # not used: 0x400
    # not used: 0x800

    ADC_RESET_ERROR = 0x1000
    ADC_CALIBRATION_ERROR = 0x2000
    ADC_CONVERSION_ERROR = 0x4000
    # not used: 0x8000

    IO_EXPENDER_ACKNOWLEDGE_ERROR = 0x1_0000
    PSA_EXPENDER_ACKNOWLEDGE_ERROR = 0x2_0000
    RTC_ACKNOWLEDGE_ERROR = 0x4_0000
    # not used: 0x8_0000

    I2C_SCL_LOW_ERROR = 0x10_0000
    I2C_SDA_LOW_ERROR = 0x20_0000
    EEPROM_1_ACKNOWLEDGE = 0x40_0000
    EEPROM_2_ACKNOWLEDGE = 0x80_0000

    # not used: 0x100_0000
    # not used: 0x200_0000
    # not used: 0x400_0000
    # not used: 0x800_0000

    EEPROM_1_READ_ERROR = 0x1000_0000
    EEPROM_1_WRITE_ERROR = 0x2000_0000
    EEPROM_2_READ_ERROR = 0x4000_0000
    EEPROM_2_WRITE_ERROR = 0x8000_0000


class ChillerL22Alarms(enum.IntFlag):
    """Level 2-2 chiller alarms.

    See the note in ChillerL1Alarms about provenance and order.
    """

    EXTERNAL_RTD_SENSOR_OPEN = 0x1
    EXTERNAL_RTD_SENSOR_SHORT = 0x2
    RETURN_TEMP_SENSOR_OPEN = 0x4
    RETURN_TEMP_SENSOR_SHORT = 0x8

    GLOBAL_TEMP_SENSOR = 0x10
    SUPPLY_TEMP_SENSOR_LOCKED = 0x20
    SUPPLY_TEMP_SENSOR_OPEN = 0x40
    SUPPLY_TEMEPRATURE_SENSOR_SHORT = 0x80

    INTERNAL_2_5V_REFERENCE_HIGH = 0x100
    INTERNAL_2_5V_REFERENCE_LOW = 0x200
    INTERNAL_5V_REFERENCE_HIGH = 0x400
    INTERNAL_5V_REFERENCE_LOW = 0x800

    EXTERNAL_THERMAL_SENSOR_OPEN = 0x1000
    EXTERNAL_THERMAL_SENSOR_SHORT = 0x2000
    AMBIENT_THERMAL_SENSOR_OPEN = 0x4000
    AMBIENT_THERMAL_SENSOR_SHORT = 0x8000

    # not used: 0x1_0000
    # not used: 0x2_0000
    # not used: 0x4_0000
    # not used: 0x8_0000

    CURRENT_SENSOR_1_OPEN = 0x10_0000
    CURRENT_SENSOR_1_SHORT = 0x20_0000
    CURRENT_SENSOR_2_OPEN = 0x40_0000
    CURRENT_SENSOR_2_SHORT = 0x80_0000

    REAR_LEFT_FAN_NOISE = 0x100_0000
    REAR_RIGHT_FAN_NOISE = 0x200_0000
    FRONT_LEFT_FAN_NOISE = 0x400_0000
    FRONT_RIGHT_FAN_NOISE = 0x800_0000

    REAR_LEFT_FAN_OPEN = 0x1000_0000
    REAR_RIGHT_FAN_OPEN = 0x2000_0000
    FRONT_LEFT_FAN_OPEN = 0x4000_0000
    FRONT_RIGHT_FAN_OPEN = 0x8000_0000


class ChillerWarnings(enum.IntFlag):
    """Chiller warnings.

    See the note in ChillerL1Alarms about provenance and order.
    """

    LOW_COOLANT_FLOW = 0x1
    COOLANT_FLUID_LEVEL = 0x2
    SWITCH_TO_SUPPLY_TEMP_AS_CONTROL_TEMP = 0x4
    # not used: 0x8

    HIGH_CONTROL_TEMP = 0x10
    LOW_CONTROL_TEMP = 0x20
    HIGH_AMBIENT_TEMP = 0x40
    LOW_AMBIENT_TEMP = 0x80


class LampBasicState(enum.IntEnum):
    """Lamp basic state.

    Meanings:

    * UNKNOWN: no connection to the lamp controller and not COOLDOWN.
    * OFF: lamp is off and fully cooled down.
      You can turn it on again or turn off the chiller.
    * ON: lamp is on and fully ignited and warmed up.
      You can adjust its power and turn it off.
    * COOLDOWN: lamp is off but cannot be turned back on yet.
      The chiller must remain operating.
      This is solely based on a timer internal to the CSC; that timer
      is typically longer than the lamp controller's cooldown phase,
      which is described in LampControllerState.
    * WARMUP: lamp is on, but not fully warmed up.
      You cannot turn the lamp off unless you specify force=True,
      which will shorten bulb life.
    * TURNING_ON: lamp has been turned off for less than
      configured max_lamp_on_delay seconds and light is not detected.
      This is a normal phase of turning on the lamp.
    * TURNING_OFF: lamp has been turned off for less than
      configured max_lamp_off_delay seconds and light is still detected.
      This is a normal phase of turning off the lamp.
    * UNEXPECTEDLY_ON: lamp has been turned off for more than
      configured max_lamp_off_delay seconds and light is still detected.
      This is very bad: the lamp controller is probably stuck on.
    * UNEXPECTEDLY_OFF: lamp has been turned on for more than
      configured max_lamp_on_delay seconds and light is not detected.
      This is bad: the lamp probably burned out or failed to turn on.
    """

    UNKNOWN = 0
    OFF = 1
    ON = 2
    COOLDOWN = 3
    WARMUP = 4
    TURNING_ON = 5
    TURNING_OFF = 6
    UNEXPECTEDLY_ON = 7
    UNEXPECTEDLY_OFF = 8


class LampControllerError(enum.IntEnum):
    """Errors reported by the lamp controller.

    Values 1-8 match the number of flashes of the error LED.
    Until the flashes have been counted the error will be UNKNOWN.

    A value of UNKNOWN indicates that the CSC has not finished counting
    the number of flashes, or the number was not a recognized value.
    """

    NONE = -1
    UNKNOWN = 0
    KILL_SWITCH = 1
    CHASSIS_OVERHEATING = 2
    ACCESS_DOOR = 3
    BALLAST_OVERHEATING = 4
    USB_DISCONNECTED = 5
    AIRFLOW_INADEQUATE = 6
    LAMP_STUCK_ON = 7
    AIRFLOW_MALFUNCTION = 8


class LampControllerState(enum.IntEnum):
    """Lamp controller state.

    Values:

    * UNKNOWN: Not connected to the lamp controller or the lamp controller
      is powered off.
    * STANDBY_OR_ON: Either the lamp is on, or it has been off long enough
      that the lamp controller's short COOLDOWN phase is over.
      The main LED is green.
    * COOLDOWN: The main LED is blue. The lamp was recently turned off and
      the lamp controller is cooling down. This is different than the CSC's
      cooldown phase, whose duration is set by config.lamp.cooldown_period.
      The lamp controller's cooldown phase is not configurable, but it is
      typically much shorter than the CSC's cooldown phase. It indicates
      that a fan is running.
    * ERROR: The lamp controller is reporting an error.
      The main LED is red and the error LED should be flashing.
    """

    UNKNOWN = 0
    STANDBY_OR_ON = 1
    COOLDOWN = 2
    ERROR = 3


class ShutterState(enum.IntEnum):
    """Shutter state."""

    UNKNOWN = 0
    CLOSED = 1
    OPEN = 2
    INVALID = 3
