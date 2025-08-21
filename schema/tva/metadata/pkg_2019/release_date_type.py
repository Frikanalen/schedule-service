from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlPeriod

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ReleaseDateType:
    day_and_year: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DayAndYear",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    year: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
