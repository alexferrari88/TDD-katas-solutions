from .utils import *
import time

NO_POSTS = "{} has currently no posts."
USER_NOT_EXIST = "User {} does not exist"


class Entry:
    def __init__(self, msg: str, when: float) -> None:
        self.msg = msg
        self.when = when


class SocialNetworking:
    def __init__(self) -> None:
        self.users = {}

    def get_or_create_user(self, name: str) -> None:
        if name not in self.users:
            self.users[name] = User(name)
        return self.users[name]


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.timeline = []

    def post(self, msg: str) -> None:
        self.timeline.append(Entry(msg, time.time()))
        print(f"{self.name} -> {msg}")

    def get_timeline(self) -> None:
        if not self.timeline:
            print(NO_POSTS.format(self.name))
            return
        for post in self.timeline:
            human_timestamp = get_human_timestamp(post.when)
            print(f"{post.msg} ({human_timestamp})")