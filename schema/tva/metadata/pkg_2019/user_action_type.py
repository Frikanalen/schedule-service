from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.extended_uritype import ExtendedUritype
from schema.tva.mpeg7.pkg_2008.rating_type import RatingType
from schema.tva.mpeg7.pkg_2008.user_action_type import (
    UserActionType as UserActionTypeUserActionType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class UserActionType(UserActionTypeUserActionType):
    program_location: Optional[ExtendedUritype] = field(
        default=None,
        metadata={
            "name": "ProgramLocation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    rating: Optional[RatingType] = field(
        default=None,
        metadata={
            "name": "Rating",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
