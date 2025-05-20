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

import typing
import unittest

from lsst.ts.xml.tables.m1m3 import FAIndex, FATable, FCUTable, fill_m1_m3
from pytest import approx


class M1M3FATableTestCase(unittest.TestCase):
    def assert_sorted(
        self, gen: typing.Generator[int, None, None], array: list[int]
    ) -> None:
        a1 = list(gen)
        a1.sort()
        self.assertEqual(a1, array)

    def test_neighbors(self) -> None:
        item = FATable[4]

        self.assert_sorted(
            item.near_neighbors_indices(FAIndex.Z), [3, 5, 10, 11, 125, 126]
        )
        self.assert_sorted(item.near_neighbors_indices(FAIndex.Y), [2, 7, 81])

        self.assert_sorted(
            item.far_neighbors_indices(FAIndex.Y), [2, 6, 7, 13, 80, 81, 86]
        )
        self.assert_sorted(item.only_far_neighbors_indices(FAIndex.Y), [6, 13, 80, 86])

        item2 = FATable[11]
        self.assert_sorted(item2.near_neighbors_indices(FAIndex.X), [])
        self.assert_sorted(item2.only_far_neighbors_indices(FAIndex.X), [9])

    def test_quadrant(self) -> None:
        assert FATable[1].quadrant == 1
        assert FATable[45].quadrant == 2
        assert FATable[155].quadrant == 4

    def test_distance_fa(self) -> None:
        assert FATable[1].distance(FATable[1]) == 0
        assert FATable[0].distance(FATable[144]) == approx(2.90, 0.01)

    def test_center_distance_fcu(self) -> None:
        assert FCUTable[1].center_distance() == approx(3.78, 0.01)
        assert FCUTable[95].center_distance() == approx(3.96, 0.01)

    def test_fcu_is_m1_m3(self) -> None:
        assert FCUTable[1].is_m1() is True
        assert FCUTable[42].is_m1() is False

        assert FCUTable[94].is_m3() is False
        assert FCUTable[41].is_m3() is True

    def test_fill_m1_m3(self) -> None:
        data = fill_m1_m3(1, 2)
        for fcu in FCUTable:
            assert data[fcu.index] == 1 if fcu.is_m1() else 2


if __name__ == "__main__":
    unittest.main()
