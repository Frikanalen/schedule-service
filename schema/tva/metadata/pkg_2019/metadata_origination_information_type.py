from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class MetadataOriginationInformationType:
    publisher: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "Publisher",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    rights_owner: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "RightsOwner",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    copyright_notice: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "CopyrightNotice",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    origin_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "originID",
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
