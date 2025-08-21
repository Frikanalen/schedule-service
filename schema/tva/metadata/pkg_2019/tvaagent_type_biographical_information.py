from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvaagentTypeBiographicalInformation:
    class Meta:
        global_type = False

    birth_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    death_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DeathDate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    nationality: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Nationality",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "white_space": "collapse",
            "pattern": r"[a-zA-Z]{2}",
        },
    )
    occupation: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Occupation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
