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

import enum
from dataclasses import dataclass

__all__ = ["ThermocoupleTable", "find_thermocouple"]


class Scanner(enum.IntEnum):
    """SAL indices for the thermal scanners."""

    TS_01 = 114
    TS_02 = 115
    TS_03 = 116
    TS_04 = 117


class Level(enum.StrEnum):
    FRONT = "F"
    MIDDLE = "M"
    BACK = "B"


@dataclass
class ThermocoupleData:
    """Represent a single thermocouple with all its data.

    Attributes
    ----------
    index : int
    x_position : float
    y_position : float
    z_position : float
    name : str
    scanner : int
    channel : int
    """

    index: int
    x_position: float
    y_position: float
    z_position: float
    name: str
    core_location: str
    scanner: Scanner
    channel: int

    @property
    def level(self) -> Level:
        if self.name[-1].isnumeric():
            return Level(self.name[-2])
        return Level(self.name[-1])

    def is_front(self) -> bool:
        return self.level == Level.FRONT

    def is_middle(self) -> bool:
        return self.level == Level.MIDDLE

    def is_back(self) -> bool:
        return self.level == Level.BACK


ThermocoupleTable = [
    #
    # Thermal Scanner 1
    #
    ThermocoupleData(0, 1.16550, 1.24874, 0.025, "MTC038B1", "F64", Scanner.TS_01, 27),
    ThermocoupleData(1, 1.16550, 1.24874, 0.414, "MTC038F", "F64", Scanner.TS_01, 28),
    ThermocoupleData(2, 2.49710, 2.40198, 0.025, "MTC040B2", "F111", Scanner.TS_01, 29),
    ThermocoupleData(3, 1.670, 2.499, 0.025, "MTC041B1", "F157", Scanner.TS_01, 31),
    ThermocoupleData(4, 1.00404, 2.30642, 0.025, "MTC043B", "F169", Scanner.TS_01, 33),
    ThermocoupleData(5, 1.00404, 2.30642, 0.617, "MTC043F", "F169", Scanner.TS_01, 34),
    ThermocoupleData(6, 1.33444, 2.88303, 0.025, "MTC042B", "F200", Scanner.TS_01, 35),
    ThermocoupleData(7, 1.89106, 3.74709, 0.025, "MTCOW11B", "F228", Scanner.TS_01, 36),
    ThermocoupleData(8, 1.891, 3.747, 0.467, "MTCOW11M", "F228", Scanner.TS_01, 37),
    ThermocoupleData(9, 1.891, 3.747, 0.885, "MTCOW11F", "F228", Scanner.TS_01, 38),
    ThermocoupleData(10, 1.001, 3.267, 0.744, "MTC044F", "F234", Scanner.TS_01, 40),
    ThermocoupleData(12, 0.144, 4.154, 0.025, "MTCOW12B", "F275", Scanner.TS_01, 43),
    ThermocoupleData(13, 0.144, 4.154, 0.467, "MTCOW12M", "F275", Scanner.TS_01, 44),
    ThermocoupleData(14, 0.144, 4.154, 0.885, "MTCOW12F", "F275", Scanner.TS_01, 45),
    ThermocoupleData(15, 0, 0.555, 0.025, "MTCIW1B", "A1", Scanner.TS_01, 1),
    ThermocoupleData(16, 0, 0.555, 0.242, "MTCIW1F", "A1", Scanner.TS_01, 2),
    ThermocoupleData(17, 0, 1.918, 0.025, "MTC001B", "A7", Scanner.TS_01, 3),
    ThermocoupleData(18, 0, 1.918, 0.232, "MTC001M", "A7", Scanner.TS_01, 4),
    ThermocoupleData(19, 0, 1.918, 0.414, "MTC001F", "A7", Scanner.TS_01, 5),
    ThermocoupleData(20, -0.332, 2.499, 0.025, "MTC002B", "A49", Scanner.TS_01, 7),
    ThermocoupleData(21, -0.332, 2.499, 0.617, "MTC002F", "A49", Scanner.TS_01, 8),
    ThermocoupleData(22, -0.993, 3.267, 0.025, "MTC003B", "A127", Scanner.TS_01, 9),
    ThermocoupleData(23, -0.993, 3.267, 0.744, "MTC003F", "A127", Scanner.TS_01, 10),
    ThermocoupleData(24, -1.166, 1.249, 0.025, "MTC007B1", "A133", Scanner.TS_01, 13),
    ThermocoupleData(25, -1.166, 1.249, 0.414, "MTC007F", "A133", Scanner.TS_01, 14),
    ThermocoupleData(26, -1.326, 2.691, 0.025, "MTC004B", "A157", Scanner.TS_01, 15),
    ThermocoupleData(27, -1.498, 2.019, 0.025, "MTC006B", "A169", Scanner.TS_01, 16),
    ThermocoupleData(28, -1.498, 2.019, 0.332, "MTC006M", "A169", Scanner.TS_01, 17),
    ThermocoupleData(29, -1.498, 2.019, 0.617, "MTC006F", "A169", Scanner.TS_01, 18),
    ThermocoupleData(30, -1.831, 2.595, 0.025, "MTC005B", "A200", Scanner.TS_01, 19),
    ThermocoupleData(31, -1.916, 3.682, 0.025, "MTCOW1B", "A205", Scanner.TS_01, 20),
    ThermocoupleData(32, -1.916, 3.682, 0.467, "MTCOW1M", "A205", Scanner.TS_01, 21),
    ThermocoupleData(33, -1.916, 3.682, 0.885, "MTCOW1F", "A205", Scanner.TS_01, 22),
    ThermocoupleData(34, -2.330, 2.499, 0.025, "MTC008B1", "A234", Scanner.TS_01, 24),
    ThermocoupleData(35, -2.330, 2.499, 0.397, "MTC008M", "A234", Scanner.TS_01, 25),
    ThermocoupleData(36, -2.330, 2.499, 0.744, "MTC008F", "A234", Scanner.TS_01, 26),
    #
    # Thermal Scanner 2
    #
    ThermocoupleData(37, -1.166, 1.249, 0.025, "MTC007B2", "A133", Scanner.TS_02, 1),
    ThermocoupleData(38, -2.330, 2.499, 0.025, "MTC008B2", "A234", Scanner.TS_02, 2),
    ThermocoupleData(39, -0.504, 0.286, 0.025, "MTCIW2B", "B1", Scanner.TS_02, 5),
    ThermocoupleData(40, -0.504, 0.286, 0.242, "MTCIW2F", "B1", Scanner.TS_02, 6),
    ThermocoupleData(41, -3.633, 2.009, 0.025, "MTCOW2B", "B19", Scanner.TS_02, 7),
    ThermocoupleData(42, -3.633, 2.009, 0.467, "MTCOW2M", "B19", Scanner.TS_02, 8),
    ThermocoupleData(43, -3.633, 2.009, 0.885, "MTCOW2F", "B19", Scanner.TS_02, 9),
    ThermocoupleData(44, -2.330, -0.961, 0.025, "MTC009B", "B49", Scanner.TS_02, 10),
    ThermocoupleData(45, -2.330, -0.961, 0.617, "MTC009F", "B49", Scanner.TS_02, 11),
    ThermocoupleData(46, -1.829, 0.099, 0.025, "MTC011B", "B102", Scanner.TS_02, 12),
    ThermocoupleData(47, -1.829, 0.099, 0.232, "MTC011M", "B102", Scanner.TS_02, 13),
    ThermocoupleData(48, -1.829, 0.099, 0.414, "MTC011F", "B102", Scanner.TS_02, 14),
    ThermocoupleData(49, -3.324, 0.961, 0.025, "MTC010B", "B111", Scanner.TS_02, 15),
    ThermocoupleData(50, -3.324, 0.961, 0.744, "MTC010F", "B111", Scanner.TS_02, 16),
    ThermocoupleData(51, -2.991, 0.192, 0.025, "MTC012B", "B157", Scanner.TS_02, 17),
    ThermocoupleData(52, -2.491, -0.288, 0.025, "MTC014B", "B169", Scanner.TS_02, 19),
    ThermocoupleData(53, -2.491, -0.288, 0.617, "MTC014F", "B169", Scanner.TS_02, 20),
    ThermocoupleData(54, -3.160, -0.288, 0.025, "MTC013B", "B200", Scanner.TS_02, 21),
    ThermocoupleData(55, -4.138, 0.057, 0.025, "MTCOW3B", "B217", Scanner.TS_02, 22),
    ThermocoupleData(56, -4.138, 0.057, 0.467, "MTCOW3M", "B217", Scanner.TS_02, 24),
    ThermocoupleData(57,-4.138, 0.057, 0.885, "MTCOW3F", "B217", Scanner.TS_02, 25),
    ThermocoupleData(58, -3.326, -0.769, 0.025, "MTC015B", "B234", Scanner.TS_02, 27),
    ThermocoupleData(59, -3.326, -0.769, 0.744, "MTC015F", "B234", Scanner.TS_02, 29),
    ThermocoupleData(60, -3.651, -2.009, 0.025, "MTCOW4B", "B275", Scanner.TS_02, 30),
    ThermocoupleData(61, -3.651, -2.009, 0.467, "MTCOW4M", "B275", Scanner.TS_02, 31),
    ThermocoupleData(62, -3.651, -2.009, 0.885, "MTCOW4F", "B275", Scanner.TS_02, 32),
    ThermocoupleData(63, -0.480, -0.336, 0.025, "MTCIW3B", "C1", Scanner.TS_02, 34),
    ThermocoupleData(64, -0.480, -0.336, 0.146, "MTCIW3M", "C1", Scanner.TS_02, 35),
    ThermocoupleData(65, -0.480, -0.336, 0.242, "MTCIW3F", "C1", Scanner.TS_02, 36),
    ThermocoupleData(66, -1.997, -1.538, 0.025, "MTC016B", "C49", Scanner.TS_02, 37),
    ThermocoupleData(67, -1.997, -1.538, 0.333, "MTC016M", "C49", Scanner.TS_02, 38),
    ThermocoupleData(68, -1.997, -1.538, 0.617, "MTC016F", "C49", Scanner.TS_02, 39),
    ThermocoupleData(69, -1.166, -1.249, 0.025, "MTC017B2", "C64", Scanner.TS_02, 40),
    ThermocoupleData(70, -2.497, 2.402, 0.025, "MTC018B1", "C111", Scanner.TS_02, 41),
    ThermocoupleData(71, -2.497, 2.402, 0.397, "MTC018M", "C111", Scanner.TS_02, 42),
    ThermocoupleData(72, -2.497, 2.402, 0.744, "MTC018F", "C111", Scanner.TS_02, 43),
    #
    # Thermal Scanner 3
    #
    ThermocoupleData(73, -1.166, -1.249, 0.025, "MTC017B1", "C64", Scanner.TS_03, 2),
    ThermocoupleData(74, -1.166, -1.249, 0.414, "MTC017F", "C64", Scanner.TS_03, 3),
    ThermocoupleData(75, -2.497, 2.402, 0.025, "MTC018B2", "C111", Scanner.TS_03, 4),
    ThermocoupleData(76, -1.664, -2.499, 0.025, "MTC019B", "C157", Scanner.TS_03, 5),
    ThermocoupleData(77, -0.993, -2.306, 0.025, "MTC021B", "C169", Scanner.TS_03, 6),
    ThermocoupleData(78, -0.993, -2.306, 0.617, "MTC021F", "C169", Scanner.TS_03, 7),
    ThermocoupleData(79, -0.133, -2.879, 0.025, "MTC020B", "C200", Scanner.TS_03, 8),
    ThermocoupleData(80, -1.855, -3.706, 0.025, "MTCOW5B", "C228", Scanner.TS_03, 9),
    ThermocoupleData(81, -1.855, -3.706, 0.467, "MTCOW5M", "C228", Scanner.TS_03, 10),
    ThermocoupleData(82, -1.855, -3.706, 0.885, "MTCOW5F", "C228", Scanner.TS_03, 11),
    ThermocoupleData(83, -0.996, -3.267, 0.025, "MTC022B", "C234", Scanner.TS_03, 12),
    ThermocoupleData(84, -0.996, -3.267, 0.744, "MTC022F", "C234", Scanner.TS_03, 13),
    ThermocoupleData(85, -0.090, -4.151, 0.025, "MTCOW6B", "C275", Scanner.TS_03, 14),
    ThermocoupleData(86, -0.090, -4.151, 0.467, "MTCOW6M", "C275", Scanner.TS_03, 15),
    ThermocoupleData(87, -0.090, -4.151, 0.885, "MTCOW6F", "C275", Scanner.TS_03, 17),
    ThermocoupleData(88, 0.003, -0.577, 0.025, "MTCIW4B", "D1", Scanner.TS_03, 18),
    ThermocoupleData(89, 0.003, -0.577, 0.242, "MTCIW4F", "D1", Scanner.TS_03, 19),
    ThermocoupleData(90, 0, -1.730, 0.025, "MTC023B", "D7", Scanner.TS_03, 20),
    ThermocoupleData(91, 0, -1.730, 0.232, "MTC023M", "D7", Scanner.TS_03, 21),
    ThermocoupleData(92, 0, -1.730, 0.414, "MTC023F", "D7", Scanner.TS_03, 22),
    ThermocoupleData(93, 0.332, -2.499, 0.025, "MTC024B", "D49", Scanner.TS_03, 23),
    ThermocoupleData(94, 0.332, -2.499, 0.617, "MTC024F", "D49", Scanner.TS_03, 24),
    ThermocoupleData(95, 1.004, -3.267, 0.025, "MTC025B", "D127", Scanner.TS_03, 25),
    ThermocoupleData(96, 1.004, -3.267, 0.744, "MTC025F", "D127", Scanner.TS_03, 26),
    ThermocoupleData(97, 1.171, -1.249, 0.025, "MTC026B1", "D133", Scanner.TS_03, 28),
    ThermocoupleData(98, 1.171, -1.249, 0.414, "MTC026F", "D133", Scanner.TS_03, 30),
    ThermocoupleData(99, 1.337, 2.691, 0.025, "MTC027B", "D157", Scanner.TS_03, 31),
    ThermocoupleData(100, 1.503, -2.018, 0.025, "MTC029B", "D169", Scanner.TS_03, 32),
    ThermocoupleData(101, 1.503, -2.018, 0.333, "MTC029M", "D169", Scanner.TS_03, 33),
    ThermocoupleData(102, 1.503, -2.018, 0.617, "MTC029F", "D169", Scanner.TS_03, 42),
    ThermocoupleData(103, 1.831, -2.595, 0.025, "MTC028B", "D200", Scanner.TS_03, 43),
    ThermocoupleData(104, 1.909, -3.707, 0.025, "MTCOW7B", "D205", Scanner.TS_03, 45),
    ThermocoupleData(105, 1.909, -3.707, 0.467, "MTCOW7M", "D205", Scanner.TS_03, 37),
    ThermocoupleData(106, 1.909, -3.707, 0.885, "MTCOW7F", "D205", Scanner.TS_03, 38),
    ThermocoupleData(107, 2.330, -2.499, 0.025, "MTC030B1", "D234", Scanner.TS_03, 39),
    ThermocoupleData(108, 2.330, -2.499, 0.397, "MTC030M", "D234", Scanner.TS_03, 40),
    ThermocoupleData(109, 2.330, -2.499, 0.744, "MTC030F", "D234", Scanner.TS_03, 41),
    #
    # Thermal scanner 4
    #
    ThermocoupleData(110, 1.171, -1.249, 0.025, "MTC026B2", "D133", Scanner.TS_04, 1),
    ThermocoupleData(111, 2.330, -2.499, 0.025, "MTC030B2", "D234", Scanner.TS_04, 2),
    ThermocoupleData(112, 0.503, -0.282, 0.025, "MTCIW5B", "E1", Scanner.TS_04, 3),
    ThermocoupleData(113, 0.503, -0.282, 0.242, "MTCIW5F", "E1", Scanner.TS_04, 4),
    ThermocoupleData(114, 3.652, -2.003, 0.025, "MTCOW8B", "E19", Scanner.TS_04, 5),
    ThermocoupleData(115, 3.652, -2.003, 0.467, "MTCOW8M", "E19", Scanner.TS_04, 6),
    ThermocoupleData(116, 3.652, -2.003, 0.885, "MTCOW8F", "E19", Scanner.TS_04, 7),
    ThermocoupleData(117, 2.336, -0.980, 0.025, "MTC031B", "E49", Scanner.TS_04, 8),
    ThermocoupleData(118, 2.336, -0.980, 0.617, "MTC031F", "E49", Scanner.TS_04, 9),
    ThermocoupleData(119, 1.836, -0.096, 0.025, "MTC033B", "E102", Scanner.TS_04, 10),
    ThermocoupleData(120, 1.836, -0.096, 0.232, "MTC033M", "E102", Scanner.TS_04, 11),
    ThermocoupleData(121, 1.836, -0.096, 0.414, "MTC033F", "E102", Scanner.TS_04, 13),
    ThermocoupleData(122, 3.334, -0.961, 0.025, "MTC032B", "E111", Scanner.TS_04, 14),
    ThermocoupleData(123, 3.334, -0.961, 0.744, "MTC032F", "E111", Scanner.TS_04, 15),
    ThermocoupleData(124, 3.002, -0.192, 0.025, "MTC034B", "E157", Scanner.TS_04, 16),
    ThermocoupleData(125, 2.497, 0.289, 0.025, "MTC036B", "E169", Scanner.TS_04, 17),
    ThermocoupleData(126, 2.497, 0.289, 0.617, "MTC036F", "E169", Scanner.TS_04, 18),
    ThermocoupleData(127, 3.163, 0.289, 0.025, "MTC035B", "E200", Scanner.TS_04, 19),
    ThermocoupleData(128, 4.137, -0.049, 0.025, "MTCOW9B", "E217", Scanner.TS_04, 20),
    ThermocoupleData(129, 4.137, -0.049, 0.467, "MTCOW9M", "E217", Scanner.TS_04, 21),
    ThermocoupleData(130, 4.137, -0.049, 0.885, "MTCOW9F", "E217", Scanner.TS_04, 22),
    ThermocoupleData(131, 3.328, 0.769, 0.025, "MTC037B", "E234", Scanner.TS_04, 23),
    ThermocoupleData(132, 3.328, 0.769, 0.744, "MTC037F", "E234", Scanner.TS_04, 24),
    ThermocoupleData(133, 3.647, 1.966, 0.025, "MTCOW10B", "E275", Scanner.TS_04, 25),
    ThermocoupleData(134, 3.647, 1.966, 0.467, "MTCOW10M", "E275", Scanner.TS_04, 26),
    ThermocoupleData(135, 3.647, 1.966, 0.885, "MTCOW10F", "E275", Scanner.TS_04, 27),
    ThermocoupleData(136, 0.485, 0.285, 0.025, "MTCIW6B", "F1", Scanner.TS_04, 28),
    ThermocoupleData(137, 0.485, 0.285, 0.146, "MTCIW6M", "F1", Scanner.TS_04, 29),
    ThermocoupleData(138, 0.485, 0.285, 0.242, "MTCIW6F", "F1", Scanner.TS_04, 30),
    ThermocoupleData(139, 1.997, 1.538, 0.025, "MTC039B", "F49", Scanner.TS_04, 31),
    ThermocoupleData(140, 1.997, 1.538, 0.333, "MTC039M", "F49", Scanner.TS_04, 32),
    ThermocoupleData(141, 1.997, 1.538, 0.617, "MTC039F", "F49", Scanner.TS_04, 33),
    ThermocoupleData(142, 1.166, 1.249, 0.025, "MTC038B2", "F64", Scanner.TS_04, 36),
    ThermocoupleData(143, 2.497, 2.402, 0.025, "MTC040B1", "F111", Scanner.TS_04, 37),
    ThermocoupleData(144, 2.497, 2.402, 0.397, "MTC040M", "F111", Scanner.TS_04, 38),
    ThermocoupleData(145, 2.497, 2.402, 0.744, "MTC040F", "F111", Scanner.TS_04, 39),
]


def find_thermocouple(scanner: Scanner, channel: int) -> ThermocoupleData | None:
    try:
        return next(
            tc
            for tc in ThermocoupleTable
            if tc.scanner == scanner and tc.channel == channel
        )
    except StopIteration:
        return None
