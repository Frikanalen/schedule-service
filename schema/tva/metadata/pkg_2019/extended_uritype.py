from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ExtendedUritype:
    class Meta:
        name = "ExtendedURIType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r'[!-\x7f-[\(\)<>@,;:\\"/\[\]\?=]]+/[!-\x7f-[\(\)<>@,;:\\"/\[\]\?=]]+',
        },
    )
    uri_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "uriType",
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
