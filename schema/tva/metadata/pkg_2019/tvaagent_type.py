from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.tvaagent_type_biographical_information import (
    TvaagentTypeBiographicalInformation,
)
from schema.tva.metadata.pkg_2019.tvaagent_type_related_organization import (
    TvaagentTypeRelatedOrganization,
)
from schema.tva.metadata.pkg_2019.tvaagent_type_related_person import (
    TvaagentTypeRelatedPerson,
)
from schema.tva.metadata.pkg_2019.tvaidref_element_type import (
    TvaidrefElementType,
)
from schema.tva.metadata.pkg_2019.tvaperson_name_type import TvapersonNameType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvaagentType:
    class Meta:
        name = "TVAAgentType"

    person_name: Optional[TvapersonNameType] = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    person_name_idref: Optional[TvaidrefElementType] = field(
        default=None,
        metadata={
            "name": "PersonNameIDRef",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    biographical_information: list[TvaagentTypeBiographicalInformation] = (
        field(
            default_factory=list,
            metadata={
                "name": "BiographicalInformation",
                "type": "Element",
                "namespace": "urn:tva:metadata:2019",
            },
        )
    )
    organization_name: Optional[TextualType] = field(
        default=None,
        metadata={
            "name": "OrganizationName",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    organization_name_idref: Optional[TvaidrefElementType] = field(
        default=None,
        metadata={
            "name": "OrganizationNameIDRef",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    related_person: list[TvaagentTypeRelatedPerson] = field(
        default_factory=list,
        metadata={
            "name": "RelatedPerson",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    related_organization: list[TvaagentTypeRelatedOrganization] = field(
        default_factory=list,
        metadata={
            "name": "RelatedOrganization",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
