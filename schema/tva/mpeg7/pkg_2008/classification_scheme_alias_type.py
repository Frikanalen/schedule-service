from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.header_type import HeaderType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class ClassificationSchemeAliasType(HeaderType):
    alias: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
