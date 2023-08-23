#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
