from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)
from schema.tva.mpeg7.pkg_2008.media_format_type_audio_coding_audio_channels import (
    MediaFormatTypeAudioCodingAudioChannels,
)
from schema.tva.mpeg7.pkg_2008.media_format_type_audio_coding_sample import (
    MediaFormatTypeAudioCodingSample,
)
from schema.tva.mpeg7.pkg_2008.media_format_type_audio_coding_value import (
    MediaFormatTypeAudioCodingValue,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaFormatTypeAudioCoding:
    class Meta:
        global_type = False

    format: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    audio_channels: Optional[MediaFormatTypeAudioCodingAudioChannels] = field(
        default=None,
        metadata={
            "name": "AudioChannels",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    sample: Optional[MediaFormatTypeAudioCodingSample] = field(
        default=None,
        metadata={
            "name": "Sample",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    emphasis: Optional[MediaFormatTypeAudioCodingValue] = field(
        default=None,
        metadata={
            "name": "Emphasis",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    presentation: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
