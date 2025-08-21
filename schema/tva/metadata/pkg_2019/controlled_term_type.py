from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.term_name_type import TermNameType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ControlledTermType:
    name: Optional[TermNameType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    definition: Optional[TextualType] = field(
        default=None,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
