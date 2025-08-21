from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.rating_type_rating_scheme_style import (
    RatingTypeRatingSchemeStyle,
)
from schema.tva.mpeg7.pkg_2008.term_use_type import TermUseType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class RatingTypeRatingScheme(TermUseType):
    class Meta:
        global_type = False

    best: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    worst: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style: Optional[RatingTypeRatingSchemeStyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
