from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.rating_type_rating_scheme import (
    RatingTypeRatingScheme,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class RatingType:
    rating_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "RatingValue",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "required": True,
        },
    )
    rating_scheme: Optional[RatingTypeRatingScheme] = field(
        default=None,
        metadata={
            "name": "RatingScheme",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "required": True,
        },
    )
