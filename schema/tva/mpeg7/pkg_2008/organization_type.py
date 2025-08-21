from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.agent_type import AgentType
from schema.tva.mpeg7.pkg_2008.electronic_address_type import (
    ElectronicAddressType,
)
from schema.tva.mpeg7.pkg_2008.organization_type_name import (
    OrganizationTypeName,
)
from schema.tva.mpeg7.pkg_2008.organization_type_name_term import (
    OrganizationTypeNameTerm,
)
from schema.tva.mpeg7.pkg_2008.place_type import PlaceType
from schema.tva.mpeg7.pkg_2008.reference_type import ReferenceType
from schema.tva.mpeg7.pkg_2008.term_use_type import TermUseType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class OrganizationType(AgentType):
    name: list[OrganizationTypeName] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    name_term: list[OrganizationTypeNameTerm] = field(
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
    contact: list[AgentType] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    contact_ref: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "ContactRef",
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
