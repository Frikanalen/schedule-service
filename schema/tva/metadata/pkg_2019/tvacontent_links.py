from dataclasses import dataclass, field

from schema.tva.metadata.pkg_2019.related_material_type import (
    RelatedMaterialType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvacontentLinks:
    class Meta:
        name = "TVAContentLinks"
        namespace = "urn:tva:metadata:2019"

    related_material: list[RelatedMaterialType] = field(
        default_factory=list,
        metadata={
            "name": "RelatedMaterial",
            "type": "Element",
            "min_occurs": 1,
        },
    )
