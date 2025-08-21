from dataclasses import dataclass, field
from typing import Optional, Union

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.csalias_type import CsaliasType
from schema.tva.metadata.pkg_2019.tvaclassification_scheme_type import (
    TvaclassificationSchemeType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ClassificationSchemeTableType:
    csalias: list[CsaliasType] = field(
        default_factory=list,
        metadata={
            "name": "CSAlias",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    classification_scheme: list[TvaclassificationSchemeType] = field(
        default_factory=list,
        metadata={
            "name": "ClassificationScheme",
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
