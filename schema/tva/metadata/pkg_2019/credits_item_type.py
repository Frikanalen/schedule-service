from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.related_material_type import (
    RelatedMaterialType,
)
from schema.tva.metadata.pkg_2019.tvaagent_type import TvaagentType
from schema.tva.mpeg7.pkg_2008.person_name_type import PersonNameType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class CreditsItemType(TvaagentType):
    character: list[PersonNameType] = field(
        default_factory=list,
        metadata={
            "name": "Character",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    presentation_role: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "PresentationRole",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    related_material: list[RelatedMaterialType] = field(
        default_factory=list,
        metadata={
            "name": "RelatedMaterial",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
