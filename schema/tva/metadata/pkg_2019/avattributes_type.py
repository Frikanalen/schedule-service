from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.audio_attributes_type import (
    AudioAttributesType,
)
from schema.tva.metadata.pkg_2019.bit_rate_type import BitRateType
from schema.tva.metadata.pkg_2019.captioning_attributes_type import (
    CaptioningAttributesType,
)
from schema.tva.metadata.pkg_2019.controlled_term_type import (
    ControlledTermType,
)
from schema.tva.metadata.pkg_2019.video_attributes_type import (
    VideoAttributesType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class AvattributesType:
    class Meta:
        name = "AVAttributesType"

    file_format: Optional[ControlledTermType] = field(
        default=None,
        metadata={
            "name": "FileFormat",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    file_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "FileSize",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    system: Optional[ControlledTermType] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    bit_rate: list[BitRateType] = field(
        default_factory=list,
        metadata={
            "name": "BitRate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "max_occurs": 2,
        },
    )
    audio_attributes: list[AudioAttributesType] = field(
        default_factory=list,
        metadata={
            "name": "AudioAttributes",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    video_attributes: Optional[VideoAttributesType] = field(
        default=None,
        metadata={
            "name": "VideoAttributes",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    captioning_attributes: list[CaptioningAttributesType] = field(
        default_factory=list,
        metadata={
            "name": "CaptioningAttributes",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
