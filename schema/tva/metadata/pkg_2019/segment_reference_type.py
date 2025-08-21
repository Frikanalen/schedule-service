from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.segment_type_type import SegmentTypeType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class SegmentReferenceType:
    segment_type: SegmentTypeType = field(
        default=SegmentTypeType.SEGMENT,
        metadata={
            "name": "segmentType",
            "type": "Attribute",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
