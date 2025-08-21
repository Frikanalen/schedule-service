from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.usage_history_type import UsageHistoryType
from schema.tva.mpeg7.pkg_2008.user_preferences_type import UserPreferencesType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class UserDescriptionType:
    user_preferences: Optional[UserPreferencesType] = field(
        default=None,
        metadata={
            "name": "UserPreferences",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    usage_history: Optional[UsageHistoryType] = field(
        default=None,
        metadata={
            "name": "UsageHistory",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
