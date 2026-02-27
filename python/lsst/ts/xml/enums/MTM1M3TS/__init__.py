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

import sys
import typing
import warnings

# TODO OSW-1914: Remove this backward compatibility completely.
warnings.simplefilter("default")
warnings.warn(
    f"lsst.ts.xml.enums.MTM1M3TS is deprecated, use lsst.ts.xml.enums.mtm1m3ts instead", 
    DeprecationWarning
)

def __getattr__(name: str) -> typing.Any:
    return getattr(sys.modules["lsst.ts.xml.enums.mtm1m3ts"], name)

