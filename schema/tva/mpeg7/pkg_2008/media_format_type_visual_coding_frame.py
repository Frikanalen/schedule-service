from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.media_format_type_visual_coding_frame_structure import (
    MediaFormatTypeVisualCodingFrameStructure,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaFormatTypeVisualCodingFrame:
    class Meta:
        global_type = False

    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    aspect_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "aspectRatio",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    rate: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    structure: Optional[MediaFormatTypeVisualCodingFrameStructure] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
