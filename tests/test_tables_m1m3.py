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

from lsst.ts.xml.tables.m1m3 import FAIndex, FATable


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


if __name__ == "__main__":
    unittest.main()
