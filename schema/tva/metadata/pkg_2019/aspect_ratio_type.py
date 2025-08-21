from dataclasses import dataclass, field

from schema.tva.metadata.pkg_2019.aspect_ratio_type_type import (
    AspectRatioTypeType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class AspectRatioType:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d+:\d+",
        },
    )
    type_value: AspectRatioTypeType = field(
        default=AspectRatioTypeType.ORIGINAL,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
