# This file is part of ts_xml.
#
# Developed for the Rubin Observatory Telescope and Site System.
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

import unittest

from lsst.ts.xml.tables.mtdome import LouverType, find_louver


class MTDomeLouverTableTestCase(unittest.TestCase):
    def test_find_louver(self) -> None:
        """find_louver returns the matching LouverData for known names."""
        louver = find_louver("A1")
        assert louver is not None
        assert louver.index == 0
        assert louver.name == "A1"
        assert louver.azimuth == 53.10
        assert louver.louver_type == LouverType.PART_4511
        assert louver.surface_area == 13.00
        assert louver.actuator_type == "ATL63-950"

        louver = find_louver("N2")
        assert louver is not None
        assert louver.index == 33
        assert louver.name == "N2"
        assert louver.azimuth == 306.90
        assert louver.louver_type == LouverType.PART_4517
        assert louver.surface_area == 5.04
        assert louver.actuator_type == "ATL63-950"

    def test_find_louver_missing_returns_none(self) -> None:
        """find_louver returns None when no louver matches the given name."""
        assert find_louver("Z9") is None


if __name__ == "__main__":
    unittest.main()
