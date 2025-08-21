from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.electronic_address_type_telephone_type import (
    ElectronicAddressTypeTelephoneType,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class ElectronicAddressTypeTelephone:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: Optional[ElectronicAddressTypeTelephoneType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
