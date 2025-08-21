from dataclasses import dataclass, field

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class SegmentsType:
    ref_list: list[str] = field(
        default_factory=list,
        metadata={
            "name": "refList",
            "type": "Attribute",
            "tokens": True,
        },
    )
