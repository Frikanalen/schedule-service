from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)
from schema.tva.mpeg7.pkg_2008.organization_type_name_term_type import (
    OrganizationTypeNameTermType,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class OrganizationTypeNameTerm(ControlledTermUseType):
    class Meta:
        global_type = False

    type_value: Optional[OrganizationTypeNameTermType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
