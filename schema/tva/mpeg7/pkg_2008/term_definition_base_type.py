from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.term_definition_base_type_name import (
    TermDefinitionBaseTypeName,
)
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class TermDefinitionBaseType(Dstype):
    name: list[TermDefinitionBaseTypeName] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    definition: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    term_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "termID",
            "type": "Attribute",
        },
    )
