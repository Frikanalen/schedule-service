from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.base_segment_group_type_type import (
    BaseSegmentGroupTypeType,
)
from schema.tva.metadata.pkg_2019.basic_segment_description_type import (
    BasicSegmentDescriptionType,
)
from schema.tva.metadata.pkg_2019.cridref_type import CridrefType
from schema.tva.metadata.pkg_2019.group_interval_type import GroupIntervalType
from schema.tva.metadata.pkg_2019.groups_type import GroupsType
from schema.tva.metadata.pkg_2019.segments_type import SegmentsType
from schema.tva.metadata.pkg_2019.time_base_reference_type import (
    TimeBaseReferenceType,
)
from schema.tva.metadata.pkg_2019.tvamedia_time_type import TvamediaTimeType
from schema.tva.mpeg7.pkg_2008.unique_idtype import UniqueIdtype

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class SegmentGroupInformationType:
    program_ref: Optional[CridrefType] = field(
        default=None,
        metadata={
            "name": "ProgramRef",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "required": True,
        },
    )
    time_base_reference: Optional[TimeBaseReferenceType] = field(
        default=None,
        metadata={
            "name": "TimeBaseReference",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    group_type: list[BaseSegmentGroupTypeType] = field(
        default_factory=list,
        metadata={
            "name": "GroupType",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "min_occurs": 1,
        },
    )
    description: Optional[BasicSegmentDescriptionType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    group_interval: Optional[GroupIntervalType] = field(
        default=None,
        metadata={
            "name": "GroupInterval",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    segments: Optional[SegmentsType] = field(
        default=None,
        metadata={
            "name": "Segments",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    groups: Optional[GroupsType] = field(
        default=None,
        metadata={
            "name": "Groups",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    key_frame_locator: list[TvamediaTimeType] = field(
        default_factory=list,
        metadata={
            "name": "KeyFrameLocator",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    other_identifier: list[UniqueIdtype] = field(
        default_factory=list,
        metadata={
            "name": "OtherIdentifier",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    group_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "groupId",
            "type": "Attribute",
            "required": True,
        },
    )
    ordered: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    number_of_segments: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfSegments",
            "type": "Attribute",
        },
    )
    number_of_key_frames: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfKeyFrames",
            "type": "Attribute",
        },
    )
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?",
        },
    )
    top_level: Optional[bool] = field(
        default=None,
        metadata={
            "name": "topLevel",
            "type": "Attribute",
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
