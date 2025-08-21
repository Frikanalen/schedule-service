from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class CridrefType:
    class Meta:
        name = "CRIDRefType"

    crid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        },
    )
