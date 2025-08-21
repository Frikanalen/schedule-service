from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class ParentalGuidanceType:
    parental_rating: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "ParentalRating",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    minimum_age: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumAge",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    region: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "white_space": "collapse",
            "pattern": r"[a-zA-Z]{2}(-[a-zA-Z0-9]{1,3})?",
        },
    )
