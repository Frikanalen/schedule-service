from enum import Enum

__NAMESPACE__ = "urn:tva:metadata:2019"


class SynopsisLengthType(Enum):
    BRIEF = "brief"
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"
    EXTENDED = "extended"
