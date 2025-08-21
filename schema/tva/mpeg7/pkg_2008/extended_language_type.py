from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.extended_language_type_type import (
    ExtendedLanguageTypeType,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class ExtendedLanguageType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: ExtendedLanguageTypeType = field(
        default=ExtendedLanguageTypeType.ORIGINAL,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    supplemental: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
