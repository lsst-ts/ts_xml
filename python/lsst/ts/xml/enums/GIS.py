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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

__all__ = ["Subsystem"]

import enum


class Subsystem(enum.Enum):
    GISCPUINPUTS = enum.auto
    GISCPUOUTPUTS = enum.auto
    GISCPURESERVE = enum.auto
    ACCESSFIREEARTHQUAKEINPUTS = enum.auto
    ACCESSFIREEARTHQUAKEOUTPUTS = enum.auto
    ACCESSFIREEARTHQUAKEFREE = enum.auto
    LASERINPUTS = enum.auto
    LASEROUTPUTS = enum.auto
    LASERFREE = enum.auto
    M2INPUTS = enum.auto
    M2OUTPUTS = enum.auto
    M2FREE = enum.auto
    PFLOWINPUTS = enum.auto
    PFLOWOUTPUTS = enum.auto
    PFLOWFREE = enum.auto
    AUXCPUINPUTS = enum.auto
    AUXCPUOUTPUTS = enum.auto
    DOMEINPUTS = enum.auto
    DOMEOUTPUTS = enum.auto
    M1M3CPUINPUTS = enum.auto
    M1M3CPUOUTPUTS = enum.auto
    TMACPUINPUTS = enum.auto
    TMACPUOUTPUTS = enum.auto
    SAFETYCAUSESONE = enum.auto
    SAFETYCAUSESTWO = enum.auto
    SAFETYCAUSESONEOVERRIDE = enum.auto
    SAFETYCAUSESTWOOVERRIDE = enum.auto
    SAFETYEFFECTSONE = enum.auto
    SAFETYEFFECTSTWO = enum.auto
