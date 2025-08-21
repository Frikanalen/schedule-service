from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.valid_period_type import ValidPeriodType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ServiceRefType:
    valid_period: list[ValidPeriodType] = field(
        default_factory=list,
        metadata={
            "name": "ValidPeriod",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    service_idref: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceIDRef",
            "type": "Attribute",
            "required": True,
        },
    )
