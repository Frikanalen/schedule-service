from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.media_rel_incr_time_point_type import (
    MediaRelIncrTimePointType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvamediaRelIncrTimePointType(MediaRelIncrTimePointType):
    class Meta:
        name = "TVAMediaRelIncrTimePointType"

    media_time_unit: str = field(
        default="PT1N1000F",
        metadata={
            "name": "mediaTimeUnit",
            "type": "Attribute",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?",
        },
    )
