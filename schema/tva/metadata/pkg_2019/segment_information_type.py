from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.basic_segment_description_type import (
    BasicSegmentDescriptionType,
)
from schema.tva.metadata.pkg_2019.cridref_type import CridrefType
from schema.tva.metadata.pkg_2019.time_base_reference_type import (
    TimeBaseReferenceType,
)
from schema.tva.metadata.pkg_2019.tvamedia_time_type import TvamediaTimeType
from schema.tva.mpeg7.pkg_2008.unique_idtype import UniqueIdtype

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class SegmentInformationType:
    """
    :ivar program_ref:
    :ivar instance_metadata_id_ref:
    :ivar time_base_reference:
    :ivar description:
    :ivar segment_locator:
    :ivar key_frame_locator:
    :ivar other_identifier:
    :ivar segment_id:
    :ivar fragment_id:
    :ivar fragment_version:
    :ivar fragment_expiration_date:
    :ivar metadata_origin_idref:
    :ivar lang:
    :ivar is_skippable: A flag to signal if the segment can be skipped.
    :ivar is_printable: A flag to signal if the information about that
        segment can be published / printed e.g. in program guides.
    """

    program_ref: Optional[CridrefType] = field(
        default=None,
        metadata={
            "name": "ProgramRef",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    instance_metadata_id_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InstanceMetadataIdRef",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "pattern": r"(i|I)(m|M)(i|I):(([^/]+)/)?([^/]+)",
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
    description: Optional[BasicSegmentDescriptionType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    segment_locator: Optional[TvamediaTimeType] = field(
        default=None,
        metadata={
            "name": "SegmentLocator",
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
    segment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "segmentId",
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
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    is_skippable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSkippable",
            "type": "Attribute",
        },
    )
    is_printable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPrintable",
            "type": "Attribute",
        },
    )
