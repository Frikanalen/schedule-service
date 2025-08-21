from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.related_material_type import (
    RelatedMaterialType,
)
from schema.tva.metadata.pkg_2019.tvaperson_name_type_name_type import (
    TvapersonNameTypeNameType,
)
from schema.tva.mpeg7.pkg_2008.person_name_type import PersonNameType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType
from schema.tva.mpeg7.pkg_2008.unique_idtype import UniqueIdtype

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvapersonNameType(PersonNameType):
    class Meta:
        name = "TVAPersonNameType"

    other_identifier: list[UniqueIdtype] = field(
        default_factory=list,
        metadata={
            "name": "OtherIdentifier",
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
    additional_information: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    name_type: Optional[TvapersonNameTypeNameType] = field(
        default=None,
        metadata={
            "name": "nameType",
            "type": "Attribute",
        },
    )
