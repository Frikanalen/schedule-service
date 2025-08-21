from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.textual_base_type import TextualBaseType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class NameComponentType(TextualBaseType):
    initial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    abbrev: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
