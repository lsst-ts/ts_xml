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

from dataclasses import dataclass

__all__ = ["FCUData", "FCUTable", "fcu_from_address"]


@dataclass
class FCUData:
    index: int
    x_position: float
    y_position: float
    z_position: float
    address: int


FCUTable = [
    FCUData(0, 0.776782776, 0, 0, 1),
    FCUData(1, 1.442567993, 0, 0, 2),
    FCUData(2, 2.10837793, 0, 0, 3),
    FCUData(3, 2.774187988, 0, 0, 4),
    FCUData(4, 3.439998047, 0, 0, 5),
    FCUData(5, 3.968012939, 0, 0, 6),
    FCUData(6, 0.44386499, -0.57660498, 0, 7),
    FCUData(7, 1.109675049, -0.57660498, 0, 8),
    FCUData(8, 1.775484985, -0.57660498, 0, 9),
    FCUData(9, 2.441295898, -0.57660498, 0, 10),
    FCUData(10, 3.107080078, -0.57660498, 0, 11),
    FCUData(11, 3.772891113, -0.57660498, 0, 12),
    FCUData(12, 0, -1.153209961, 0, 13),
    FCUData(13, 0.776782776, -1.153209961, 0, 14),
    FCUData(14, 1.442567993, -1.153209961, 0, 15),
    FCUData(15, 2.10837793, -1.153209961, 0, 16),
    FCUData(16, 2.774187988, -1.153209961, 0, 17),
    FCUData(17, 3.439998047, -1.153209961, 0, 18),
    FCUData(18, 3.9005, -0.997687012, 0, 19),
    FCUData(19, 0.44386499, -1.729819946, 0, 20),
    FCUData(20, 1.109675049, -1.729819946, 0, 21),
    FCUData(21, 1.775484985, -1.729819946, 0, 22),
    FCUData(22, 2.44127002, -1.729819946, 0, 23),
    FCUData(23, 3.107080078, -1.729819946, 0, 24),
    FCUData(24, 3.724452881, -1.517949951, 0, 25),
    FCUData(25, 0, -2.306419922, 0, 26),
    FCUData(26, 0.776782776, -2.306419922, 0, 27),
    FCUData(27, 1.442567993, -2.306419922, 0, 28),
    FCUData(28, 2.10837793, -2.306419922, 0, 29),
    FCUData(29, 2.774187988, -2.306419922, 0, 30),
    FCUData(30, 3.387954102, -2.167409912, 0, 31),
    FCUData(31, 0.44386499, -2.883030029, 0, 32),
    FCUData(32, 1.109675049, -2.883030029, 0, 33),
    FCUData(33, 1.775484985, -2.883030029, 0, 34),
    FCUData(34, 2.44127002, -2.883030029, 0, 35),
    FCUData(35, 2.939364014, -2.745179932, 0, 36),
    FCUData(36, 0.221945206, -3.459629883, 0, 37),
    FCUData(37, 0.88772998, -3.459629883, 0, 38),
    FCUData(38, 1.553540039, -3.267429932, 0, 39),
    FCUData(39, 2.089733887, -3.436389893, 0, 40),
    FCUData(40, 0.365734589, -4.00525, 0, 41),
    FCUData(41, 1.085088013, -3.87276001, 0, 42),
    FCUData(42, 1.60401001, -3.692780029, 0, 43),
    FCUData(43, -0.44386499, -0.57660498, 0, 44),
    FCUData(44, -1.109680054, -0.57660498, 0, 45),
    FCUData(45, -1.77548999, -0.57660498, 0, 46),
    FCUData(46, -2.441300049, -0.57660498, 0, 47),
    FCUData(47, -3.107080078, -0.57660498, 0, 48),
    FCUData(48, -3.772889893, -0.57660498, 0, 49),
    FCUData(49, -0.77678302, -1.153209961, 0, 50),
    FCUData(50, -1.442569946, -1.153209961, 0, 51),
    FCUData(51, -2.108379883, -1.153209961, 0, 52),
    FCUData(52, -2.774189941, -1.153209961, 0, 53),
    FCUData(53, -3.44, -1.153209961, 0, 54),
    FCUData(54, -3.9005, -0.997687012, 0, 55),
    FCUData(55, -0.44386499, -1.729819946, 0, 56),
    FCUData(56, -1.109680054, -1.729819946, 0, 57),
    FCUData(57, -1.77548999, -1.729819946, 0, 58),
    FCUData(58, -2.44127002, -1.729819946, 0, 59),
    FCUData(59, -3.107080078, -1.729819946, 0, 60),
    FCUData(60, -3.724449951, -1.517949951, 0, 61),
    FCUData(61, -0.77678302, -2.306419922, 0, 62),
    FCUData(62, -1.442569946, -2.306419922, 0, 63),
    FCUData(63, -2.108379883, -2.306419922, 0, 64),
    FCUData(64, -2.774189941, -2.306419922, 0, 65),
    FCUData(65, -3.387949951, -2.167409912, 0, 66),
    FCUData(66, -0.44386499, -2.883030029, 0, 67),
    FCUData(67, -1.109680054, -2.883030029, 0, 68),
    FCUData(68, -1.77548999, -2.883030029, 0, 69),
    FCUData(69, -2.44127002, -2.883030029, 0, 70),
    FCUData(70, -2.939360107, -2.745179932, 0, 71),
    FCUData(71, -0.221945007, -3.459629883, 0, 72),
    FCUData(72, -0.88772998, -3.459629883, 0, 73),
    FCUData(73, -1.553540039, -3.267429932, 0, 74),
    FCUData(74, -2.08972998, -3.436389893, 0, 75),
    FCUData(75, -0.365734985, -4.00525, 0, 76),
    FCUData(76, -1.085089966, -3.87276001, 0, 77),
    FCUData(77, -1.60401001, -3.692780029, 0, 78),
    FCUData(78, -0.77678302, 0, 0, 79),
    FCUData(79, -1.442569946, 0, 0, 80),
    FCUData(80, -2.108379883, 0, 0, 81),
    FCUData(81, -2.774189941, 0, 0, 82),
    FCUData(82, -3.44, 0, 0, 83),
    FCUData(83, -3.96801001, 0, 0, 84),
    FCUData(84, -0.44386499, 0.576605408, 0, 85),
    FCUData(85, -1.109680054, 0.576605408, 0, 86),
    FCUData(86, -1.77548999, 0.576605408, 0, 87),
    FCUData(87, -2.441300049, 0.576605408, 0, 88),
    FCUData(88, -3.107080078, 0.576605408, 0, 89),
    FCUData(89, -3.772889893, 0.576605408, 0, 90),
    FCUData(90, 0, 1.15321106, 0, 91),
    FCUData(91, -0.77678302, 1.15321106, 0, 92),
    FCUData(92, -1.442569946, 1.15321106, 0, 93),
    FCUData(93, -2.108379883, 1.15321106, 0, 94),
    FCUData(94, -2.774189941, 1.15321106, 0, 95),
    FCUData(95, -3.44, 1.15321106, 0, 96),
]


def fcu_from_address(address: int) -> FCUData:
    return next(fcu for fcu in FCUTable if fcu.address == address)
