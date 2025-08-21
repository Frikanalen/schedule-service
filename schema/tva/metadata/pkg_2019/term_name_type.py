from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TermNameType(TextualType):
    preferred: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
