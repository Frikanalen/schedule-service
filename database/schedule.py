from zoneinfo import ZoneInfo

import psycopg
import pytz
from psycopg.rows import namedtuple_row
from datetime import datetime
import os


class Organization:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name


class Video:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.CRID = "crid://frikanalen.no/{}".format(ID)

    def __repr__(self):
        return 'Video[ID={},name="{}"]'.format(self.ID, self.name)


class ScheduleItem:
    def __repr__(self):
        s = "ScheduleItem["
        if self.start_time and self.end_time:
            s += self.start_time.strftime("[%d %H:%M-")
            s += self.end_time.strftime("%H:%M]")
        if self.video:
            s += self.video.__repr__()
        s += "]"
        return s

    def __init__(self):
        self.video = None
        self.start_time = None
        self.end_time = None
        self.organization = None


class ScheduledVideo(ScheduleItem):
    def __getstate__(self):
        return {
            "videoID": self.video.ID,
            "startTime": self.start_time,
            "endTime": self.end_time,
            "name": self.video.name,
            "type": "video",
        }


class Graphics(ScheduleItem):
    def __getstate__(self):
        return {
            "url": self.URL,
            "startTime": self.start_time,
            "endTime": self.end_time,
            "type": "graphics",
        }


class UnconfiguredEnvironment(Exception):
    """base class for new exception"""

    pass


def get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if database_url is None:
        raise UnconfiguredEnvironment("DATABASE_URL must be set")
    return database_url


class Schedule:
    def __init__(self):
        self.conn = psycopg.connect(get_database_url())

    def get_date(self, date) -> dict[str, any]:
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

        schedule = {"date": date, "items": []}

        with self.conn.cursor(row_factory=namedtuple_row) as cur:
            cur.execute(query, (date, date))
            rows = cur.fetchall()

        for r in rows:
            item = ScheduledVideo()
            item.CRID = f"crid://frikanalen.no/{r.video_id}"
            item.video = Video(ID=r.video_id, name=r.video_name)
            item.organization = Organization(ID=r.organization_id, name=r.organization_name)
            item.reason = r.schedulereason
            item.start_time = r.starttime.astimezone(ZoneInfo("Europe/Oslo"))
            item.end_time = r.endtime.astimezone(ZoneInfo("Europe/Oslo"))
            schedule["items"].append(item)

        return schedule


if __name__ == "__main__":
    s = Schedule()
    print(s.get_date(datetime.now(tz=pytz.timezone("Europe/Oslo"))))
