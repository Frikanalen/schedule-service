from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlPeriod

from schema.tva.metadata.pkg_2019.award_type import AwardType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class AwardsListItemType:
    title: Optional[TextualType] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "required": True,
        },
    )
    year: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
            "required": True,
        },
    )
    award: list[AwardType] = field(
        default_factory=list,
        metadata={
            "name": "Award",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
