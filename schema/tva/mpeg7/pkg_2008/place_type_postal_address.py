from dataclasses import dataclass, field
from typing import Optional, Union

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class PlaceTypePostalAddress:
    class Meta:
        global_type = False

    address_line: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "min_occurs": 1,
        },
    )
    posting_identifier: Optional[TextualType] = field(
        default=None,
        metadata={
            "name": "PostingIdentifier",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
