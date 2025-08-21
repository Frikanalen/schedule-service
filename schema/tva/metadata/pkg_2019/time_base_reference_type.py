from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.media_rel_incr_time_point_type import (
    MediaRelIncrTimePointType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TimeBaseReferenceType:
    media_time_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "MediaTimePoint",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "pattern": r"(\-?\d+(\-\d{2}(\-\d{2})?)?)?(T\d{2}(:\d{2}(:\d{2}(:\d+)?)?)?)?(F\d+)?",
        },
    )
    media_rel_incr_time_point: Optional[MediaRelIncrTimePointType] = field(
        default=None,
        metadata={
            "name": "MediaRelIncrTimePoint",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    timebase_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "timebaseId",
            "type": "Attribute",
        },
    )
