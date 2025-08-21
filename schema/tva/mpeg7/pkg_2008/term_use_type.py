from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.inline_term_definition_type import (
    InlineTermDefinitionType,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class TermUseType(InlineTermDefinitionType):
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
