from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.aggregation_of_type_type import (
    AggregationOfTypeType,
)
from schema.tva.metadata.pkg_2019.cridref_type import CridrefType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class AggregationOfType:
    aggregated_program: list[CridrefType] = field(
        default_factory=list,
        metadata={
            "name": "AggregatedProgram",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "min_occurs": 2,
        },
    )
    type_value: Optional[AggregationOfTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
