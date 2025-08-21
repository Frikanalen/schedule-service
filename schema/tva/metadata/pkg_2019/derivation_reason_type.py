from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.base_derivation_reason_type import (
    BaseDerivationReasonType,
)
from schema.tva.metadata.pkg_2019.derivation_reason_type_value import (
    DerivationReasonTypeValue,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class DerivationReasonType(BaseDerivationReasonType):
    value: Optional[DerivationReasonTypeValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
