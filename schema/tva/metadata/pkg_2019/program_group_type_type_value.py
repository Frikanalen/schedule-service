from enum import Enum

__NAMESPACE__ = "urn:tva:metadata:2019"


class ProgramGroupTypeTypeValue(Enum):
    SERIES = "series"
    SHOW = "show"
    PROGRAM_CONCEPT = "programConcept"
    PROGRAM_COMPILATION = "programCompilation"
    OTHER_COLLECTION = "otherCollection"
    OTHER_CHOICE = "otherChoice"
    MINI_SERIES = "mini-series"
    SUB_SERIES = "sub-series"
    SEASON = "season"
    BRAND = "brand"
    AUTOMATIC_ACQUISITION_THEMED = "automaticAcquisitionThemed"
    AUTOMATIC_ACQUISITION_NON_THEMED = "automaticAcquisitionNonThemed"
    CLIP = "clip"
    APPLICATION = "application"
