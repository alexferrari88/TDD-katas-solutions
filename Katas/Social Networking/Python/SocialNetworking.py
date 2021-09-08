from typing import List, Set
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
        self.name: str = name
        self.timeline: List[Entry] = []
        self.following: Set[User] = set()

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

    def follow(self, who) -> None:
        self.following.add(who)

    def display_wall(self) -> None:
        timelines = {f"{entry.when}__{self.name}": entry.msg for entry in self.timeline}

        for user in self.following:
            for entry in user.timeline:
                timelines[f"{entry.when}__{user.name}"] = entry.msg

        for wall_entry in reversed(sorted(timelines.items())):
            timestamp, user_name = wall_entry[0].split("__")
            human_timestamp = get_human_timestamp(float(timestamp))
            print(f"{user_name} - {wall_entry[1]} ({human_timestamp})")
