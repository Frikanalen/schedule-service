from datetime import datetime, timedelta, time
from zoneinfo import ZoneInfo

from xsdata.models.datatype import XmlDateTime

from database import schedule
from database.schedule import ScheduleDict
from schema.tva.metadata.pkg_2019 import (
    MetadataOriginationInformationType,
    MetadataOriginationInformationTableType,
    Tvamain,
    ProgramDescriptionType,
    ProgramLocationTableType,
    ScheduleType,
    ScheduleEventType,
    CridrefType,
    ProgramInformationTableType,
    ProgramInformationType,
    BasicContentDescriptionType,
    ServiceInformationTableType,
    ServiceInformationType,
    ServiceInformationNameType,
)
from schema.tva.mpeg7.pkg_2008 import TextualType, TitleType


def crid(video_id: int) -> str:
    return f"crid://frikanalen.no/{video_id}"


tz = ZoneInfo("Europe/Oslo")


def day_start(d: datetime) -> datetime:
    return datetime.combine(d, time.min, tzinfo=tz)


def day_end(d: datetime) -> datetime:
    return day_start(d) + timedelta(days=1)


def get_tv_anytime(schedule_for_day: ScheduleDict):
    return Tvamain(
        rights_owner="",
        lang="no",
        publisher="Foreningen Frikanalen, Tore Sinding Bekkedal",
        publication_time=XmlDateTime.now(),
        metadata_origination_information_table=MetadataOriginationInformationTableType(
            metadata_origination_information=[
                MetadataOriginationInformationType(
                    publisher=[TextualType("Foreningen Frikanalen")],
                    rights_owner=[TextualType("Foreningen Frikanalen")],
                )
            ]
        ),
        program_description=ProgramDescriptionType(
            service_information_table=ServiceInformationTableType(
                service_information=[
                    ServiceInformationType(
                        service_id="frikanalen.no", name=[ServiceInformationNameType("Frikanalen")]
                    )
                ]
            ),
            program_information_table=ProgramInformationTableType(
                program_information=[
                    ProgramInformationType(
                        program_id=crid(x.video.id),
                        basic_description=BasicContentDescriptionType(
                            title=[TitleType(f"{x.organization.name}: ${x.video.name}")]
                        ),
                    )
                    for x in schedule_for_day.entries
                ]
            ),
            program_location_table=ProgramLocationTableType(
                schedule=[
                    ScheduleType(
                        service_idref=["frikanalen.no"],
                        start=XmlDateTime.from_datetime(day_start(schedule_for_day.date)),
                        end=XmlDateTime.from_datetime(day_end(schedule_for_day.date)),
                        schedule_event=[
                            ScheduleEventType(
                                published_start_time=XmlDateTime.from_datetime(item.start_time),
                                published_end_time=XmlDateTime.from_datetime(item.end_time),
                                actual_start_time=XmlDateTime.from_datetime(item.start_time),
                                actual_end_time=XmlDateTime.from_datetime(item.end_time),
                                program=CridrefType(crid=crid(item.video.id)),
                            )
                            for item in schedule_for_day.entries
                        ],
                    )
                ]
            ),
        ),
    )


if __name__ == "__main__":
    s = schedule.Schedule()
    todays_schedule = s.get_date(datetime.now())
    foo = get_tv_anytime(todays_schedule)
    print(foo)
