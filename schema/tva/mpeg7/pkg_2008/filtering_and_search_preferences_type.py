from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.classification_preferences_type import (
    ClassificationPreferencesType,
)
from schema.tva.mpeg7.pkg_2008.creation_preferences_type import (
    CreationPreferencesType,
)
from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.preference_condition_type import (
    PreferenceConditionType,
)
from schema.tva.mpeg7.pkg_2008.source_preferences_type import (
    SourcePreferencesType,
)
from schema.tva.mpeg7.pkg_2008.user_choice_type import UserChoiceType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class FilteringAndSearchPreferencesType(Dstype):
    creation_preferences: list[CreationPreferencesType] = field(
        default_factory=list,
        metadata={
            "name": "CreationPreferences",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    classification_preferences: list[ClassificationPreferencesType] = field(
        default_factory=list,
        metadata={
            "name": "ClassificationPreferences",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    source_preferences: list[SourcePreferencesType] = field(
        default_factory=list,
        metadata={
            "name": "SourcePreferences",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    preference_condition: list[PreferenceConditionType] = field(
        default_factory=list,
        metadata={
            "name": "PreferenceCondition",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    filtering_and_search_preferences: list[
        "FilteringAndSearchPreferencesType"
    ] = field(
        default_factory=list,
        metadata={
            "name": "FilteringAndSearchPreferences",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
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
