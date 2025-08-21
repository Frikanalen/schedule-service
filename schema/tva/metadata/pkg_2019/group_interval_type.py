from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class GroupIntervalType:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
