from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.release_date_type import ReleaseDateType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ReleaseInformationType:
    release_date: Optional[ReleaseDateType] = field(
        default=None,
        metadata={
            "name": "ReleaseDate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    release_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReleaseLocation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "white_space": "collapse",
            "pattern": r"[a-zA-Z]{2}(-[a-zA-Z0-9]{1,3})?",
        },
    )
