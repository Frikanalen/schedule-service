from dataclasses import dataclass, field

from schema.tva.metadata.pkg_2019.purchase_item_type import PurchaseItemType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class PurchaseListType:
    purchase_item: list[PurchaseItemType] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseItem",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    purchase_id_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseIdRef",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
