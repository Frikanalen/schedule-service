from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime, XmlDuration

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.flag_type import FlagType
from schema.tva.metadata.pkg_2019.program_location_type import (
    ProgramLocationType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ScheduleEventType(ProgramLocationType):
    published_start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PublishedStartTime",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    published_end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PublishedEndTime",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    published_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PublishedDuration",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    actual_start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActualStartTime",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    actual_end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActualEndTime",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    actual_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ActualDuration",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    live: Optional[FlagType] = field(
        default=None,
        metadata={
            "name": "Live",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    repeat: Optional[FlagType] = field(
        default=None,
        metadata={
            "name": "Repeat",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    first_showing: Optional[FlagType] = field(
        default=None,
        metadata={
            "name": "FirstShowing",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    last_showing: Optional[FlagType] = field(
        default=None,
        metadata={
            "name": "LastShowing",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    free: Optional[FlagType] = field(
        default=None,
        metadata={
            "name": "Free",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
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
