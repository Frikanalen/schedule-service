from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class PlaceTypeAdministrativeUnit:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
