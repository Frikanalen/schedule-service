from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.reference_type import ReferenceType
from schema.tva.mpeg7.pkg_2008.unique_idtype import UniqueIdtype
from schema.tva.mpeg7.pkg_2008.user_action_type_action_time import (
    UserActionTypeActionTime,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class UserActionType(Dstype):
    action_time: Optional[UserActionTypeActionTime] = field(
        default=None,
        metadata={
            "name": "ActionTime",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    program_identifier: Optional[UniqueIdtype] = field(
        default=None,
        metadata={
            "name": "ProgramIdentifier",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "required": True,
        },
    )
    action_data_item: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "ActionDataItem",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
