from dataclasses import dataclass, field

from schema.tva.metadata.pkg_2019.segment_information_type import (
    SegmentInformationType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class SegmentListType:
    segment_information: list[SegmentInformationType] = field(
        default_factory=list,
        metadata={
            "name": "SegmentInformation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
