from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.controlled_term_type import (
    ControlledTermType,
)
from schema.tva.metadata.pkg_2019.genre_type_type import GenreTypeType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class GenreType(ControlledTermType):
    type_value: GenreTypeType = field(
        default=GenreTypeType.MAIN,
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
