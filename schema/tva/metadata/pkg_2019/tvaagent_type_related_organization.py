from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.tvaidref_element_type import (
    TvaidrefElementType,
)
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvaagentTypeRelatedOrganization:
    class Meta:
        global_type = False

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
    relationship: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
