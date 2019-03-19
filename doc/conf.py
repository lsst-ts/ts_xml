"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documenation builds.
"""
import sys;
sys.setrecursionlimit(2000)

from documenteer.sphinxconfig.stackconf import build_package_configs
# import ts_xml
# import ts_xml.version


globals().update(build_package_configs(
    project_name="ts_xml",
    version="develop"))


# Remove ts_xml from the default intersphinx configuration
try:
    del intersphinx_mapping['ts_xml']  # noqa
except KeyError:
    pass


# Add pipelines.lsst.io to the intersphinx configuration.
# NOTE: we might want to be more sophisticated about mapping corresponding
# versions of the Pipelines and ts_xml. This technique will
# mostly work if the Pipelines and ts_xml are developed
# concurrently.
intersphinx_mapping['lsst'] = ('https://pipelines.lsst.io/v/daily/', None)  # noqa
