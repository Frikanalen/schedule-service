from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class PriceType:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        },
    )
