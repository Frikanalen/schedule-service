from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.media_time_type import MediaTimeType
from schema.tva.mpeg7.pkg_2008.time_type import TimeType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class UserActionTypeActionTime:
    class Meta:
        global_type = False

    media_time: Optional[MediaTimeType] = field(
        default=None,
        metadata={
            "name": "MediaTime",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    general_time: Optional[TimeType] = field(
        default=None,
        metadata={
            "name": "GeneralTime",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
