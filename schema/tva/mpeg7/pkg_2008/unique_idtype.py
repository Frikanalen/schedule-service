from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.unique_idtype_encoding import (
    UniqueIdtypeEncoding,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class UniqueIdtype:
    class Meta:
        name = "UniqueIDType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: str = field(
        default="URI",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    organization: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    encoding: UniqueIdtypeEncoding = field(
        default=UniqueIdtypeEncoding.TEXT,
        metadata={
            "type": "Attribute",
        },
    )
