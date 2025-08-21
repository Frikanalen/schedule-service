from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.place_type import PlaceType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class SourcePreferencesTypeDisseminationLocation(PlaceType):
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
