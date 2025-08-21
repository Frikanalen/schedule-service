from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.credits_information_table_type import (
    CreditsInformationTableType,
)
from schema.tva.metadata.pkg_2019.group_information_table_type import (
    GroupInformationTableType,
)
from schema.tva.metadata.pkg_2019.program_information_table_type import (
    ProgramInformationTableType,
)
from schema.tva.metadata.pkg_2019.program_location_table_type import (
    ProgramLocationTableType,
)
from schema.tva.metadata.pkg_2019.program_review_table_type import (
    ProgramReviewTableType,
)
from schema.tva.metadata.pkg_2019.purchase_information_table_type import (
    PurchaseInformationTableType,
)
from schema.tva.metadata.pkg_2019.rights_information_table_type import (
    RightsInformationTableType,
)
from schema.tva.metadata.pkg_2019.segment_information_table_type import (
    SegmentInformationTableType,
)
from schema.tva.metadata.pkg_2019.service_information_table_type import (
    ServiceInformationTableType,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ProgramDescriptionType:
    program_information_table: Optional[ProgramInformationTableType] = field(
        default=None,
        metadata={
            "name": "ProgramInformationTable",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    group_information_table: Optional[GroupInformationTableType] = field(
        default=None,
        metadata={
            "name": "GroupInformationTable",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    program_location_table: Optional[ProgramLocationTableType] = field(
        default=None,
        metadata={
            "name": "ProgramLocationTable",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    service_information_table: Optional[ServiceInformationTableType] = field(
        default=None,
        metadata={
            "name": "ServiceInformationTable",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    credits_information_table: Optional[CreditsInformationTableType] = field(
        default=None,
        metadata={
            "name": "CreditsInformationTable",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    program_review_table: Optional[ProgramReviewTableType] = field(
        default=None,
        metadata={
            "name": "ProgramReviewTable",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    segment_information_table: Optional[SegmentInformationTableType] = field(
        default=None,
        metadata={
            "name": "SegmentInformationTable",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    purchase_information_table: Optional[PurchaseInformationTableType] = field(
        default=None,
        metadata={
            "name": "PurchaseInformationTable",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    rights_information_table: Optional[RightsInformationTableType] = field(
        default=None,
        metadata={
            "name": "RightsInformationTable",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
