from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.aggregation_of_type import AggregationOfType
from schema.tva.metadata.pkg_2019.avattributes_type import AvattributesType
from schema.tva.metadata.pkg_2019.basic_content_description_type import (
    BasicContentDescriptionType,
)
from schema.tva.metadata.pkg_2019.derived_from_type import DerivedFromType
from schema.tva.metadata.pkg_2019.episode_of_type import EpisodeOfType
from schema.tva.metadata.pkg_2019.member_of_type import MemberOfType
from schema.tva.mpeg7.pkg_2008.unique_idtype import UniqueIdtype

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ProgramInformationType:
    basic_description: Optional[BasicContentDescriptionType] = field(
        default=None,
        metadata={
            "name": "BasicDescription",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "required": True,
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
    avattributes: Optional[AvattributesType] = field(
        default=None,
        metadata={
            "name": "AVAttributes",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    member_of: list[MemberOfType] = field(
        default_factory=list,
        metadata={
            "name": "MemberOf",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    derived_from: Optional[DerivedFromType] = field(
        default=None,
        metadata={
            "name": "DerivedFrom",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    episode_of: Optional[EpisodeOfType] = field(
        default=None,
        metadata={
            "name": "EpisodeOf",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    part_of_aggregated_program: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartOfAggregatedProgram",
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
    program_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "programId",
            "type": "Attribute",
            "required": True,
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
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
