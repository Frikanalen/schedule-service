from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.browsing_preferences_type import (
    BrowsingPreferencesType,
)
from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.filtering_and_search_preferences_type import (
    FilteringAndSearchPreferencesType,
)
from schema.tva.mpeg7.pkg_2008.user_choice_type import UserChoiceType
from schema.tva.mpeg7.pkg_2008.user_identifier_type import UserIdentifierType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class UserPreferencesType(Dstype):
    user_identifier: Optional[UserIdentifierType] = field(
        default=None,
        metadata={
            "name": "UserIdentifier",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    filtering_and_search_preferences: list[
        FilteringAndSearchPreferencesType
    ] = field(
        default_factory=list,
        metadata={
            "name": "FilteringAndSearchPreferences",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    browsing_preferences: list[BrowsingPreferencesType] = field(
        default_factory=list,
        metadata={
            "name": "BrowsingPreferences",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    allow_automatic_update: UserChoiceType = field(
        default=UserChoiceType.FALSE,
        metadata={
            "name": "allowAutomaticUpdate",
            "type": "Attribute",
        },
    )
