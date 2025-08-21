from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.avattributes_type import AvattributesType
from schema.tva.metadata.pkg_2019.base_member_of_type import BaseMemberOfType
from schema.tva.metadata.pkg_2019.caption_language_type import (
    CaptionLanguageType,
)
from schema.tva.metadata.pkg_2019.genre_type import GenreType
from schema.tva.metadata.pkg_2019.purchase_list_type import PurchaseListType
from schema.tva.metadata.pkg_2019.related_material_type import (
    RelatedMaterialType,
)
from schema.tva.metadata.pkg_2019.sign_language_type import SignLanguageType
from schema.tva.metadata.pkg_2019.synopsis_type import SynopsisType
from schema.tva.metadata.pkg_2019.tvaparental_guidance_type import (
    TvaparentalGuidanceType,
)
from schema.tva.mpeg7.pkg_2008.title_type import TitleType
from schema.tva.mpeg7.pkg_2008.unique_idtype import UniqueIdtype

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class InstanceDescriptionType:
    title: list[TitleType] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    synopsis: list[SynopsisType] = field(
        default_factory=list,
        metadata={
            "name": "Synopsis",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    genre: list[GenreType] = field(
        default_factory=list,
        metadata={
            "name": "Genre",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    purchase_list: Optional[PurchaseListType] = field(
        default=None,
        metadata={
            "name": "PurchaseList",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    caption_language: list[CaptionLanguageType] = field(
        default_factory=list,
        metadata={
            "name": "CaptionLanguage",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    sign_language: list[SignLanguageType] = field(
        default_factory=list,
        metadata={
            "name": "SignLanguage",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    parental_guidance: list[TvaparentalGuidanceType] = field(
        default_factory=list,
        metadata={
            "name": "ParentalGuidance",
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
    related_material: list[RelatedMaterialType] = field(
        default_factory=list,
        metadata={
            "name": "RelatedMaterial",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
