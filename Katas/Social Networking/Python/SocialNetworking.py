from datetime import datetime
import dateutil.relativedelta
import time

NO_POSTS = "There are currently no posts on this timeline."
USER_NOT_EXIST = "User {} does not exist"


class Entry:
    def __init__(self, msg: str, when: float) -> None:
        self.msg = msg
        self.when = when


class SocialNetworking:
    timeline = {}

    def post(self, user: str, message: str) -> None:
        self.timeline.setdefault(user, []).append(Entry(msg=message, when=time.time()))
        print(f"{user} -> {message}")

    def read(self, user: str) -> None:
        posts = self.timeline.get(user, [])
        if not posts:
            print(USER_NOT_EXIST.format(user))
            return
        for post in posts:
            delta = int(time.time() - post.when)
            plural = "s" if 1 < delta < 60 or delta > 60 else ""
            time_name = "second" if 0 <= delta < 60 else "minute"
            if delta >= 60:
                delta //= 60
            print(f"{post.msg} ({delta} {time_name}{plural} ago)")