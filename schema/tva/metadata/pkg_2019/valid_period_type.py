from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ValidPeriodType:
    valid_from: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidFrom",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    valid_to: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidTo",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
