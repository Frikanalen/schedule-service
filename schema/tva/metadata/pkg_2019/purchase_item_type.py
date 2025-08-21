from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from schema.tva.metadata.pkg_2019.drmdeclaration_type import DrmdeclarationType
from schema.tva.metadata.pkg_2019.price_type import PriceType
from schema.tva.metadata.pkg_2019.purchase_type import PurchaseType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class PurchaseItemType:
    price: list[PriceType] = field(
        default_factory=list,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "min_occurs": 1,
        },
    )
    purchase: list[PurchaseType] = field(
        default_factory=list,
        metadata={
            "name": "Purchase",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    description: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    pricing_server_url: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PricingServerURL",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    drmdeclaration: Optional[DrmdeclarationType] = field(
        default=None,
        metadata={
            "name": "DRMDeclaration",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
