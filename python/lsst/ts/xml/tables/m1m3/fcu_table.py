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
from math import sqrt

__all__ = ["FCUData", "FCUTable", "fcu_from_address"]


@dataclass
class FCUData:
    index: int
    x_position: float
    y_position: float
    z_position: float
    name: str

    def center_distance(self) -> float:
        """Calculate distance from mirror center. Usefull for obtaining mirror
        thickness above the FCU input.

        Returns
        -------
        distance : float
            Distance from mirror center in the XY plane.
        """
        return sqrt(self.x_position**2 + self.y_position**2)


FCUTable = [
    FCUData(0, 0.8160258, 3.8896036, 0, "F1"),
    FCUData(1, 0.3860038, 3.7613082, 0, "F2"),
    FCUData(2, -0.3860038, 3.7613082, 0, "F3"),
    FCUData(3, -0.8160258, 3.8896036, 0, "F4"),
    FCUData(4, 1.1067796, 3.2662622, 0, "F5"),
    FCUData(5, 0.4409694, 3.2662622, 0, "F6"),
    FCUData(6, -0.4409694, 3.2662622, 0, "F7"),
    FCUData(7, -1.1067796, 3.2662622, 0, "F8"),
    FCUData(8, 0.7767828, 2.6910538, 0, "F9"),
    FCUData(9, -0.0536956, 2.5928066, 0, "F10"),
    FCUData(10, -0.7767828, 2.6910538, 0, "F11"),
    FCUData(11, 2.4383746, 2.1130514, 0, "F12"),
    FCUData(12, 1.7725898, 2.1130514, 0, "F13"),
    FCUData(13, 0.4409694, 2.1130514, 0, "F14"),
    FCUData(14, -0.4409694, 2.1130514, 0, "F15"),
    FCUData(15, -1.7725898, 2.1130514, 0, "F16"),
    FCUData(16, -2.4383746, 2.1130514, 0, "F17"),
    FCUData(17, 3.4399982, 1.537843, 0, "F18"),
    FCUData(18, 2.774188, 1.537843, 0, "F19"),
    FCUData(19, 2.1083778, 1.537843, 0, "F20"),
    FCUData(20, 1.5527782, 1.5373858, 0, "F21"),
    FCUData(21, 0.8893302, 1.5393162, 0, "F22"),
    FCUData(22, 0.0573024, 1.6327374, 0, "F23"),
    FCUData(23, -0.8893302, 1.5393162, 0, "F24"),
    FCUData(24, -1.5527782, 1.5373858, 0, "F25"),
    FCUData(25, -2.1083778, 1.537843, 0, "F26"),
    FCUData(26, -2.774188, 1.537843, 0, "F27"),
    FCUData(27, -3.4399982, 1.537843, 0, "F28"),
    FCUData(28, 3.1091378, 1.149858, 0, "F29"),
    FCUData(29, 2.4383746, 0.9598406, 0, "F30"),
    FCUData(30, 1.7216374, 1.0602976, 0, "F31"),
    FCUData(31, 1.1067542, 0.9598406, 0, "F32"),
    FCUData(32, 0.4409694, 0.9598406, 0, "F33"),
    FCUData(33, -0.4409694, 0.9598406, 0, "F34"),
    FCUData(34, -1.1067796, 0.9598406, 0, "F35"),
    FCUData(35, -1.7216374, 1.0602976, 0, "F36"),
    FCUData(36, -2.4383746, 0.9598406, 0, "F37"),
    FCUData(37, -3.1091378, 1.149858, 0, "F38"),
    FCUData(38, 3.7607494, 0.2855976, 0, "F39"),
    FCUData(39, 2.774188, 0.3846322, 0, "F40"),
    FCUData(40, -2.1083778, 0.3846322, 0, "F41"),
    FCUData(41, 0.891032, 0.3866134, 0, "F42"),
    FCUData(42, -0.891032, 0.3866134, 0, "F43"),
    FCUData(43, -2.1083778, 0.3846322, 0, "F44"),
    FCUData(44, -2.774188, 0.3846322, 0, "F45"),
    FCUData(45, -3.7607494, 0.2855976, 0, "F46"),
    FCUData(46, 4.117086, -0.280162, 0, "F47"),
    FCUData(47, 3.7608002, -0.2874772, 0, "F48"),
    FCUData(48, 2.4383746, -0.1933702, 0, "F49"),
    FCUData(49, 1.7725898, -0.1933702, 0, "F50"),
    FCUData(50, -1.7725898, -0.1933702, 0, "F51"),
    FCUData(51, -2.4383746, -0.1933702, 0, "F52"),
    FCUData(52, -3.7588952, -0.2883154, 0, "F53"),
    FCUData(53, -4.117086, -0.280162, 0, "F54"),
    FCUData(54, 3.4399982, -0.7685786, 0, "F55"),
    FCUData(55, 2.774188, -0.7685786, 0, "F56"),
    FCUData(56, 2.1083778, -0.7685786, 0, "F57"),
    FCUData(57, 1.4368272, -0.767842, 0, "F58"),
    FCUData(58, 0.7767828, -0.7685786, 0, "F59"),
    FCUData(59, 0.3932174, -0.8725154, 0, "F60"),
    FCUData(60, -0.3932174, -0.8725154, 0, "F61"),
    FCUData(61, -0.7767828, -0.7685786, 0, "F62"),
    FCUData(62, -1.4368272, -0.767842, 0, "F63"),
    FCUData(63, -2.1083778, -0.7685786, 0, "F64"),
    FCUData(64, -2.774188, -0.7685786, 0, "F65"),
    FCUData(65, -3.4399982, -0.7685786, 0, "F66"),
    FCUData(66, 3.1041848, -1.346581, 0, "F67"),
    FCUData(67, 1.7725898, -1.346581, 0, "F68"),
    FCUData(68, 1.1096752, -1.3454126, 0, "F69"),
    FCUData(69, -1.1096752, -1.3454126, 0, "F70"),
    FCUData(70, -1.7725898, -1.346581, 0, "F71"),
    FCUData(71, -3.1041848, -1.346581, 0, "F72"),
    FCUData(72, 3.4810192, -1.919351, 0, "F73"),
    FCUData(73, 2.1083778, -1.9217894, 0, "F74"),
    FCUData(74, 1.442593, -1.9217894, 0, "F75"),
    FCUData(75, 0.7390892, -1.9887946, 0, "F76"),
    FCUData(76, -0.0544068, -1.8223738, 0, "F77"),
    FCUData(77, -0.7390892, -1.9887946, 0, "F78"),
    FCUData(78, -1.442593, -1.9217894, 0, "F79"),
    FCUData(79, -2.1083778, -1.9217894, 0, "F80"),
    FCUData(80, -3.4810192, -1.919351, 0, "F81"),
    FCUData(81, 2.4383746, -2.4997918, 0, "F82"),
    FCUData(82, 1.1067796, -2.4997918, 0, "F83"),
    FCUData(83, 0.4409694, -2.4997918, 0, "F84"),
    FCUData(84, -0.4409694, -2.4997918, 0, "F85"),
    FCUData(85, -1.1067796, -2.4997918, 0, "F86"),
    FCUData(86, -2.4383746, -2.4997918, 0, "F87"),
    FCUData(87, 0.7765288, -2.882265, 0, "F88"),
    FCUData(88, 0.222504, -3.0759654, 0, "F89"),
    FCUData(89, -0.222504, -3.0759654, 0, "F90"),
    FCUData(90, -0.7765288, -2.882265, 0, "F91"),
    FCUData(91, 1.8135092, -3.5172904, 0, "F92"),
    FCUData(92, 1.1067796, -3.6530026, 0, "F93"),
    FCUData(93, 0.4445, -3.6434776, 0, "F94"),
    FCUData(94, -0.4445, -3.6434776, 0, "F95"),
    FCUData(95, -1.8135092, -3.5172904, 0, "F96"),
]


def fcu_from_address(address: int) -> FCUData:
    return next(fcu for fcu in FCUTable if fcu.index == address - 1)
