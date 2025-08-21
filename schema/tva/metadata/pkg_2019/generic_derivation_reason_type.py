from dataclasses import dataclass, field

from schema.tva.metadata.pkg_2019.base_derivation_reason_type import (
    BaseDerivationReasonType,
)
from schema.tva.metadata.pkg_2019.controlled_term_type import (
    ControlledTermType,
)
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class GenericDerivationReasonType(BaseDerivationReasonType):
    classifier: list[ControlledTermType] = field(
        default_factory=list,
        metadata={
            "name": "Classifier",
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
            "min_occurs": 1,
        },
    )
