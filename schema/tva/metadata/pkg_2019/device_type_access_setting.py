from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class DeviceTypeAccessSetting:
    class Meta:
        global_type = False

    setting_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SettingDescription",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
