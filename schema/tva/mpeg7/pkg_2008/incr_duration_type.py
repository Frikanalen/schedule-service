from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class IncrDurationType:
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
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
