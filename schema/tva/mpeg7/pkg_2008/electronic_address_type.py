from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.electronic_address_type_telephone import (
    ElectronicAddressTypeTelephone,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class ElectronicAddressType:
    telephone: list[ElectronicAddressTypeTelephone] = field(
        default_factory=list,
        metadata={
            "name": "Telephone",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    fax: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    email: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    url: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
