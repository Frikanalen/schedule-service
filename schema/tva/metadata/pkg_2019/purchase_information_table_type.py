from dataclasses import dataclass, field
from typing import Optional, Union

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.purchase_information_type import (
    PurchaseInformationType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class PurchaseInformationTableType:
    purchase_information: list[PurchaseInformationType] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseInformation",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    metadata_origin_idref: Optional[str] = field(
        default=None,
        metadata={
            "name": "metadataOriginIDRef",
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
