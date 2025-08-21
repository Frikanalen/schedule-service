from dataclasses import dataclass, field
from typing import Union

from schema.tva.mpeg7.pkg_2008.summary_component_type_value import (
    SummaryComponentTypeValue,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class SummaryPreferencesTypeSummaryType:
    class Meta:
        global_type = False

    value: Union[str, SummaryComponentTypeValue] = field(
        default="",
        metadata={
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
    preference_value: int = field(
        default=10,
        metadata={
            "name": "preferenceValue",
            "type": "Attribute",
            "min_inclusive": -100,
            "max_inclusive": 100,
        },
    )
