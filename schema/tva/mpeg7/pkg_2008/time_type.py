from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.incr_duration_type import IncrDurationType
from schema.tva.mpeg7.pkg_2008.rel_incr_time_point_type import (
    RelIncrTimePointType,
)
from schema.tva.mpeg7.pkg_2008.rel_time_point_type import RelTimePointType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class TimeType:
    time_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimePoint",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "pattern": r"(\-?\d+(\-\d{2}(\-\d{2})?)?)?(T\d{2}(:\d{2}(:\d{2}(:\d+)?)?)?)?(F\d+)?((\-|\+)\d{2}:\d{2})?",
        },
    )
    rel_time_point: Optional[RelTimePointType] = field(
        default=None,
        metadata={
            "name": "RelTimePoint",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    rel_incr_time_point: Optional[RelIncrTimePointType] = field(
        default=None,
        metadata={
            "name": "RelIncrTimePoint",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    duration: Optional[str] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?((\-|\+)\d{2}:\d{2}Z)?",
        },
    )
    incr_duration: Optional[IncrDurationType] = field(
        default=None,
        metadata={
            "name": "IncrDuration",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
