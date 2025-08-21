from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvatimeType:
    class Meta:
        name = "TVATimeType"

    time_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimePoint",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "required": True,
            "pattern": r"(\-?\d+(\-\d{2}(\-\d{2})?)?)?(T\d{2}(:\d{2}(:\d{2}(:\d+)?)?)?)?(F\d+)?((\-|\+)\d{2}:\d{2})?",
        },
    )
    duration: Optional[str] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?((\-|\+)\d{2}:\d{2}Z)?",
        },
    )
