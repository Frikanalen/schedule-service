from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.textual_base_type import TextualBaseType
from schema.tva.mpeg7.pkg_2008.title_type_value import TitleTypeValue

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class TitleType(TextualBaseType):
    type_value: TitleTypeValue = field(
        default=TitleTypeValue.MAIN,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
