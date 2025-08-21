from dataclasses import dataclass, field

from schema.tva.metadata.pkg_2019.base_member_of_type import BaseMemberOfType
from schema.tva.metadata.pkg_2019.generic_derivation_reason_type import (
    GenericDerivationReasonType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class DerivedFromType(BaseMemberOfType):
    derivation_reason: list[GenericDerivationReasonType] = field(
        default_factory=list,
        metadata={
            "name": "DerivationReason",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
