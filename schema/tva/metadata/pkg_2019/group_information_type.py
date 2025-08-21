from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.aggregation_of_type import AggregationOfType
from schema.tva.metadata.pkg_2019.base_member_of_type import BaseMemberOfType
from schema.tva.metadata.pkg_2019.base_program_group_type_type import (
    BaseProgramGroupTypeType,
)
from schema.tva.metadata.pkg_2019.basic_content_description_type import (
    BasicContentDescriptionType,
)
from schema.tva.mpeg7.pkg_2008.unique_idtype import UniqueIdtype

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class GroupInformationType:
    group_type: Optional[BaseProgramGroupTypeType] = field(
        default=None,
        metadata={
            "name": "GroupType",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "required": True,
        },
    )
    basic_description: Optional[BasicContentDescriptionType] = field(
        default=None,
        metadata={
            "name": "BasicDescription",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "required": True,
        },
    )
    member_of: list[BaseMemberOfType] = field(
        default_factory=list,
        metadata={
            "name": "MemberOf",
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
    part_of_aggregated_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartOfAggregatedGroup",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        },
    )
    aggregation_of: Optional[AggregationOfType] = field(
        default=None,
        metadata={
            "name": "AggregationOf",
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
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        },
    )
    ordered: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    num_of_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "numOfItems",
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
    service_idref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "serviceIDRef",
            "type": "Attribute",
            "tokens": True,
        },
    )
