from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.dtype import Dtype
from schema.tva.mpeg7.pkg_2008.place_type import PlaceType
from schema.tva.mpeg7.pkg_2008.preference_condition_type_time import (
    PreferenceConditionTypeTime,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class PreferenceConditionType(Dtype):
    place: Optional[PlaceType] = field(
        default=None,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    time: list[PreferenceConditionTypeTime] = field(
        default_factory=list,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
