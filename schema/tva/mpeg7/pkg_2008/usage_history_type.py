from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.user_action_history_type import (
    UserActionHistoryType,
)
from schema.tva.mpeg7.pkg_2008.user_choice_type import UserChoiceType
from schema.tva.mpeg7.pkg_2008.user_identifier_type import UserIdentifierType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class UsageHistoryType(Dstype):
    user_identifier: Optional[UserIdentifierType] = field(
        default=None,
        metadata={
            "name": "UserIdentifier",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    user_action_history: list[UserActionHistoryType] = field(
        default_factory=list,
        metadata={
            "name": "UserActionHistory",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "min_occurs": 1,
        },
    )
    allow_collection: UserChoiceType = field(
        default=UserChoiceType.FALSE,
        metadata={
            "name": "allowCollection",
            "type": "Attribute",
        },
    )
