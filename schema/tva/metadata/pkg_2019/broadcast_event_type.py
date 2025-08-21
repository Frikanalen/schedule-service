from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from schema.tva.metadata.pkg_2019.schedule_event_type import ScheduleEventType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class BroadcastEventType(ScheduleEventType):
    service_idref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "serviceIDRef",
            "type": "Attribute",
            "tokens": True,
        },
    )
    fragment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "fragmentId",
            "type": "Attribute",
        },
    )
    fragment_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "fragmentVersion",
            "type": "Attribute",
        },
    )
    fragment_expiration_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "fragmentExpirationDate",
            "type": "Attribute",
        },
    )
