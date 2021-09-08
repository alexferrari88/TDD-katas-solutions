from typing import List
from .SocialNetworking import SocialNetworking, User, NO_POSTS, USER_NOT_EXIST
import time
from .IOOutput import IOOutput
import pytest


class MockOutput(IOOutput):
    def __init__(self) -> None:
        self.value = ""

    def write(self, content: str) -> None:
        self.value += content + "\n"

    def read(self) -> str:
        return self.value


@pytest.fixture
def setup(autouse=True):
    IO = MockOutput()
    sn = SocialNetworking(IO)
    return IO, sn


class TestSocialNetworking:
    def assert_output_equals(self, IO, want):
        got = IO.read()
        assert got == f"{want}\n"

    def assert_in_output(self, IO, wants):
        got = IO.read()
        for want in wants:
            assert want in got

    def test_should_user_post_to_own_timeline(self, setup):
        IO, sn = setup
        user = sn.get_or_create_user("Alice")
        user.post("I love the weather today")
        self.assert_output_equals(IO, "Alice -> I love the weather today")

    def test_should_user_read_timeline_single_post(self, setup):
        IO, sn = setup
        user = sn.get_or_create_user("Alice")
        user.post("I love the weather today")
        user.get_timeline()
        assert "I love the weather today" in IO.read()

    def test_should_user_read_timeline_multiple_posts(self, setup):
        IO, sn = setup
        user = sn.get_or_create_user("Bob")
        user.post("Damn! We lost!")
        # needed because user can't submit at
        # the exact same time two different messages
        time.sleep(0.05)
        user.post("Good game though.")
        user.get_timeline()
        self.assert_in_output(IO, ["Damn! We lost!", "Good game though."])

    def test_should_user_with_no_posts_show_NO_POSTS(self, setup):
        IO, sn = setup
        user = sn.get_or_create_user("John")
        user.get_timeline()
        self.assert_output_equals(IO, NO_POSTS.format(user.name))

    def test_should_time_reported_be_right(self, setup):
        IO, _ = setup
        # it would have been better to break this in more tests
        FIVE_MINUTES = 5 * 60
        ONE_MINUTE = 60
        TWO_SECONDS = 2
        ONE_SECOND = 1
        SHOULD_BE_THREE_MINUTES = 200
        test_user = "John"
        from .SocialNetworking import Entry

        timeline_stub = [
            Entry("Test msg 1", time.time() - ONE_SECOND),
            Entry("Test msg 2", time.time() - TWO_SECONDS),
            Entry("Test msg 3", time.time() - ONE_MINUTE),
            Entry("Test msg 4", time.time() - SHOULD_BE_THREE_MINUTES),
            Entry("Test msg 5", time.time() - FIVE_MINUTES),
        ]

        class StubUser(User):
            def __init__(self, name: str, timeline: List[Entry], IO: IOOutput) -> None:
                super().__init__(name)
                self.timeline = timeline
                self.IO = IO

        user = StubUser(test_user, timeline_stub, IO)
        user.get_timeline()
        self.assert_in_output(
            IO,
            [
                "1 second ago",
                "2 seconds ago",
                "1 minute ago",
                "3 minutes ago",
                "5 minutes ago",
            ],
        )

    def test_should_user_subscribe_to_1_other_user_timelines(self, setup):
        IO, sn = setup
        sn.get_or_create_user("Alice").post("I love the weather today")
        user = sn.get_or_create_user("Charlie")
        user.post("I'm in New York today! Anyone wants to have a coffee?")
        user.follow(sn.get_or_create_user("Alice"))
        user.display_wall()
        self.assert_in_output(
            IO,
            [
                "Charlie - I'm in New York today! Anyone wants to have a coffee?",
                "Alice - I love the weather today",
            ],
        )

    def test_should_user_subscribe_to_multiple_users_timelines(self, setup):
        IO, sn = setup
        sn.get_or_create_user("Alice").post("I love the weather today")
        sn.get_or_create_user("Bob").post("Damn! We lost!")
        time.sleep(0.0005)
        sn.get_or_create_user("Bob").post("Good game though.")
        user = sn.get_or_create_user("Charlie")
        user.post("I'm in New York today! Anyone wants to have a coffee?")
        user.follow(sn.get_or_create_user("Alice"))
        user.follow(sn.get_or_create_user("Bob"))
        user.display_wall()
        self.assert_in_output(
            IO,
            [
                "Charlie - I'm in New York today! Anyone wants to have a coffee?",
                "Alice - I love the weather today",
                "Bob - Good game though.",
                "Bob - Damn! We lost!",
            ],
        )
