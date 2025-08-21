from enum import Enum

__NAMESPACE__ = "urn:tva:metadata:2019"


class ColorTypeType(Enum):
    COLOR = "color"
    BLACK_AND_WHITE = "blackAndWhite"
    BLACK_AND_WHITE_AND_COLOR = "blackAndWhiteAndColor"
    COLORIZED = "colorized"
