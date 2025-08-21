from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.tvatime_type import TvatimeType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class CreationCoordinatesType:
    creation_date: Optional[TvatimeType] = field(
        default=None,
        metadata={
            "name": "CreationDate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    creation_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreationLocation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "white_space": "collapse",
            "pattern": r"[a-zA-Z]{2}(-[a-zA-Z0-9]{1,3})?",
        },
    )
