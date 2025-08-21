from dataclasses import dataclass, field
from typing import Optional, Union

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.review_type import ReviewType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ProgramReviewTableType:
    review: list[ReviewType] = field(
        default_factory=list,
        metadata={
            "name": "Review",
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
