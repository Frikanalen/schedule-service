from dataclasses import dataclass, field
from typing import Optional, Union

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.metadata_origination_information_type import (
    MetadataOriginationInformationType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class MetadataOriginationInformationTableType:
    metadata_origination_information: list[
        MetadataOriginationInformationType
    ] = field(
        default_factory=list,
        metadata={
            "name": "MetadataOriginationInformation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
