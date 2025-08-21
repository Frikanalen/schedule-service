from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.media_locator_type import MediaLocatorType
from schema.tva.mpeg7.pkg_2008.media_time_type import MediaTimeType
from schema.tva.mpeg7.pkg_2008.temporal_segment_locator_type_byte_position import (
    TemporalSegmentLocatorTypeBytePosition,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class TemporalSegmentLocatorType(MediaLocatorType):
    media_time: Optional[MediaTimeType] = field(
        default=None,
        metadata={
            "name": "MediaTime",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    byte_position: Optional[TemporalSegmentLocatorTypeBytePosition] = field(
        default=None,
        metadata={
            "name": "BytePosition",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
