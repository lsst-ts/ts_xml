from documenteer.conf.pipelinespkg import *  # type: ignore # noqa

from lsst.ts.xml import *  # noqa

project = "ts_xml"
html_theme_options["logotext"] = project  # type: ignore # noqa
html_title = project
html_short_title = project

intersphinx_mapping["ts_idl"] = ("https://ts-idl.lsst.io", None)  # type: ignore # noqa
