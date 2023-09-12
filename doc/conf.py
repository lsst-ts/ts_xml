from documenteer.conf.pipelinespkg import *  # type: ignore # noqa
from lsst.ts import xml  # noqa

project = "ts_xml"
version = xml.__version__
html_theme_options["logotext"] = project  # type: ignore # noqa
html_title = project
html_short_title = project

intersphinx_mapping["ts_idl"] = ("https://ts-idl.lsst.io", None)  # type: ignore # noqa
extensions.remove("sphinxcontrib.autoprogram")  # type: ignore # noqa not used and doesn't report parallel safe
extensions.remove("documenteer.sphinxext.lssttasks")  # type: ignore # noqa not used and doesn't report parallel safe
