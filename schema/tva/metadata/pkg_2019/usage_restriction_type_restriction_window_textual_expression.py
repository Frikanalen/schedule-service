from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class UsageRestrictionTypeRestrictionWindowTextualExpression:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
