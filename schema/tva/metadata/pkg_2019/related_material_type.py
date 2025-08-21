from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.controlled_term_type import (
    ControlledTermType,
)
from schema.tva.metadata.pkg_2019.related_material_type_format import (
    RelatedMaterialTypeFormat,
)
from schema.tva.metadata.pkg_2019.related_material_type_social_media_reference import (
    RelatedMaterialTypeSocialMediaReference,
)
from schema.tva.metadata.pkg_2019.segment_reference_type import (
    SegmentReferenceType,
)
from schema.tva.metadata.pkg_2019.tvamedia_locator_type import (
    TvamediaLocatorType,
)
from schema.tva.mpeg7.pkg_2008.media_locator_type import MediaLocatorType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType
from schema.tva.mpeg7.pkg_2008.title_media_type import TitleMediaType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class RelatedMaterialType:
    how_related: Optional[ControlledTermType] = field(
        default=None,
        metadata={
            "name": "HowRelated",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    format: Optional[RelatedMaterialTypeFormat] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    media_locator: list[TvamediaLocatorType] = field(
        default_factory=list,
        metadata={
            "name": "MediaLocator",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    segment_reference: Optional[SegmentReferenceType] = field(
        default=None,
        metadata={
            "name": "SegmentReference",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    promotional_text: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "PromotionalText",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    promotional_media: list[TitleMediaType] = field(
        default_factory=list,
        metadata={
            "name": "PromotionalMedia",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    social_media_reference: list[RelatedMaterialTypeSocialMediaReference] = (
        field(
            default_factory=list,
            metadata={
                "name": "SocialMediaReference",
                "type": "Element",
                "namespace": "urn:tva:metadata:2019",
            },
        )
    )
    source_media_locator: Optional[MediaLocatorType] = field(
        default=None,
        metadata={
            "name": "SourceMediaLocator",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
