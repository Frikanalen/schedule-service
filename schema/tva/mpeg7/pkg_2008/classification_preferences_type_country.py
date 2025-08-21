from dataclasses import dataclass, field

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class ClassificationPreferencesTypeCountry:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "collapse",
            "pattern": r"[a-zA-Z]{2}",
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
