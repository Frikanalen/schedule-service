from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.service_information_type_service_url_name import (
    ServiceInformationTypeServiceUrlName,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ServiceInformationTypeServiceUrl:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name: Optional[ServiceInformationTypeServiceUrlName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
