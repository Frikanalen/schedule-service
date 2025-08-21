from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.controlled_term_type import (
    ControlledTermType,
)
from schema.tva.metadata.pkg_2019.purchase_type_quantity_range import (
    PurchaseTypeQuantityRange,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class PurchaseType:
    purchase_type: Optional[ControlledTermType] = field(
        default=None,
        metadata={
            "name": "PurchaseType",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    quantity_unit: Optional[ControlledTermType] = field(
        default=None,
        metadata={
            "name": "QuantityUnit",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    quantity_range: Optional[PurchaseTypeQuantityRange] = field(
        default=None,
        metadata={
            "name": "QuantityRange",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
