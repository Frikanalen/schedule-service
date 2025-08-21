from enum import Enum

__NAMESPACE__ = "urn:tva:metadata:2019"


class TvamainTypeType(Enum):
    EPG = "epg"
    LAST_MINUTE_UPDATE = "lastMinuteUpdate"
    PRESENT_FOLLOWING = "presentFollowing"
    OTHER = "other"
