from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.preference_condition_type_time_value import (
    PreferenceConditionTypeTimeValue,
)
from schema.tva.mpeg7.pkg_2008.time_type import TimeType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class PreferenceConditionTypeTime(TimeType):
    class Meta:
        global_type = False

    recurrence: PreferenceConditionTypeTimeValue = field(
        default=PreferenceConditionTypeTimeValue.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    num_of_recurrences: Optional[int] = field(
        default=None,
        metadata={
            "name": "numOfRecurrences",
            "type": "Attribute",
        },
    )
