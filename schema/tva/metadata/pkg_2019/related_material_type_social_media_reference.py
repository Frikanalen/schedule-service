from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class RelatedMaterialTypeSocialMediaReference:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    reference_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "referenceType",
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
