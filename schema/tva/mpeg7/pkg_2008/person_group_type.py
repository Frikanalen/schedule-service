from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.agent_type import AgentType
from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)
from schema.tva.mpeg7.pkg_2008.electronic_address_type import (
    ElectronicAddressType,
)
from schema.tva.mpeg7.pkg_2008.organization_type import OrganizationType
from schema.tva.mpeg7.pkg_2008.person_group_type_name import (
    PersonGroupTypeName,
)
from schema.tva.mpeg7.pkg_2008.person_group_type_name_term import (
    PersonGroupTypeNameTerm,
)
from schema.tva.mpeg7.pkg_2008.person_name_type import PersonNameType
from schema.tva.mpeg7.pkg_2008.place_type import PlaceType
from schema.tva.mpeg7.pkg_2008.reference_type import ReferenceType
from schema.tva.mpeg7.pkg_2008.term_use_type import TermUseType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class PersonGroupType(AgentType):
    name: list[PersonGroupTypeName] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    name_term: list[PersonGroupTypeNameTerm] = field(
        default_factory=list,
        metadata={
            "name": "NameTerm",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    kind: Optional[TermUseType] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    member: list["PersonType"] = field(
        default_factory=list,
        metadata={
            "name": "Member",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    member_ref: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "MemberRef",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    jurisdiction: Optional[PlaceType] = field(
        default=None,
        metadata={
            "name": "Jurisdiction",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    jurisdiction_ref: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "JurisdictionRef",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    address: Optional[PlaceType] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    address_ref: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "AddressRef",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    electronic_address: Optional[ElectronicAddressType] = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )


@dataclass
class PersonTypeAffiliation:
    class Meta:
        global_type = False

    organization: Optional[OrganizationType] = field(
        default=None,
        metadata={
            "name": "Organization",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    organization_ref: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "OrganizationRef",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    person_group: Optional[PersonGroupType] = field(
        default=None,
        metadata={
            "name": "PersonGroup",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    person_group_ref: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "PersonGroupRef",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )


@dataclass
class PersonType(AgentType):
    name: list[PersonNameType] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    name_term: list[ControlledTermUseType] = field(
        default_factory=list,
        metadata={
            "name": "NameTerm",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    affiliation: list[PersonTypeAffiliation] = field(
        default_factory=list,
        metadata={
            "name": "Affiliation",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    citizenship: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Citizenship",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "white_space": "collapse",
            "pattern": r"[a-zA-Z]{2}",
        },
    )
    address: Optional[PlaceType] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    address_ref: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "AddressRef",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    electronic_address: list[ElectronicAddressType] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    person_description: Optional[TextualType] = field(
        default=None,
        metadata={
            "name": "PersonDescription",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    nationality: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nationality",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "white_space": "collapse",
            "pattern": r"[a-zA-Z]{2}",
        },
    )
