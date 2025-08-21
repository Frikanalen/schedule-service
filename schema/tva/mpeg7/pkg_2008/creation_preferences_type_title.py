from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.title_type import TitleType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class CreationPreferencesTypeTitle(TitleType):
    class Meta:
        global_type = False

    preference_value: int = field(
        default=10,
        metadata={
            "name": "preferenceValue",
            "type": "Attribute",
            "min_inclusive": -100,
            "max_inclusive": 100,
        },
    )
