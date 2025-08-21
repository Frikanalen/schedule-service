from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.preference_condition_type import (
    PreferenceConditionType,
)
from schema.tva.mpeg7.pkg_2008.term_use_type import TermUseType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class BrowsingPreferencesTypePreferenceCondition(PreferenceConditionType):
    class Meta:
        global_type = False

    genre: Optional[TermUseType] = field(
        default=None,
        metadata={
            "name": "Genre",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
