from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from schema.tva.metadata.pkg_2019.usage_restriction_type_restriction_window_textual_expression import (
    UsageRestrictionTypeRestrictionWindowTextualExpression,
)
from schema.tva.metadata.pkg_2019.valid_period_type import ValidPeriodType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class UsageRestrictionTypeRestrictionWindow:
    class Meta:
        global_type = False

    textual_expression: Optional[
        UsageRestrictionTypeRestrictionWindowTextualExpression
    ] = field(
        default=None,
        metadata={
            "name": "TextualExpression",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    validity_period: Optional[ValidPeriodType] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    validity_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ValidityDuration",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
