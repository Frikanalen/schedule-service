from dataclasses import dataclass, field
from typing import Union

from schema.tva.metadata.pkg_2019.tvaterm_definition_base_type import (
    TvatermDefinitionBaseType,
)
from schema.tva.mpeg7.pkg_2008.term_relation_qualifier_type_value import (
    TermRelationQualifierTypeValue,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvatermDefinitionType(TvatermDefinitionBaseType):
    class Meta:
        name = "TVATermDefinitionType"

    term: list["TvatermDefinitionTypeTerm"] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )


@dataclass
class TvatermDefinitionTypeTerm(TvatermDefinitionType):
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
