from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.mapping_term_type import MappingTermType
from schema.tva.metadata.pkg_2019.tvaterm_definition_base_type_equivalent_csterm import (
    TvatermDefinitionBaseTypeEquivalentCsterm,
)
from schema.tva.metadata.pkg_2019.tvaterm_definition_base_type_name import (
    TvatermDefinitionBaseTypeName,
)
from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvatermDefinitionBaseType(Dstype):
    class Meta:
        name = "TVATermDefinitionBaseType"

    name: list[TvatermDefinitionBaseTypeName] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    definition: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    equivalent_csterm: list[TvatermDefinitionBaseTypeEquivalentCsterm] = field(
        default_factory=list,
        metadata={
            "name": "EquivalentCSTerm",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    mapping_term: list[MappingTermType] = field(
        default_factory=list,
        metadata={
            "name": "mappingTerm",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    term_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "termID",
            "type": "Attribute",
        },
    )
