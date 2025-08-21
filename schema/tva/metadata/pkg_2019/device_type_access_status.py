from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class DeviceTypeAccessStatus:
    class Meta:
        global_type = False

    blocked: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
