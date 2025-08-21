from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.base_segment_group_type_type import (
    BaseSegmentGroupTypeType,
)
from schema.tva.metadata.pkg_2019.segment_group_type_type_value import (
    SegmentGroupTypeTypeValue,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class SegmentGroupTypeType(BaseSegmentGroupTypeType):
    value: Optional[SegmentGroupTypeTypeValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
