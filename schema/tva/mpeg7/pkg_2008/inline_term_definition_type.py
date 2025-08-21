from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.inline_term_definition_type_name import (
    InlineTermDefinitionTypeName,
)
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class InlineTermDefinitionType:
    name: list[InlineTermDefinitionTypeName] = field(
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
