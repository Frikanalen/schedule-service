from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from schema.tva.metadata.pkg_2019.tvaperson_name_type import TvapersonNameType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class PersonNameFragmentType(TvapersonNameType):
    person_name_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "personNameId",
            "type": "Attribute",
            "required": True,
        },
    )
    fragment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "fragmentId",
            "type": "Attribute",
        },
    )
    fragment_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "fragmentVersion",
            "type": "Attribute",
        },
    )
    fragment_expiration_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "fragmentExpirationDate",
            "type": "Attribute",
        },
    )
    metadata_origin_idref: Optional[str] = field(
        default=None,
        metadata={
            "name": "metadataOriginIDRef",
            "type": "Attribute",
        },
    )
