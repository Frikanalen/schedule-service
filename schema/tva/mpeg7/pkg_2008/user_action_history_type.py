from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.time_type import TimeType
from schema.tva.mpeg7.pkg_2008.user_action_list_type import UserActionListType
from schema.tva.mpeg7.pkg_2008.user_choice_type import UserChoiceType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class UserActionHistoryType(Dstype):
    observation_period: list[TimeType] = field(
        default_factory=list,
        metadata={
            "name": "ObservationPeriod",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    user_action_list: list[UserActionListType] = field(
        default_factory=list,
        metadata={
            "name": "UserActionList",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "min_occurs": 1,
        },
    )
    protected: UserChoiceType = field(
        default=UserChoiceType.TRUE,
        metadata={
            "type": "Attribute",
        },
    )
