from dataclasses import dataclass
from zoneinfo import ZoneInfo

import psycopg
import pytz
from psycopg.rows import namedtuple_row
from datetime import datetime
import os

from xsdata.formats.dataclass.serializers import XmlSerializer


@dataclass
class Organization:
    ID: int
    name: str


@dataclass
class Video:
    id: int
    name: str


class UnconfiguredEnvironment(Exception):
    """base class for new exception"""

    pass


def get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if database_url is None:
        raise UnconfiguredEnvironment("DATABASE_URL must be set")
    return database_url


@dataclass
class ScheduledVideoDict:
    CRID: str
    video: Video
    organization: Organization
    reason: str
    start_time: datetime
    end_time: datetime


@dataclass
class ScheduleDict:
    date: datetime
    entries: list[ScheduledVideoDict]


class Schedule:
    def __init__(self):
        self.conn = psycopg.connect(get_database_url())

    def get_date(self, date) -> ScheduleDict:
        query = """
            SELECT
                i.video_id,
                v.name AS video_name,
                v.organization_id,
                o.name AS organization_name,
                i.schedulereason,
                i.starttime,
                (i.starttime + i.duration) AS endtime,
                date_trunc('day', i.starttime) AS perceived_start_date,
                date_trunc('day', %s) AS perceived_query_date
            FROM fk_scheduleitem AS i
            JOIN fk_video AS v ON (video_id = v.id)
            JOIN fk_organization AS o ON (v.organization_id = o.id)
            WHERE date_trunc('day', i.starttime AT TIME ZONE 'Europe/Oslo')
                  = date_trunc('day', %s AT TIME ZONE 'Europe/Oslo')
            ORDER BY i.starttime ASC;
        """

        schedule = ScheduleDict(date=date, entries=[])

        with self.conn.cursor(row_factory=namedtuple_row) as cur:
            cur.execute(query, (date, date))
            rows = cur.fetchall()

        for r in rows:
            schedule.entries.append(
                ScheduledVideoDict(
                    CRID=f"crid://frikanalen.no/{r.video_id}",
                    video=Video(id=r.video_id, name=r.video_name),
                    organization=Organization(ID=r.organization_id, name=r.organization_name),
                    reason=r.schedulereason,
                    start_time=r.starttime.astimezone(ZoneInfo("Europe/Oslo")),
                    end_time=r.endtime.astimezone(ZoneInfo("Europe/Oslo")),
                )
            )

        return schedule


if __name__ == "__main__":
    s = Schedule()
    x = XmlSerializer()

    print(x.render(s.get_date(datetime.now(tz=pytz.timezone("Europe/Oslo")))))

