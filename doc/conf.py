"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documenation builds.
"""
import sys

from documenteer.sphinxconfig.stackconf import build_package_configs

sys.setrecursionlimit(2000)


globals().update(build_package_configs(
    project_name="ts_xml",
    version="develop"))


# Remove ts_xml from the default intersphinx configuration
try:
    del intersphinx_mapping['ts_xml']  # noqa
except KeyError:
    pass

extensions.append('sphinx.ext.autosectionlabel')
autosectionlabel_prefix_document=True