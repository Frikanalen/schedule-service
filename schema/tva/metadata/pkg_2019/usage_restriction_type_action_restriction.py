from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class UsageRestrictionTypeActionRestriction(ControlledTermUseType):
    class Meta:
        global_type = False

    activation_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "activationFlag",
            "type": "Attribute",
        },
    )
