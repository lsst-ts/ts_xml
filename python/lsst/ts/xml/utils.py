# This file is part of ts_xml
#
# Developed for the LSST Data Management System.
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

__all__ = ["get_pkg_root", "get_sal_interfaces_dir"]

import pathlib


def get_pkg_root():
    """Return the root directory of this package."""
    return pathlib.Path(__file__).resolve().parent / "data"


def get_sal_interfaces_dir():
    """Return the path to the ``sal_interfaces`` dir within this package."""
    return get_pkg_root() / "trunk" / "ts_xml" / "sal_interfaces"
