from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaFormatTypeBitRate:
    class Meta:
        global_type = False

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    variable: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    minimum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    average: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maximum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
