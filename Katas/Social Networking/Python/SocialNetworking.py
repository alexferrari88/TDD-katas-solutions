# https://github.com/sandromancuso/social_networking_kata
from typing import List, Optional, Set
from utils import *
import time
from IOOutput import IOOutput
from Console import Console

NO_POSTS = "{} has currently no posts."
USER_NOT_EXIST = "User {} does not exist"
HELP_MSG_TEXT = "Welcome to CLIbook!🌎\n"
COMMANDS_TEXT = (
    "Enter any of these commands:\n"
    + "Post as user: \t\t\t\t<username> -> <message>\n"
    + "Check a user's timeline😎: \t\tvisit <username>\n"
    + "Follow another user🤗: \t\t\tfollow <your username> <username to follow>\n"
    + "Check user's wall📃: \t\t\twall <username>\n"
    + "Get this help message again🆘: \t\thelp\n"
)


class Entry:
    def __init__(self, msg: str, when: float) -> None:
        self.msg = msg
        self.when = when


class SocialNetworking:
    def __init__(self, IO: Optional[IOOutput] = Console) -> None:
        self.users = {}
        self.IO = IO

    def get_or_create_user(self, name: str) -> None:
        if name not in self.users:
            self.users[name] = User(name, self.IO)
        return self.users[name]


class User:
    def __init__(self, name: str, IO: Optional[IOOutput] = Console) -> None:
        self.name: str = name
        self.timeline: List[Entry] = []
        self.following: Set[User] = set()
        self.IO = IO

    def post(self, msg: str) -> None:
        self.timeline.append(Entry(msg, time.time()))
        self.IO.write(f"{self.name} -> {msg}")

    def get_timeline(self) -> None:
        if not self.timeline:
            self.IO.write(NO_POSTS.format(self.name))
            return
        for post in self.timeline:
            human_timestamp = get_human_timestamp(post.when)
            self.IO.write(f"{post.msg} ({human_timestamp})")

    def follow(self, who) -> None:
        self.following.add(who)
        self.IO.write(f"{self.name} is now following {who.name}🤗")

    def display_wall(self) -> None:
        timelines = {f"{entry.when}__{self.name}": entry.msg for entry in self.timeline}

        for user in self.following:
            for entry in user.timeline:
                timelines[f"{entry.when}__{user.name}"] = entry.msg

        for wall_entry in reversed(sorted(timelines.items())):
            timestamp, user_name = wall_entry[0].split("__")
            human_timestamp = get_human_timestamp(float(timestamp))
            self.IO.write(f"{user_name} - {wall_entry[1]} ({human_timestamp})")


def main():
    console = Console()
    sn = SocialNetworking(console)
    command = ""
    console.write(HELP_MSG_TEXT)

    console.write(COMMANDS_TEXT)

    while command != "exit":
        command = input()
        if "->" in command:
            username, msg = command.split("->")
            username = username.strip()
            msg = msg.strip()
            sn.get_or_create_user(username).post(msg)
        elif command[:5].lower() == "visit":
            username = command[6:]
            sn.get_or_create_user(username).get_timeline()
        elif command[:6].lower() == "follow":
            follower_name, followee_name = command[7:].split(" ")
            followee_name.strip()
            follower_name.strip()
            follower = sn.get_or_create_user(follower_name)
            followee = sn.get_or_create_user(followee_name)
            follower.follow(followee)


if __name__ == "__main__":
    main()
