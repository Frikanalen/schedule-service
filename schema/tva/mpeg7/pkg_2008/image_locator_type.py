from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.image_locator_type_byte_position import (
    ImageLocatorTypeBytePosition,
)
from schema.tva.mpeg7.pkg_2008.media_locator_type import MediaLocatorType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class ImageLocatorType(MediaLocatorType):
    media_time_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "MediaTimePoint",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "pattern": r"(\-?\d+(\-\d{2}(\-\d{2})?)?)?(T\d{2}(:\d{2}(:\d{2}(:\d+)?)?)?)?(F\d+)?",
        },
    )
    byte_position: Optional[ImageLocatorTypeBytePosition] = field(
        default=None,
        metadata={
            "name": "BytePosition",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
