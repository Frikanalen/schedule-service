from enum import Enum

__NAMESPACE__ = "urn:tva:mpeg7:2008"


class PreferenceConditionTypeTimeValue(Enum):
    NONE = "none"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    ANNUALLY = "annually"
