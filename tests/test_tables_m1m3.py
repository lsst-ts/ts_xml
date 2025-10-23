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

from lsst.ts.xml.enums.MTM1M3TS import AirNozzle
from lsst.ts.xml.tables.m1m3 import (
    NOZZLES_NUM,
    FAIndex,
    FATable,
    FCUTable,
    Level,
    Scanner,
    ThermocoupleTable,
    calibration_pairs,
    fill_m1_m3,
    find_air_nozzle,
    find_thermocouple,
    set_air_nozzles_types,
)
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

    def test_thermocouple_table(self) -> None:
        assert len([t for t in ThermocoupleTable if t.scanner == Scanner.TS_01]) == 37
        assert len([t for t in ThermocoupleTable if t.scanner == Scanner.TS_02]) == 36
        assert len([t for t in ThermocoupleTable if t.scanner == Scanner.TS_03]) == 37
        assert len([t for t in ThermocoupleTable if t.scanner == Scanner.TS_04]) == 36

        assert len([t for t in ThermocoupleTable if t.level == Level.FRONT]) == 50
        assert len([t for t in ThermocoupleTable if t.level == Level.MIDDLE]) == 26
        assert len([t for t in ThermocoupleTable if t.level == Level.BACK]) == 70

        assert find_thermocouple(Scanner.TS_04, 0) is None
        assert find_thermocouple(Scanner.TS_02, 18) is None

        tc = find_thermocouple(Scanner.TS_01, 37)
        assert tc is not None
        assert tc.index == 8

        tc = find_thermocouple(Scanner.TS_04, 39)
        assert tc is not None
        assert tc.index == 145

        assert find_thermocouple(Scanner.TS_01, 28).is_calibration() is False
        assert find_thermocouple(Scanner.TS_01, 29).is_calibration() is True

        assert find_thermocouple(Scanner.TS_04, 37).is_calibration() is True
        assert find_thermocouple(Scanner.TS_04, 39).is_calibration() is False

        assert len([tc for tc in ThermocoupleTable if tc.is_calibration()]) == 16
        assert len(calibration_pairs()) == 8

        for cp in calibration_pairs():
            assert cp[0].name[:-1] == cp[1].name[:-1]
            assert cp[0].core_location == cp[1].core_location
            assert cp[0].x_position == cp[1].x_position
            assert cp[0].y_position == cp[1].y_position
            assert cp[0].z_position == cp[1].z_position
            assert cp[0].scanner != cp[1].scanner

    def test_air_nozzle_table(self) -> None:
        for sector in "ABCDEF":
            for i in range(1, NOZZLES_NUM + 1):
                cell = find_air_nozzle(f"{sector}{i}")
                assert cell is not None
                assert cell.nozzle == AirNozzle.UNKNOWN
            cell = find_air_nozzle(sector + "300")
            assert cell is None

        class Data:
            nozzlesA = [AirNozzle.SUPER_SHORT] * NOZZLES_NUM
            nozzlesB = [AirNozzle.BLOCKED] * NOZZLES_NUM
            nozzlesC = [AirNozzle.OFFSET] * NOZZLES_NUM
            nozzlesD = [AirNozzle.INSTALLED] * NOZZLES_NUM
            nozzlesE = [AirNozzle.COVERED] * NOZZLES_NUM
            nozzlesF = [AirNozzle.SUPER_SHORT] * NOZZLES_NUM

        set_air_nozzles_types(Data())

        for i in range(1, NOZZLES_NUM + 1):
            assert find_air_nozzle(f"A{i}").nozzle == AirNozzle.SUPER_SHORT
            assert find_air_nozzle(f"B{i}").nozzle == AirNozzle.BLOCKED
            assert find_air_nozzle(f"C{i}").nozzle == AirNozzle.OFFSET
            assert find_air_nozzle(f"D{i}").nozzle == AirNozzle.INSTALLED
            assert find_air_nozzle(f"E{i}").nozzle == AirNozzle.COVERED
            assert find_air_nozzle(f"F{i}").nozzle == AirNozzle.SUPER_SHORT


if __name__ == "__main__":
    unittest.main()
