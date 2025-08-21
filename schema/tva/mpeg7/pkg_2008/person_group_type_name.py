from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.person_group_type_name_type import (
    PersonGroupTypeNameType,
)
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class PersonGroupTypeName(TextualType):
    class Meta:
        global_type = False

    type_value: Optional[PersonGroupTypeNameType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
