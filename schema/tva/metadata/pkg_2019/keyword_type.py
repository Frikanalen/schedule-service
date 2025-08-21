from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.keyword_type_type import KeywordTypeType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class KeywordType(TextualType):
    type_value: KeywordTypeType = field(
        default=KeywordTypeType.MAIN,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    metadata_origin_idref: Optional[str] = field(
        default=None,
        metadata={
            "name": "metadataOriginIDRef",
            "type": "Attribute",
        },
    )
