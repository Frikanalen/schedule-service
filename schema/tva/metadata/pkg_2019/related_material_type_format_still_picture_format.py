from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.controlled_term_type import (
    ControlledTermType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class RelatedMaterialTypeFormatStillPictureFormat(ControlledTermType):
    class Meta:
        global_type = False

    horizontal_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "horizontalSize",
            "type": "Attribute",
        },
    )
    vertical_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "verticalSize",
            "type": "Attribute",
        },
    )
