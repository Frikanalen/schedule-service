from dataclasses import dataclass, field

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaRelTimePointType:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?",
        },
    )
