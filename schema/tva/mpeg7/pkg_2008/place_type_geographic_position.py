from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.geographic_point_type import GeographicPointType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class PlaceTypeGeographicPosition:
    class Meta:
        global_type = False

    point: Optional[GeographicPointType] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "required": True,
        },
    )
    datum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
