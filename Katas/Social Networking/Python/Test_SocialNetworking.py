from .SocialNetworking import SocialNetworking, NO_POSTS, USER_NOT_EXIST
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

    def test_should_post_to_timeline(self, capsys):
        self.sn.post("Alice", "I love the weather today")
        self.assert_print_equals(capsys, "Alice -> I love the weather today")

    def test_should_user_read_timeline_single_post(self, capsys):
        self.sn.read("Alice")
        self.assert_in_print(capsys, ["I love the weather today"])

    def test_should_return_USER_NOT_EXIST_when_read_for_unknown_user(self, capsys):
        sn = SocialNetworking()
        test_user = "John"
        sn.read(test_user)
        self.assert_print_equals(capsys, USER_NOT_EXIST.format(test_user))

    def test_should_user_read_timeline_multiple_posts(self, capsys):
        self.sn.post("Bob", "Damn! We lost!")
        self.sn.post("Bob", "Good game though.")
        self.assert_in_print(capsys, ["Damn! We lost!", "Good game though."])

    def test_should_time_reported_be_right(self, capsys, monkeypatch):
        FIVE_MINUTES = 5 * 60
        ONE_MINUTE = 60
        TWO_SECONDS = 2
        ONE_SECOND = 1
        SHOULD_BE_THREE_MINUTES = 200
        test_user = "John"
        from .SocialNetworking import Entry

        timeline_stub = {
            test_user: [
                Entry("Test msg 1", time.time() - ONE_SECOND),
                Entry("Test msg 2", time.time() - TWO_SECONDS),
                Entry("Test msg 3", time.time() - ONE_MINUTE),
                Entry("Test msg 4", time.time() - SHOULD_BE_THREE_MINUTES),
                Entry("Test msg 5", time.time() - FIVE_MINUTES),
            ]
        }

        sn = SocialNetworking()
        monkeypatch.setattr(sn, "timeline", timeline_stub)
        sn.read(test_user)
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
