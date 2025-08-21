from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.credits_item_type import CreditsItemType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class AwardType:
    category: Optional[TextualType] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "required": True,
        },
    )
    nominee: Optional[CreditsItemType] = field(
        default=None,
        metadata={
            "name": "Nominee",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    recipient: Optional[CreditsItemType] = field(
        default=None,
        metadata={
            "name": "Recipient",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    nominated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Nominated",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    awarded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Awarded",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
