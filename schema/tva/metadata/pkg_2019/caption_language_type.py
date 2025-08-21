from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class CaptionLanguageType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    primary: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    translation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    closed: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    supplemental: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
