from typing import List
from .SocialNetworking import SocialNetworking, User, NO_POSTS, USER_NOT_EXIST
import time


class TestSocialNetworking:
    sn = SocialNetworking()

    def assert_print_equals(self, capsys, want):
        out, _ = capsys.readouterr()
        assert out == f"{want}\n"

    def assert_in_print(self, capsys, wants):
        out, _ = capsys.readouterr()
        for want in wants:
            assert want in out

    def test_should_user_post_to_own_timeline(self, capsys):
        user = self.sn.get_or_create_user("Alice")
        user.post("I love the weather today")
        self.assert_print_equals(capsys, "Alice -> I love the weather today")

    def test_should_user_read_timeline_single_post(self, capsys):
        user_to_check = self.sn.get_or_create_user("Alice")
        user_to_check.get_timeline()
        self.assert_in_print(capsys, ["I love the weather today"])

    def test_should_user_read_timeline_multiple_posts(self, capsys):
        user = self.sn.get_or_create_user("Bob")
        user.post("Damn! We lost!")
        user.post("Good game though.")
        user.get_timeline()
        self.assert_in_print(capsys, ["Damn! We lost!", "Good game though."])

    def test_should_user_with_no_posts_show_NO_POSTS(self, capsys):
        user = self.sn.get_or_create_user("John")
        user.get_timeline()
        self.assert_print_equals(capsys, NO_POSTS.format(user.name))

    def test_should_time_reported_be_right(self, capsys, monkeypatch):
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
            def __init__(self, name: str, timeline: List[Entry]) -> None:
                super().__init__(name)
                self.timeline = timeline

        user = StubUser(test_user, timeline_stub)
        user.get_timeline()
        self.assert_in_print(
            capsys,
            [
                "1 second ago",
                "2 seconds ago",
                "1 minute ago",
                "3 minutes ago",
                "5 minutes ago",
            ],
        )