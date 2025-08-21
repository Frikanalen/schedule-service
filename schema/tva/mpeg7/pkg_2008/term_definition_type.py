from dataclasses import dataclass, field
from typing import Union

from schema.tva.mpeg7.pkg_2008.term_definition_base_type import (
    TermDefinitionBaseType,
)
from schema.tva.mpeg7.pkg_2008.term_relation_qualifier_type_value import (
    TermRelationQualifierTypeValue,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class TermDefinitionType(TermDefinitionBaseType):
    term: list["TermDefinitionTypeTerm"] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )


@dataclass
class TermDefinitionTypeTerm(TermDefinitionType):
    class Meta:
        global_type = False

    relation: Union[str, TermRelationQualifierTypeValue] = field(
        default=TermRelationQualifierTypeValue.NT,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
