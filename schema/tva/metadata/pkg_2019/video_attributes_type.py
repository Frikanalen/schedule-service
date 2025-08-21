from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.aspect_ratio_type import AspectRatioType
from schema.tva.metadata.pkg_2019.bit_rate_type import BitRateType
from schema.tva.metadata.pkg_2019.color_type import ColorType
from schema.tva.metadata.pkg_2019.controlled_term_type import (
    ControlledTermType,
)
from schema.tva.metadata.pkg_2019.scan_type import ScanType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class VideoAttributesType:
    coding: Optional[ControlledTermType] = field(
        default=None,
        metadata={
            "name": "Coding",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    scan: Optional[ScanType] = field(
        default=None,
        metadata={
            "name": "Scan",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    horizontal_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "HorizontalSize",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    vertical_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "VerticalSize",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    aspect_ratio: list[AspectRatioType] = field(
        default_factory=list,
        metadata={
            "name": "AspectRatio",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "max_occurs": 2,
        },
    )
    color: Optional[ColorType] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    frame_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrameRate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "pattern": r"([0-9]{1,3}(.[0-9]{1,3})?)|([0-9]{1,3}/1.001)",
        },
    )
    bit_rate: Optional[BitRateType] = field(
        default=None,
        metadata={
            "name": "BitRate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    picture_format: Optional[ControlledTermType] = field(
        default=None,
        metadata={
            "name": "PictureFormat",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
