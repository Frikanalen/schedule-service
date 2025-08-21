from dataclasses import dataclass, field
from typing import Optional, Union

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.organization_name_type import (
    OrganizationNameType,
)
from schema.tva.metadata.pkg_2019.person_name_fragment_type import (
    PersonNameFragmentType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class CreditsInformationTableType:
    person_name: list[PersonNameFragmentType] = field(
        default_factory=list,
        metadata={
            "name": "PersonName",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    organization_name: list[OrganizationNameType] = field(
        default_factory=list,
        metadata={
            "name": "OrganizationName",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    copyright_notice: Optional[str] = field(
        default=None,
        metadata={
            "name": "copyrightNotice",
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
