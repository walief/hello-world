from hello_world import get_message


def test_get_message_returns_expected_greeting() -> None:
    assert get_message() == "Hello, world!"
