from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.bit_rate_type import BitRateType
from schema.tva.metadata.pkg_2019.controlled_term_type import (
    ControlledTermType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class CaptioningAttributesType:
    coding: Optional[ControlledTermType] = field(
        default=None,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    bit_rate: Optional[BitRateType] = field(
        default=None,
        metadata={
            "name": "BitRate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
