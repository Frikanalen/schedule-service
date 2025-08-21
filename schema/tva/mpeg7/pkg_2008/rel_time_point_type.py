from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class RelTimePointType:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?((\-|\+)\d{2}:\d{2}Z)?",
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
