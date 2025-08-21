from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)
from schema.tva.mpeg7.pkg_2008.dtype import Dtype
from schema.tva.mpeg7.pkg_2008.media_format_type_audio_coding import (
    MediaFormatTypeAudioCoding,
)
from schema.tva.mpeg7.pkg_2008.media_format_type_bit_rate import (
    MediaFormatTypeBitRate,
)
from schema.tva.mpeg7.pkg_2008.media_format_type_visual_coding import (
    MediaFormatTypeVisualCoding,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaFormatType(Dtype):
    content: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "required": True,
        },
    )
    medium: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "Medium",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    file_format: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "FileFormat",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    file_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "FileSize",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    system: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    bit_rate: Optional[MediaFormatTypeBitRate] = field(
        default=None,
        metadata={
            "name": "BitRate",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    visual_coding: Optional[MediaFormatTypeVisualCoding] = field(
        default=None,
        metadata={
            "name": "VisualCoding",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    audio_coding: Optional[MediaFormatTypeAudioCoding] = field(
        default=None,
        metadata={
            "name": "AudioCoding",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    scene_coding_format: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "SceneCodingFormat",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    graphics_coding_format: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "GraphicsCodingFormat",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    other_coding_format: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "OtherCodingFormat",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
