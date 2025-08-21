from dataclasses import dataclass, field

from schema.tva.metadata.pkg_2019.explanation_type import ExplanationType
from schema.tva.mpeg7.pkg_2008.parental_guidance_type import (
    ParentalGuidanceType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvaparentalGuidanceType(ParentalGuidanceType):
    class Meta:
        name = "TVAParentalGuidanceType"

    explanatory_text: list[ExplanationType] = field(
        default_factory=list,
        metadata={
            "name": "ExplanatoryText",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
