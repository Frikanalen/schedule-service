from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.cridref_type import CridrefType
from schema.tva.metadata.pkg_2019.valid_period_type import ValidPeriodType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class BaseMemberOfType(CridrefType):
    time_limitation: list[ValidPeriodType] = field(
        default_factory=list,
        metadata={
            "name": "TimeLimitation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
