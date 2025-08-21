from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.color_type_type import ColorTypeType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ColorType:
    type_value: Optional[ColorTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
