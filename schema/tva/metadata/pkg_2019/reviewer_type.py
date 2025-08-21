from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.tvaagent_type import TvaagentType
from schema.tva.mpeg7.pkg_2008.textual_type import TextualType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ReviewerType(TvaagentType):
    publication: Optional[TextualType] = field(
        default=None,
        metadata={
            "name": "Publication",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
