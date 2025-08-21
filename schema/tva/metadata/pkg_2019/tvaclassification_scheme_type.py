from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.tvaterm_definition_type import (
    TvatermDefinitionType,
)
from schema.tva.mpeg7.pkg_2008.classification_scheme_base_type import (
    ClassificationSchemeBaseType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvaclassificationSchemeType(ClassificationSchemeBaseType):
    class Meta:
        name = "TVAClassificationSchemeType"

    term: list[TvatermDefinitionType] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "min_occurs": 1,
        },
    )
    fragment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "fragmentId",
            "type": "Attribute",
        },
    )
    fragment_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "fragmentVersion",
            "type": "Attribute",
        },
    )
    fragment_expiration_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "fragmentExpirationDate",
            "type": "Attribute",
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
