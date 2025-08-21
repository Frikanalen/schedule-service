from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.organization_type_name_type import (
    OrganizationTypeNameType,
)
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class OrganizationTypeName(TextualType):
    class Meta:
        global_type = False

    type_value: Optional[OrganizationTypeNameType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
