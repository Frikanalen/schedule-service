from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.genre_type import GenreType
from schema.tva.metadata.pkg_2019.purchase_list_type import PurchaseListType
from schema.tva.metadata.pkg_2019.related_material_type import (
    RelatedMaterialType,
)
from schema.tva.metadata.pkg_2019.service_information_name_type import (
    ServiceInformationNameType,
)
from schema.tva.metadata.pkg_2019.service_information_type_service_url import (
    ServiceInformationTypeServiceUrl,
)
from schema.tva.metadata.pkg_2019.service_ref_type import ServiceRefType
from schema.tva.metadata.pkg_2019.synopsis_type import SynopsisType
from schema.tva.metadata.pkg_2019.tvamedia_locator_type import (
    TvamediaLocatorType,
)
from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ServiceInformationType:
    name: list[ServiceInformationNameType] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    owner: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Owner",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    service_url: list[ServiceInformationTypeServiceUrl] = field(
        default_factory=list,
        metadata={
            "name": "ServiceURL",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    service_type: list[ControlledTermUseType] = field(
        default_factory=list,
        metadata={
            "name": "ServiceType",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    logo: list[TvamediaLocatorType] = field(
        default_factory=list,
        metadata={
            "name": "Logo",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    service_description: list[SynopsisType] = field(
        default_factory=list,
        metadata={
            "name": "ServiceDescription",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    service_genre: list[GenreType] = field(
        default_factory=list,
        metadata={
            "name": "ServiceGenre",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    service_language: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLanguage",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    parent_service: list[ServiceRefType] = field(
        default_factory=list,
        metadata={
            "name": "ParentService",
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
    purchase_list: Optional[PurchaseListType] = field(
        default=None,
        metadata={
            "name": "PurchaseList",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    group_purchase_idref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "GroupPurchaseIDRef",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    service_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceId",
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
