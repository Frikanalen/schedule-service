from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.usage_restriction_type_action_restriction import (
    UsageRestrictionTypeActionRestriction,
)
from schema.tva.metadata.pkg_2019.usage_restriction_type_restriction_window import (
    UsageRestrictionTypeRestrictionWindow,
)
from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class UsageRestrictionType:
    restriction_type: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "RestrictionType",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    restriction_sub_type: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "RestrictionSubType",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    restriction_window: Optional[UsageRestrictionTypeRestrictionWindow] = (
        field(
            default=None,
            metadata={
                "name": "RestrictionWindow",
                "type": "Element",
                "namespace": "urn:tva:metadata:2019",
            },
        )
    )
    action_restriction: list[UsageRestrictionTypeActionRestriction] = field(
        default_factory=list,
        metadata={
            "name": "ActionRestriction",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    restriction_status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RestrictionStatus",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "required": True,
        },
    )
