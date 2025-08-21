from dataclasses import dataclass, field
from typing import Optional, Union

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.mpeg7.pkg_2008.name_component_type import NameComponentType
from schema.tva.mpeg7.pkg_2008.person_name_type_type import PersonNameTypeType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class PersonNameType:
    given_name: list[NameComponentType] = field(
        default_factory=list,
        metadata={
            "name": "GivenName",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    linking_name: list[NameComponentType] = field(
        default_factory=list,
        metadata={
            "name": "LinkingName",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    family_name: list[NameComponentType] = field(
        default_factory=list,
        metadata={
            "name": "FamilyName",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    title: list[NameComponentType] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    salutation: list[NameComponentType] = field(
        default_factory=list,
        metadata={
            "name": "Salutation",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    numeration: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Numeration",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    date_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "dateFrom",
            "type": "Attribute",
            "pattern": r"(\-?\d+(\-\d{2}(\-\d{2})?)?)?(T\d{2}(:\d{2}(:\d{2}(:\d+)?)?)?)?(F\d+)?((\-|\+)\d{2}:\d{2})?",
        },
    )
    date_to: Optional[str] = field(
        default=None,
        metadata={
            "name": "dateTo",
            "type": "Attribute",
            "pattern": r"(\-?\d+(\-\d{2}(\-\d{2})?)?)?(T\d{2}(:\d{2}(:\d{2}(:\d+)?)?)?)?(F\d+)?((\-|\+)\d{2}:\d{2})?",
        },
    )
    type_value: Optional[PersonNameTypeType] = field(
        default=None,
        metadata={
            "name": "type",
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
