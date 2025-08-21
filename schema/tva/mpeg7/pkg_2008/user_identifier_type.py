from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.textual_type import TextualType
from schema.tva.mpeg7.pkg_2008.user_choice_type import UserChoiceType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class UserIdentifierType:
    name: Optional[TextualType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "required": True,
        },
    )
    protected: UserChoiceType = field(
        default=UserChoiceType.TRUE,
        metadata={
            "type": "Attribute",
        },
    )
