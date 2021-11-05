from documenteer.conf.pipelinespkg import *  # noqa


project = "ts_xml"
html_theme_options["logotext"] = project  # noqa
html_title = project
html_short_title = project

intersphinx_mapping["ts_idl"] = ("https://ts-idl.lsst.io", None)  # noqa
