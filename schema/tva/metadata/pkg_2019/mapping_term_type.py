from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class MappingTermType:
    classification_scheme_acronym: Optional[TextualType] = field(
        default=None,
        metadata={
            "name": "ClassificationSchemeAcronym",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    classification_scheme_name: Optional[TextualType] = field(
        default=None,
        metadata={
            "name": "ClassificationSchemeName",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    classification_scheme_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassificationSchemeURL",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    original_term_name: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "OriginalTermName",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    original_term_definition: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "OriginalTermDefinition",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    mapping_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MappingDate",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    original_term_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "originalTermID",
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r":[^:]+:[^:]+",
        },
    )
