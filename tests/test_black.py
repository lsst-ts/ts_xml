# This file is part of ts_xml.
#
# Developed for the LSST Telescope and Site Systems.
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
import subprocess

from lsst.ts import xml


class BlackTestCase(unittest.TestCase):
    def test_black_formatted(self):
        """Test that all Python code is formatted with black.
        """

        pkg_root = xml.get_pkg_root()
        result = subprocess.run(
            ["black", "--check", str(pkg_root), "--exclude", "version.py"],
            capture_output=True,
        )
        if result.returncode != 0:
            raise AssertionError(result.stderr)


if __name__ == "__main__":
    unittest.main()
