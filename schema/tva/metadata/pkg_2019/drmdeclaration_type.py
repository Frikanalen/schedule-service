from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.extended_uritype import ExtendedUritype

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class DrmdeclarationType:
    class Meta:
        name = "DRMDeclarationType"

    drm: Optional[ExtendedUritype] = field(
        default=None,
        metadata={
            "name": "DRM",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    license_locator: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicenseLocator",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    license_expression: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicenseExpression",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
