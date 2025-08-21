from dataclasses import dataclass, field
from typing import Optional, Union

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.segment_group_list_type import (
    SegmentGroupListType,
)
from schema.tva.metadata.pkg_2019.segment_list_type import SegmentListType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class SegmentInformationTableType:
    segment_list: Optional[SegmentListType] = field(
        default=None,
        metadata={
            "name": "SegmentList",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    segment_group_list: Optional[SegmentGroupListType] = field(
        default=None,
        metadata={
            "name": "SegmentGroupList",
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
