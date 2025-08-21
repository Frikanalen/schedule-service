from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.tvaplace_type import TvaplaceType
from schema.tva.metadata.pkg_2019.tvatime_type import TvatimeType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class DepictedCoordinatesType:
    depicted_date: Optional[TvatimeType] = field(
        default=None,
        metadata={
            "name": "DepictedDate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    depicted_location: Optional[TvaplaceType] = field(
        default=None,
        metadata={
            "name": "DepictedLocation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
