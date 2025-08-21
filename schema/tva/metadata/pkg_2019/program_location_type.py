from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.cridref_type import CridrefType
from schema.tva.metadata.pkg_2019.extended_uritype import ExtendedUritype
from schema.tva.metadata.pkg_2019.instance_description_type import (
    InstanceDescriptionType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ProgramLocationType:
    program: Optional[CridrefType] = field(
        default=None,
        metadata={
            "name": "Program",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "required": True,
        },
    )
    program_url: Optional[ExtendedUritype] = field(
        default=None,
        metadata={
            "name": "ProgramURL",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    auxiliary_url: list[ExtendedUritype] = field(
        default_factory=list,
        metadata={
            "name": "AuxiliaryURL",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    instance_metadata_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstanceMetadataId",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "pattern": r"(i|I)(m|M)(i|I):(([^/]+)/)?([^/]+)",
        },
    )
    instance_description: Optional[InstanceDescriptionType] = field(
        default=None,
        metadata={
            "name": "InstanceDescription",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
