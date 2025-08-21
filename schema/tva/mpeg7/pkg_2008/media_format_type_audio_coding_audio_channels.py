from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaFormatTypeAudioCodingAudioChannels:
    class Meta:
        global_type = False

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    front: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    side: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rear: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lfe: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    track: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
