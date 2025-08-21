from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.classification_scheme_base_type import (
    ClassificationSchemeBaseType,
)
from schema.tva.mpeg7.pkg_2008.term_definition_type import TermDefinitionType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class ClassificationSchemeType(ClassificationSchemeBaseType):
    term: list[TermDefinitionType] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "min_occurs": 1,
        },
    )
