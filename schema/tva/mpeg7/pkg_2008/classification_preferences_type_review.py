from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.agent_type import AgentType
from schema.tva.mpeg7.pkg_2008.rating_type import RatingType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class ClassificationPreferencesTypeReview:
    class Meta:
        global_type = False

    rating: Optional[RatingType] = field(
        default=None,
        metadata={
            "name": "Rating",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    reviewer: Optional[AgentType] = field(
        default=None,
        metadata={
            "name": "Reviewer",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    preference_value: int = field(
        default=10,
        metadata={
            "name": "preferenceValue",
            "type": "Attribute",
            "min_inclusive": -100,
            "max_inclusive": 100,
        },
    )
