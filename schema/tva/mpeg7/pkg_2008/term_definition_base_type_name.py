from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class TermDefinitionBaseTypeName(TextualType):
    class Meta:
        global_type = False

    preferred: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
