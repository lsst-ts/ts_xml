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

__all__ = [
    "get_pkg_root",
    "get_data_dir",
    "get_sal_interfaces_dir",
    "find_in_xml",
    "find_tag_in_xml",
    "find_text_in_xml",
]

import pathlib
from xml.etree import ElementTree


def get_pkg_root() -> pathlib.Path:
    """Return the root directory of this package."""
    return pathlib.Path(__file__).resolve().parents[4]


def get_data_dir() -> pathlib.Path:
    """Return the data directory of this package."""
    return pathlib.Path(__file__).resolve().parent / "data"


def get_sal_interfaces_dir() -> pathlib.Path:
    """Return the path to the ``sal_interfaces`` dir within this package."""
    return get_data_dir() / "sal_interfaces"


def find_in_xml(element: ElementTree.Element, item: str) -> ElementTree.Element:
    """Find an element and make sure it is not None."""
    found = element.find(item)
    if found is None:
        raise RuntimeError(f"{element}.find({item}) returned None")
    return found


def find_tag_in_xml(element: ElementTree.Element, item: str) -> str:
    """Find the tag of an XML element."""
    found = find_in_xml(element=element, item=item)
    if found.tag is None:
        raise RuntimeError(f"{element}.find({item}) has null tag")
    return found.tag


def find_text_in_xml(element: ElementTree.Element, item: str) -> str:
    """Find the text of an XML element."""
    found = find_in_xml(element=element, item=item)
    if found.text is None:
        raise RuntimeError(f"{element}.find({item}) has null text")
    return found.text
