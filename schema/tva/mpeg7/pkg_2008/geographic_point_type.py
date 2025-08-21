from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class GeographicPointType:
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        },
    )
    latitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        },
    )
    altitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
