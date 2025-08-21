from dataclasses import dataclass, field

from schema.tva.metadata.pkg_2019.segment_group_information_type import (
    SegmentGroupInformationType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class SegmentGroupListType:
    segment_group_information: list[SegmentGroupInformationType] = field(
        default_factory=list,
        metadata={
            "name": "SegmentGroupInformation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
