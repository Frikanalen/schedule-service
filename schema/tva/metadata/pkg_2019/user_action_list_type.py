from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.user_action_type import UserActionType
from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.term_use_type import TermUseType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class UserActionListType(Dstype):
    action_type: Optional[TermUseType] = field(
        default=None,
        metadata={
            "name": "ActionType",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    user_action: list[UserActionType] = field(
        default_factory=list,
        metadata={
            "name": "UserAction",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    num_of_instances: Optional[int] = field(
        default=None,
        metadata={
            "name": "numOfInstances",
            "type": "Attribute",
        },
    )
    total_duration: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalDuration",
            "type": "Attribute",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?((\-|\+)\d{2}:\d{2}Z)?",
        },
    )
