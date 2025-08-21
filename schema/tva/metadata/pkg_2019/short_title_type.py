from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.title_type import TitleType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ShortTitleType(TitleType):
    length: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
