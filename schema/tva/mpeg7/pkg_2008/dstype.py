from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.mpeg7_base_type import Mpeg7BaseType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class Dstype(Mpeg7BaseType):
    class Meta:
        name = "DSType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    time_base: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeBase",
            "type": "Attribute",
            "pattern": r"/?((((child::)?((\i\c*:)?(\i\c*)(\[\d+\])?))|\.|(\.\.))/)*((((child::)?((\i\c*:)?(\i\c*)(\[\d+\])?))|\.)|((attribute::|@)((\i\c*:)?(\i\c*|\*))))",
        },
    )
    time_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeUnit",
            "type": "Attribute",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?((\-|\+)\d{2}:\d{2}Z)?",
        },
    )
