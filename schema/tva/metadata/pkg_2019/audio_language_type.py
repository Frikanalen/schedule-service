from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.extended_language_type import (
    ExtendedLanguageType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class AudioLanguageType(ExtendedLanguageType):
    purpose: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
