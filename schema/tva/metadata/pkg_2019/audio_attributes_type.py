from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.audio_language_type import AudioLanguageType
from schema.tva.metadata.pkg_2019.bit_rate_type import BitRateType
from schema.tva.metadata.pkg_2019.controlled_term_type import (
    ControlledTermType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class AudioAttributesType:
    coding: Optional[ControlledTermType] = field(
        default=None,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    num_of_channels: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumOfChannels",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    mix_type: Optional[ControlledTermType] = field(
        default=None,
        metadata={
            "name": "MixType",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    audio_language: Optional[AudioLanguageType] = field(
        default=None,
        metadata={
            "name": "AudioLanguage",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    sample_frequency: Optional[int] = field(
        default=None,
        metadata={
            "name": "SampleFrequency",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    bits_per_sample: Optional[int] = field(
        default=None,
        metadata={
            "name": "BitsPerSample",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    bit_rate: Optional[BitRateType] = field(
        default=None,
        metadata={
            "name": "BitRate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
