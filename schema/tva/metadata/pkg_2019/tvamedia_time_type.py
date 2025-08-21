from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.tvamedia_rel_incr_time_point_type import (
    TvamediaRelIncrTimePointType,
)
from schema.tva.mpeg7.pkg_2008.media_incr_duration_type import (
    MediaIncrDurationType,
)
from schema.tva.mpeg7.pkg_2008.media_rel_time_point_type import (
    MediaRelTimePointType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvamediaTimeType:
    class Meta:
        name = "TVAMediaTimeType"

    media_rel_time_point: Optional[MediaRelTimePointType] = field(
        default=None,
        metadata={
            "name": "MediaRelTimePoint",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    media_rel_incr_time_point: Optional[TvamediaRelIncrTimePointType] = field(
        default=None,
        metadata={
            "name": "MediaRelIncrTimePoint",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    media_duration: Optional[str] = field(
        default=None,
        metadata={
            "name": "MediaDuration",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?",
        },
    )
    media_incr_duration: Optional[MediaIncrDurationType] = field(
        default=None,
        metadata={
            "name": "MediaIncrDuration",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
