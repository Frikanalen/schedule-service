from datetime import datetime


class Schedule:
    def __init__(self):
        self.db = Database()

    def get_for_date(self, date):
        query = """
            SELECT
                i.video_id,
                v.name as video_name,
                v.organization_id,
                o.name as organization_name,
                i.schedulereason,
                i.starttime,
                (i.starttime + i.duration) as endtime
            FROM fk_scheduleitem AS i
            JOIN fk_video AS v ON (video_id = v.id)
            JOIN fk_organization AS o ON (v.organization_id = o.id)
            WHERE (date_trunc('day', i.starttime) = date_trunc('day', %s))
            ORDER BY i.starttime ASC;"""
        cur = self.db.conn.cursor()
        cur.execute(query, (date,))
        schedule = {"date": date, "items": []}

        for item in cur.fetchall():
            new_item = ScheduledVideo()
            new_item.video = Video(ID=item[0], name=item[1])
            new_item.organization = Organization(ID=item[2], name=item[3])
            new_item.reason = item[4]
            new_item.start_time = item[5]
            new_item.end_time = item[6]
            new_item.CRID = "crid://frikanalen.no/%d" % (item[0],)
            schedule["items"].append(new_item)
        return schedule


if __name__ == "__main__":
    s = Schedule()
    print(s.get_for_date(datetime.now()))
