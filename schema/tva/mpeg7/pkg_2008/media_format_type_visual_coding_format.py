from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)
from schema.tva.mpeg7.pkg_2008.media_format_type_visual_coding_format_value import (
    MediaFormatTypeVisualCodingFormatValue,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaFormatTypeVisualCodingFormat(ControlledTermUseType):
    class Meta:
        global_type = False

    color_domain: MediaFormatTypeVisualCodingFormatValue = field(
        default=MediaFormatTypeVisualCodingFormatValue.COLOR,
        metadata={
            "name": "colorDomain",
            "type": "Attribute",
        },
    )
