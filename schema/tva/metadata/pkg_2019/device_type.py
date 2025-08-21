from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.device_type_access_setting import (
    DeviceTypeAccessSetting,
)
from schema.tva.metadata.pkg_2019.device_type_access_status import (
    DeviceTypeAccessStatus,
)
from schema.tva.metadata.pkg_2019.device_type_device_os import (
    DeviceTypeDeviceOs,
)
from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class DeviceType:
    device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeviceName",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    device_brand: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeviceBrand",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    device_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeviceModel",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    device_type: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "DeviceType",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    device_os: list[DeviceTypeDeviceOs] = field(
        default_factory=list,
        metadata={
            "name": "DeviceOS",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    access_status: Optional[DeviceTypeAccessStatus] = field(
        default=None,
        metadata={
            "name": "AccessStatus",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    access_setting: list[DeviceTypeAccessSetting] = field(
        default_factory=list,
        metadata={
            "name": "AccessSetting",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    deviceid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
