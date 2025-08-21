from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.source_preferences_type_dissemination_date import (
    SourcePreferencesTypeDisseminationDate,
)
from schema.tva.mpeg7.pkg_2008.source_preferences_type_dissemination_format import (
    SourcePreferencesTypeDisseminationFormat,
)
from schema.tva.mpeg7.pkg_2008.source_preferences_type_dissemination_location import (
    SourcePreferencesTypeDisseminationLocation,
)
from schema.tva.mpeg7.pkg_2008.source_preferences_type_dissemination_source import (
    SourcePreferencesTypeDisseminationSource,
)
from schema.tva.mpeg7.pkg_2008.source_preferences_type_disseminator import (
    SourcePreferencesTypeDisseminator,
)
from schema.tva.mpeg7.pkg_2008.source_preferences_type_media_format import (
    SourcePreferencesTypeMediaFormat,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class SourcePreferencesType(Dstype):
    dissemination_format: list[SourcePreferencesTypeDisseminationFormat] = (
        field(
            default_factory=list,
            metadata={
                "name": "DisseminationFormat",
                "type": "Element",
                "namespace": "urn:tva:mpeg7:2008",
            },
        )
    )
    dissemination_source: list[SourcePreferencesTypeDisseminationSource] = (
        field(
            default_factory=list,
            metadata={
                "name": "DisseminationSource",
                "type": "Element",
                "namespace": "urn:tva:mpeg7:2008",
            },
        )
    )
    dissemination_location: list[
        SourcePreferencesTypeDisseminationLocation
    ] = field(
        default_factory=list,
        metadata={
            "name": "DisseminationLocation",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    dissemination_date: list[SourcePreferencesTypeDisseminationDate] = field(
        default_factory=list,
        metadata={
            "name": "DisseminationDate",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    disseminator: list[SourcePreferencesTypeDisseminator] = field(
        default_factory=list,
        metadata={
            "name": "Disseminator",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    media_format: list[SourcePreferencesTypeMediaFormat] = field(
        default_factory=list,
        metadata={
            "name": "MediaFormat",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    no_repeat: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noRepeat",
            "type": "Attribute",
        },
    )
    no_encryption: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noEncryption",
            "type": "Attribute",
        },
    )
    no_pay_per_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noPayPerUse",
            "type": "Attribute",
        },
    )
    preference_value: int = field(
        default=10,
        metadata={
            "name": "preferenceValue",
            "type": "Attribute",
            "min_inclusive": -100,
            "max_inclusive": 100,
        },
    )
