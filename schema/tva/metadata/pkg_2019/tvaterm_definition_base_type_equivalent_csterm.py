from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvatermDefinitionBaseTypeEquivalentCsterm:
    class Meta:
        global_type = False

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
