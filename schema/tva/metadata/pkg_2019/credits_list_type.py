from dataclasses import dataclass, field

from schema.tva.metadata.pkg_2019.credits_item_type import CreditsItemType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class CreditsListType:
    credits_item: list[CreditsItemType] = field(
        default_factory=list,
        metadata={
            "name": "CreditsItem",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
