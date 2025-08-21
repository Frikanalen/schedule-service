from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.browsing_preferences_type_preference_condition import (
    BrowsingPreferencesTypePreferenceCondition,
)
from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.summary_preferences_type import (
    SummaryPreferencesType,
)
from schema.tva.mpeg7.pkg_2008.user_choice_type import UserChoiceType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class BrowsingPreferencesType(Dstype):
    summary_preferences: list[SummaryPreferencesType] = field(
        default_factory=list,
        metadata={
            "name": "SummaryPreferences",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    preference_condition: list[BrowsingPreferencesTypePreferenceCondition] = (
        field(
            default_factory=list,
            metadata={
                "name": "PreferenceCondition",
                "type": "Element",
                "namespace": "urn:tva:mpeg7:2008",
            },
        )
    )
    protected: UserChoiceType = field(
        default=UserChoiceType.TRUE,
        metadata={
            "type": "Attribute",
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
