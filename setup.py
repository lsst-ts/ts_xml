#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_namespace_packages

install_requires = ["black"]
setup_requires = ["setuptools_scm", "pytest-runner"]
tests_requires = ["pytest", "pytest-flake8", "lxml", "black"]
dev_requires = install_requires + tests_requires + ["documenteer[pipelines]"]

setup(
    name="ts_xml",
    description="Installs python code for ts_xml.",
    install_requires=install_requires,
    setup_requires=setup_requires,
    package_dir={"": "python"},
    packages=find_namespace_packages(where="python"),
    scripts=[],
    tests_require=tests_requires,
    extras_require={},
    license="GPL",
)
