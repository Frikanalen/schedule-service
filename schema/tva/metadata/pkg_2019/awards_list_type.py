from dataclasses import dataclass, field

from schema.tva.metadata.pkg_2019.awards_list_item_type import (
    AwardsListItemType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class AwardsListType:
    awards_list_item: list[AwardsListItemType] = field(
        default_factory=list,
        metadata={
            "name": "AwardsListItem",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "min_occurs": 1,
        },
    )
