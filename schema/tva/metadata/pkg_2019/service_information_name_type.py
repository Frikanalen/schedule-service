from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.service_information_name_length_type import (
    ServiceInformationNameLengthType,
)
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ServiceInformationNameType(TextualType):
    length: Optional[ServiceInformationNameLengthType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
