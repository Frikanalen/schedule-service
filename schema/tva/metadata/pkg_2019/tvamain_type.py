from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.classification_scheme_table_type import (
    ClassificationSchemeTableType,
)
from schema.tva.metadata.pkg_2019.metadata_origination_information_table_type import (
    MetadataOriginationInformationTableType,
)
from schema.tva.metadata.pkg_2019.program_description_type import (
    ProgramDescriptionType,
)
from schema.tva.metadata.pkg_2019.tvamain_type_type import TvamainTypeType
from schema.tva.metadata.pkg_2019.user_description_type import (
    UserDescriptionType,
)
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvamainType:
    class Meta:
        name = "TVAMainType"

    copyright_notice: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "CopyrightNotice",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    metadata_origination_information_table: Optional[
        MetadataOriginationInformationTableType
    ] = field(
        default=None,
        metadata={
            "name": "MetadataOriginationInformationTable",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    classification_scheme_table: Optional[ClassificationSchemeTableType] = (
        field(
            default=None,
            metadata={
                "name": "ClassificationSchemeTable",
                "type": "Element",
                "namespace": "urn:tva:metadata:2019",
            },
        )
    )
    program_description: Optional[ProgramDescriptionType] = field(
        default=None,
        metadata={
            "name": "ProgramDescription",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    user_description: list[UserDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "UserDescription",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    publisher: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publication_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publicationTime",
            "type": "Attribute",
        },
    )
    rights_owner: Optional[str] = field(
        default=None,
        metadata={
            "name": "rightsOwner",
            "type": "Attribute",
        },
    )
    origin_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "originID",
            "type": "Attribute",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[TvamainTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
