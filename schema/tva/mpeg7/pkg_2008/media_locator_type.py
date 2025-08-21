from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.inline_media_type import InlineMediaType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaLocatorType:
    media_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "MediaUri",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    inline_media: Optional[InlineMediaType] = field(
        default=None,
        metadata={
            "name": "InlineMedia",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    stream_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "StreamID",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
