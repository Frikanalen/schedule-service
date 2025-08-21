from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.controlled_term_type import (
    ControlledTermType,
)
from schema.tva.metadata.pkg_2019.device_type import DeviceType
from schema.tva.metadata.pkg_2019.rights_statement_type_rights_link import (
    RightsStatementTypeRightsLink,
)
from schema.tva.metadata.pkg_2019.rights_statement_type_temporal_scope import (
    RightsStatementTypeTemporalScope,
)
from schema.tva.metadata.pkg_2019.tvaagent_type import TvaagentType
from schema.tva.metadata.pkg_2019.usage_restriction_type import (
    UsageRestrictionType,
)
from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class RightsStatementType:
    rights_expression: list[TextualType] = field(
        default_factory=list,
        metadata={
            "name": "RightsExpression",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    rights_link: list[RightsStatementTypeRightsLink] = field(
        default_factory=list,
        metadata={
            "name": "RightsLink",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    rights_type: Optional[ControlledTermType] = field(
        default=None,
        metadata={
            "name": "RightsType",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    rights_contact: list[TvaagentType] = field(
        default_factory=list,
        metadata={
            "name": "RightsContact",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    temporal_scope: Optional[RightsStatementTypeTemporalScope] = field(
        default=None,
        metadata={
            "name": "TemporalScope",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    geographical_scope: list[ControlledTermUseType] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalScope",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    geographical_exclusion_scope: list[ControlledTermUseType] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalExclusionScope",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    usage_restriction: list[UsageRestrictionType] = field(
        default_factory=list,
        metadata={
            "name": "UsageRestriction",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    device: list[DeviceType] = field(
        default_factory=list,
        metadata={
            "name": "Device",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    program_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "programId",
            "type": "Attribute",
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        },
    )
    segment_ref_list: list[str] = field(
        default_factory=list,
        metadata={
            "name": "segmentRefList",
            "type": "Attribute",
            "tokens": True,
        },
    )
    instance_metadata_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstanceMetadataIdRef",
            "type": "Attribute",
            "pattern": r"(i|I)(m|M)(i|I):(([^/]+)/)?([^/]+)",
        },
    )
