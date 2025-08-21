from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.term_use_type import TermUseType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class CreationPreferencesTypeTool(TermUseType):
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
