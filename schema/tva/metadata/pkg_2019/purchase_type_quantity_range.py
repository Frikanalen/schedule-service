from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class PurchaseTypeQuantityRange:
    class Meta:
        global_type = False

    min: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
