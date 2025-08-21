from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class SignLanguageType:
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
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    closed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
