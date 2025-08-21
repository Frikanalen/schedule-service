from enum import Enum

__NAMESPACE__ = "urn:tva:mpeg7:2008"


class AuxiliaryLanguageTypeValue(Enum):
    DUBBED = "dubbed"
    CLOSED_CAPTIONS = "closedCaptions"
    SUB_TITLES = "subTitles"
    SIGN_LANGUAGE = "signLanguage"
    AUDIO_DESCRIPTION = "audioDescription"
