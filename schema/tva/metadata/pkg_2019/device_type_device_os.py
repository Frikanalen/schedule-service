from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class DeviceTypeDeviceOs(ControlledTermUseType):
    class Meta:
        global_type = False

    blocked: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
