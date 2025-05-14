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
# the Free Software Foundation either version 3 of the License or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""M1 radius in m."""
M1_R = 4.1988

"""M3 Radius in m."""
M3_R = 2.5337

"""Radisu of center hole in m."""
CENTER_HOLE_R = 1.0547 / 2.0

from .fa_table import (
    FATABLE_XFA,
    FATABLE_YFA,
    FATABLE_ZFA,
    HP_COUNT,
    FAIndex,
    FAOrientation,
    FASubnet,
    FATable,
    FAType,
    ForceActuatorData,
    actuator_id_to_index,
    force_actuator_from_id,
)
from .fcu_table import FCUData, FCUTable, fcu_from_address, fill_m1_m3
from .thermocouple_table import (
    Level,
    Scanner,
    ThermocoupleData,
    ThermocoupleTable,
    find_thermocouple,
)
