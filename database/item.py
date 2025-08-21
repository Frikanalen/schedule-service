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
