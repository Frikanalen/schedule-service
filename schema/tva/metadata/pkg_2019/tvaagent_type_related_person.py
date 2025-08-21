from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.tvaidref_element_type import (
    TvaidrefElementType,
)
from schema.tva.metadata.pkg_2019.tvaperson_name_type import TvapersonNameType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvaagentTypeRelatedPerson:
    class Meta:
        global_type = False

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
    relationship: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
