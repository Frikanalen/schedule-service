from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class TemporalSegmentLocatorTypeBytePosition:
    class Meta:
        global_type = False

    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
