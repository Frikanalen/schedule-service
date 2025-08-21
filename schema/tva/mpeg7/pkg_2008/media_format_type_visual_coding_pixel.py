from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaFormatTypeVisualCodingPixel:
    class Meta:
        global_type = False

    resolution: Optional[int] = field(
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
    bits_per: Optional[int] = field(
        default=None,
        metadata={
            "name": "bitsPer",
            "type": "Attribute",
        },
    )
