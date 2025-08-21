from dataclasses import dataclass, field
from typing import Optional, Union

from schema.org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from schema.tva.metadata.pkg_2019.broadcast_event_type import (
    BroadcastEventType,
)
from schema.tva.metadata.pkg_2019.on_demand_program_type import (
    OnDemandProgramType,
)
from schema.tva.metadata.pkg_2019.on_demand_service_type import (
    OnDemandServiceType,
)
from schema.tva.metadata.pkg_2019.push_download_type import PushDownloadType
from schema.tva.metadata.pkg_2019.schedule_type import ScheduleType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ProgramLocationTableType:
    schedule: list[ScheduleType] = field(
        default_factory=list,
        metadata={
            "name": "Schedule",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    broadcast_event: list[BroadcastEventType] = field(
        default_factory=list,
        metadata={
            "name": "BroadcastEvent",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    on_demand_program: list[OnDemandProgramType] = field(
        default_factory=list,
        metadata={
            "name": "OnDemandProgram",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    on_demand_service: list[OnDemandServiceType] = field(
        default_factory=list,
        metadata={
            "name": "OnDemandService",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    push_download_program: list[PushDownloadType] = field(
        default_factory=list,
        metadata={
            "name": "PushDownloadProgram",
            "type": "Element",
            "namespace": "urn:tva:metadata:2019",
        },
    )
    metadata_origin_idref: Optional[str] = field(
        default=None,
        metadata={
            "name": "metadataOriginIDRef",
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
