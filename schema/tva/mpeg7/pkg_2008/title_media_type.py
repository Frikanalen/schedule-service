from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.image_locator_type import ImageLocatorType
from schema.tva.mpeg7.pkg_2008.temporal_segment_locator_type import (
    TemporalSegmentLocatorType,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class TitleMediaType:
    title_image: Optional[ImageLocatorType] = field(
        default=None,
        metadata={
            "name": "TitleImage",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    title_video: Optional[TemporalSegmentLocatorType] = field(
        default=None,
        metadata={
            "name": "TitleVideo",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    title_audio: Optional[TemporalSegmentLocatorType] = field(
        default=None,
        metadata={
            "name": "TitleAudio",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
