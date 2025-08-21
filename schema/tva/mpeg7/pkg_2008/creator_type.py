from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.media_agent_type import MediaAgentType
from schema.tva.mpeg7.pkg_2008.person_name_type import PersonNameType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class CreatorType(MediaAgentType):
    character: list[PersonNameType] = field(
        default_factory=list,
        metadata={
            "name": "Character",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
