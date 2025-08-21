from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.explanation_length_type import (
    ExplanationLengthType,
)
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ExplanationType(TextualType):
    length: Optional[ExplanationLengthType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
