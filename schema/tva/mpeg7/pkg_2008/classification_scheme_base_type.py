from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.reference_type import ReferenceType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class ClassificationSchemeBaseType(Dstype):
    import_value: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Import",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    domain: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "pattern": r"(/|((//|/)(((child::)?((\i\c*:)?(\i\c*|\*)))|\.))*)(\|(/|((//|/)(((child::)?((\i\c*:)?(\i\c*|\*)))|\.))*))*",
            "tokens": True,
        },
    )
