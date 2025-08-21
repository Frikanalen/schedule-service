from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class InlineMediaType:
    media_data16: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MediaData16",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "format": "base16",
        },
    )
    media_data64: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MediaData64",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "format": "base64",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r'[!-\x7f-[\(\)<>@,;:\\"/\[\]\?=]]+/[!-\x7f-[\(\)<>@,;:\\"/\[\]\?=]]+',
        },
    )
