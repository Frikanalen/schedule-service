from dataclasses import dataclass, field
from typing import Optional, Union

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)
from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.place_type_administrative_unit import (
    PlaceTypeAdministrativeUnit,
)
from schema.tva.mpeg7.pkg_2008.place_type_geographic_position import (
    PlaceTypeGeographicPosition,
)
from schema.tva.mpeg7.pkg_2008.place_type_postal_address import (
    PlaceTypePostalAddress,
)
from schema.tva.mpeg7.pkg_2008.term_use_type import TermUseType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class PlaceType(Dstype):
    name: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    name_term: list[ControlledTermUseType] = field(
        default_factory=list,
        metadata={
            "name": "NameTerm",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    role: Optional[TermUseType] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    geographic_position: Optional[PlaceTypeGeographicPosition] = field(
        default=None,
        metadata={
            "name": "GeographicPosition",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    region: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "white_space": "collapse",
            "pattern": r"[a-zA-Z]{2}(-[a-zA-Z0-9]{1,3})?",
        },
    )
    administrative_unit: list[PlaceTypeAdministrativeUnit] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeUnit",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    postal_address: Optional[PlaceTypePostalAddress] = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    internal_coordinates: Optional[str] = field(
        default=None,
        metadata={
            "name": "InternalCoordinates",
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
