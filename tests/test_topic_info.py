# This file is part of ts_xml.
#
# Developed for the Rubin Observatory Telescope and Site System.
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
# ß
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from lsst.ts.xml.topic_info import TopicInfo


def test_topic_from_avro() -> None:
    topic_subname = "arbitrary_subname"
    topic_info = TopicInfo.from_avro(
        "focal_plane_sensor.avsc", "ATCamera", topic_subname, False
    )
    assert topic_info.component_name == "ATCamera"
    assert topic_info.sal_name == "focal_plane_sensor"
    assert (
        topic_info._avro_schema_cache[("ATCamera", "tel_focal_plane_sensor")]
        is not None
    )
    schema = topic_info.make_avro_schema()
    assert len(schema["fields"][1]["type"]) == 2
