from dataclasses import dataclass, field
from typing import Optional, Union

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class TextualBaseType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
