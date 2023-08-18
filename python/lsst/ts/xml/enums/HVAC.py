# This file is part of ts_xml.
#
# Developed for the Vera C. Rubin Observatory Telescope and Site Systems.
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__all__ = [
    "DeviceId",
    "DynaleneState",
    "DynaleneTankLevel",
]

from enum import IntEnum


class DeviceId(IntEnum):
    bombaAguaFriaP01 = 1
    generalP01 = 2
    valvulaP01 = 3
    dynaleneP05 = 4
    chiller01P01 = 101
    chiller02P01 = 102
    chiller03P01 = 103
    crack01P02 = 201
    crack02P02 = 202
    fancoil01P02 = 301
    fancoil02P02 = 302
    fancoil03P02 = 303
    fancoil04P02 = 304
    fancoil05P02 = 305
    fancoil06P02 = 306
    fancoil07P02 = 307
    fancoil08P02 = 308
    fancoil09P02 = 309
    fancoil10P02 = 310
    fancoil11P02 = 311
    fancoil12P02 = 312
    manejadoraLower01P05 = 401
    manejadoraLower02P05 = 402
    manejadoraLower03P05 = 403
    manejadoraLower04P05 = 404
    manejadoraSblancaP04 = 501
    manejadoraSlimpiaP04 = 502
    vea01P05 = 601
    vea08P05 = 602
    vea09P05 = 603
    vea10P05 = 604
    vea11P05 = 605
    vea12P05 = 606
    vea13P05 = 607
    vea14P05 = 608
    vea15P05 = 609
    vea16P05 = 610
    vea17P05 = 611
    vea01P01 = 701
    vec01P01 = 702
    vin01P01 = 703
    vex03LowerP04 = 801
    vex04CargaP04 = 802


class DynaleneState(IntEnum):
    """Dynalene state."""

    Initialized = 0
    ShuttingDown = 1
    PoweringOn = 2
    PoweredOn = 3
    PoweringOff = 4
    PoweredOff = 5
    Warning = 6
    Alarm = 7
    ShutOff = 8


class DynaleneTankLevel(IntEnum):
    """Dynalene Tank Level alarm state."""

    OK = 0
    Warning = 1
    Alarm = 2


# Dict of index: DeviceId, where index is the index of the device in DeviceId.
# Used to understand the bits in the device_ids field of the deviceEnabled
# event.
DeviceIndex = {i: dev_id for i, dev_id in enumerate(DeviceId)}

# Dict grouping MQTT topics representing HVAC devices together.
DEVICE_GROUPS = {
    "CHILLER": [
        "LSST/PISO01/CHILLER_01",
        "LSST/PISO01/CHILLER_02",
        "LSST/PISO01/CHILLER_03",
    ],
    "CRACK": [
        "LSST/PISO02/CRACK01",
        "LSST/PISO02/CRACK02",
    ],
    "DYNALENE": ["LSST/PISO05/DYNALENE"],
    "FANCOIL": [
        "LSST/PISO02/FANCOIL01",
        "LSST/PISO02/FANCOIL02",
        "LSST/PISO02/FANCOIL03",
        "LSST/PISO02/FANCOIL04",
        "LSST/PISO02/FANCOIL05",
        "LSST/PISO02/FANCOIL06",
        "LSST/PISO02/FANCOIL07",
        "LSST/PISO02/FANCOIL08",
        "LSST/PISO02/FANCOIL09",
        "LSST/PISO02/FANCOIL10",
        "LSST/PISO02/FANCOIL11",
        "LSST/PISO02/FANCOIL12",
    ],
    "MANEJADORA_LOWER": [
        "LSST/PISO05/MANEJADORA/LOWER_01",
        "LSST/PISO05/MANEJADORA/LOWER_02",
        "LSST/PISO05/MANEJADORA/LOWER_03",
        "LSST/PISO05/MANEJADORA/LOWER_04",
    ],
    "MANEJADORA": [
        "LSST/PISO04/MANEJADORA/GENERAL/SBLANCA",
        "LSST/PISO04/MANEJADORA/GENERAL/SLIMPIA",
    ],
    "VEA": [
        "LSST/PISO05/VEA_01",
        "LSST/PISO05/VEA_08",
        "LSST/PISO05/VEA_09",
        "LSST/PISO05/VEA_10",
        "LSST/PISO05/VEA_11",
        "LSST/PISO05/VEA_12",
        "LSST/PISO05/VEA_13",
        "LSST/PISO05/VEA_14",
        "LSST/PISO05/VEA_15",
        "LSST/PISO05/VEA_16",
        "LSST/PISO05/VEA_17",
    ],
    "SALA_MAQUINAS": [
        "LSST/PISO01/VEA_01",
        "LSST/PISO01/VIN_01",
        "LSST/PISO01/VEC_01",
    ],
    "VEX": [
        "LSST/PISO04/VEX_03/DAMPER_LOWER/GENERAL",
        "LSST/PISO04/VEX_04/ZONA_CARGA/GENERAL",
    ],
}

# Dict assigning an ID to each device group. This is used in dictionary
# comprehension so it is better to keep it as a dict instead of an enum.
DEVICE_GROUP_IDS = {
    "CHILLER": 100,
    "CRACK": 200,
    "FANCOIL": 300,
    "MANEJADORA_LOWER": 400,
    "MANEJADORA": 500,
    "VEA": 600,
    "SALA_MAQUINAS": 700,
    "VEX": 800,
    "DYNALENE": 900,
}
