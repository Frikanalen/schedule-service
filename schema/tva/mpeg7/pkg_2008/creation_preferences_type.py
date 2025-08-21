from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.creation_preferences_type_creator import (
    CreationPreferencesTypeCreator,
)
from schema.tva.mpeg7.pkg_2008.creation_preferences_type_date_period import (
    CreationPreferencesTypeDatePeriod,
)
from schema.tva.mpeg7.pkg_2008.creation_preferences_type_keyword import (
    CreationPreferencesTypeKeyword,
)
from schema.tva.mpeg7.pkg_2008.creation_preferences_type_location import (
    CreationPreferencesTypeLocation,
)
from schema.tva.mpeg7.pkg_2008.creation_preferences_type_title import (
    CreationPreferencesTypeTitle,
)
from schema.tva.mpeg7.pkg_2008.creation_preferences_type_tool import (
    CreationPreferencesTypeTool,
)
from schema.tva.mpeg7.pkg_2008.dstype import Dstype

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class CreationPreferencesType(Dstype):
    title: list[CreationPreferencesTypeTitle] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    creator: list[CreationPreferencesTypeCreator] = field(
        default_factory=list,
        metadata={
            "name": "Creator",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    keyword: list[CreationPreferencesTypeKeyword] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    location: list[CreationPreferencesTypeLocation] = field(
        default_factory=list,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    date_period: list[CreationPreferencesTypeDatePeriod] = field(
        default_factory=list,
        metadata={
            "name": "DatePeriod",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    tool: list[CreationPreferencesTypeTool] = field(
        default_factory=list,
        metadata={
            "name": "Tool",
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
