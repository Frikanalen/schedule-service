from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaRelIncrTimePointType:
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    media_time_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediaTimeUnit",
            "type": "Attribute",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?",
        },
    )
