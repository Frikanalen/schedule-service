from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.avattributes_type import AvattributesType
from schema.tva.metadata.pkg_2019.related_material_type_format_still_picture_format import (
    RelatedMaterialTypeFormatStillPictureFormat,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class RelatedMaterialTypeFormat:
    class Meta:
        global_type = False

    avattributes: Optional[AvattributesType] = field(
        default=None,
        metadata={
            "name": "AVAttributes",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    still_picture_format: Optional[
        RelatedMaterialTypeFormatStillPictureFormat
    ] = field(
        default=None,
        metadata={
            "name": "StillPictureFormat",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
