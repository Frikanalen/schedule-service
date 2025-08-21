from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.extended_uritype import ExtendedUritype
from schema.tva.mpeg7.pkg_2008.inline_media_type import InlineMediaType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvamediaLocatorType:
    class Meta:
        name = "TVAMediaLocatorType"

    media_uri: Optional[ExtendedUritype] = field(
        default=None,
        metadata={
            "name": "MediaUri",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    auxiliary_uri: list[ExtendedUritype] = field(
        default_factory=list,
        metadata={
            "name": "AuxiliaryURI",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    inline_media: Optional[InlineMediaType] = field(
        default=None,
        metadata={
            "name": "InlineMedia",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    stream_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "StreamID",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
