from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.media_incr_duration_type import (
    MediaIncrDurationType,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaTimeType:
    media_time_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "MediaTimePoint",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "required": True,
            "pattern": r"(\-?\d+(\-\d{2}(\-\d{2})?)?)?(T\d{2}(:\d{2}(:\d{2}(:\d+)?)?)?)?(F\d+)?",
        },
    )
    media_duration: Optional[str] = field(
        default=None,
        metadata={
            "name": "MediaDuration",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?",
        },
    )
    media_incr_duration: Optional[MediaIncrDurationType] = field(
        default=None,
        metadata={
            "name": "MediaIncrDuration",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
