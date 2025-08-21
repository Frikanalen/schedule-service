from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.extended_uritype import ExtendedUritype
from schema.tva.metadata.pkg_2019.reviewer_type import ReviewerType
from schema.tva.mpeg7.pkg_2008.rating_type import RatingType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType
from schema.tva.mpeg7.pkg_2008.user_identifier_type import UserIdentifierType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class MediaReviewType:
    rating: list[RatingType] = field(
        default_factory=list,
        metadata={
            "name": "Rating",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    free_text_review: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "FreeTextReview",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    reviewer: list[ReviewerType] = field(
        default_factory=list,
        metadata={
            "name": "Reviewer",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    review_reference: Optional[ExtendedUritype] = field(
        default=None,
        metadata={
            "name": "ReviewReference",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    target: list[UserIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "Target",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
