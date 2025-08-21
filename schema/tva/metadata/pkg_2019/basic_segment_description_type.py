from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.credits_list_type import CreditsListType
from schema.tva.metadata.pkg_2019.genre_type import GenreType
from schema.tva.metadata.pkg_2019.keyword_type import KeywordType
from schema.tva.metadata.pkg_2019.related_material_type import (
    RelatedMaterialType,
)
from schema.tva.metadata.pkg_2019.synopsis_type import SynopsisType
from schema.tva.mpeg7.pkg_2008.title_type import TitleType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class BasicSegmentDescriptionType:
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
    keyword: list[KeywordType] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
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
    credits_list: Optional[CreditsListType] = field(
        default=None,
        metadata={
            "name": "CreditsList",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
