from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime, XmlDuration

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.program_location_type import (
    ProgramLocationType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class PushDownloadType(ProgramLocationType):
    published_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PublishedDuration",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    start_of_availability: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartOfAvailability",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    end_of_availability: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndOfAvailability",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    content_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "ContentVersion",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    expiry_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpiryTime",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    activation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActivationTime",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
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
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    service_idref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "serviceIDRef",
            "type": "Attribute",
            "tokens": True,
        },
    )
