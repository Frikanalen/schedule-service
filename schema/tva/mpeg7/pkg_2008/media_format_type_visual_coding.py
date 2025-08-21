from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.media_format_type_visual_coding_format import (
    MediaFormatTypeVisualCodingFormat,
)
from schema.tva.mpeg7.pkg_2008.media_format_type_visual_coding_frame import (
    MediaFormatTypeVisualCodingFrame,
)
from schema.tva.mpeg7.pkg_2008.media_format_type_visual_coding_pixel import (
    MediaFormatTypeVisualCodingPixel,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaFormatTypeVisualCoding:
    class Meta:
        global_type = False

    format: Optional[MediaFormatTypeVisualCodingFormat] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    pixel: Optional[MediaFormatTypeVisualCodingPixel] = field(
        default=None,
        metadata={
            "name": "Pixel",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    frame: Optional[MediaFormatTypeVisualCodingFrame] = field(
        default=None,
        metadata={
            "name": "Frame",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
