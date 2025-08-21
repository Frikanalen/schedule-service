from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from schema.tva.metadata.pkg_2019.awards_list_type import AwardsListType
from schema.tva.metadata.pkg_2019.caption_language_type import (
    CaptionLanguageType,
)
from schema.tva.metadata.pkg_2019.creation_coordinates_type import (
    CreationCoordinatesType,
)
from schema.tva.metadata.pkg_2019.credits_list_type import CreditsListType
from schema.tva.metadata.pkg_2019.depicted_coordinates_type import (
    DepictedCoordinatesType,
)
from schema.tva.metadata.pkg_2019.genre_type import GenreType
from schema.tva.metadata.pkg_2019.keyword_type import KeywordType
from schema.tva.metadata.pkg_2019.purchase_list_type import PurchaseListType
from schema.tva.metadata.pkg_2019.related_material_type import (
    RelatedMaterialType,
)
from schema.tva.metadata.pkg_2019.release_information_type import (
    ReleaseInformationType,
)
from schema.tva.metadata.pkg_2019.short_title_type import ShortTitleType
from schema.tva.metadata.pkg_2019.sign_language_type import SignLanguageType
from schema.tva.metadata.pkg_2019.synopsis_type import SynopsisType
from schema.tva.metadata.pkg_2019.tvaparental_guidance_type import (
    TvaparentalGuidanceType,
)
from schema.tva.metadata.pkg_2019.tvatime_type import TvatimeType
from schema.tva.mpeg7.pkg_2008.extended_language_type import (
    ExtendedLanguageType,
)
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType
from schema.tva.mpeg7.pkg_2008.title_media_type import TitleMediaType
from schema.tva.mpeg7.pkg_2008.title_type import TitleType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class BasicContentDescriptionType:
    title: list[TitleType] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    media_title: list[TitleMediaType] = field(
        default_factory=list,
        metadata={
            "name": "MediaTitle",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    short_title: list[ShortTitleType] = field(
        default_factory=list,
        metadata={
            "name": "ShortTitle",
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
    promotional_information: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "PromotionalInformation",
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
    genre: list[GenreType] = field(
        default_factory=list,
        metadata={
            "name": "Genre",
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
    language: list[ExtendedLanguageType] = field(
        default_factory=list,
        metadata={
            "name": "Language",
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
    credits_list: Optional[CreditsListType] = field(
        default=None,
        metadata={
            "name": "CreditsList",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    awards_list: Optional[AwardsListType] = field(
        default=None,
        metadata={
            "name": "AwardsList",
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
    production_date: Optional[TvatimeType] = field(
        default=None,
        metadata={
            "name": "ProductionDate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    production_location: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ProductionLocation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "white_space": "collapse",
            "pattern": r"[a-zA-Z]{2}(-[a-zA-Z0-9]{1,3})?",
        },
    )
    creation_coordinates: list[CreationCoordinatesType] = field(
        default_factory=list,
        metadata={
            "name": "CreationCoordinates",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    depicted_coordinates: list[DepictedCoordinatesType] = field(
        default_factory=list,
        metadata={
            "name": "DepictedCoordinates",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    release_information: list[ReleaseInformationType] = field(
        default_factory=list,
        metadata={
            "name": "ReleaseInformation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
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
