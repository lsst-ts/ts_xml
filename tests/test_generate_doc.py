#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

from lsst.ts.xml.generate_sal_generics_doc import write_generic_page
from lsst.ts.xml.generate_subsystems_doc import generate_subsystems_doc
from lsst.ts.xml.utils import get_pkg_root


def test_generate_subsystems_doc() -> None:
    generate_subsystems_doc()
    rst_dir = get_pkg_root() / "doc" / "sal_interfaces"
    index = rst_dir / "index.rst"

    try:
        assert rst_dir.exists()
        assert index.exists()
    finally:
        for ff in rst_dir.glob("*"):
            ff.unlink()
        rst_dir.rmdir()


def test_write_generic_page() -> None:
    write_generic_page()
    rst_dir = get_pkg_root() / "doc" / "sal_generics.rst"

    try:
        assert rst_dir.exists()
    finally:
        rst_dir.unlink(missing_ok=True)
