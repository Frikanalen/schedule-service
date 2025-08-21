from enum import Enum

__NAMESPACE__ = "urn:tva:metadata:2019"


class DerivationReasonTypeValue(Enum):
    VIOLENCE = "violence"
    LANGUAGE = "language"
    SEX = "sex"
    DURATION = "duration"
    OTHER = "other"
