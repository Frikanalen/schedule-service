from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.agent_type import AgentType
from schema.tva.mpeg7.pkg_2008.controlled_term_use_type import (
    ControlledTermUseType,
)
from schema.tva.mpeg7.pkg_2008.reference_type import ReferenceType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class MediaAgentType:
    role: Optional[ControlledTermUseType] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "required": True,
        },
    )
    agent: Optional[AgentType] = field(
        default=None,
        metadata={
            "name": "Agent",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    agent_ref: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "AgentRef",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
