from hello_world import get_message
from hello_world.main import build_parser, main


def test_get_message_returns_default_greeting() -> None:
    assert get_message() == "Hello, world!"


def test_get_message_uses_custom_name() -> None:
    assert get_message("Codex") == "Hello, Codex!"


def test_build_parser_accepts_custom_name() -> None:
    args = build_parser().parse_args(["--name", "Python"])

    assert args.name == "Python"


def test_main_prints_default_greeting(capsys) -> None:
    main([])

    assert capsys.readouterr().out == "Hello, world!\n"


def test_main_prints_custom_name(capsys) -> None:
    main(["--name", "CLI"])

    assert capsys.readouterr().out == "Hello, CLI!\n"
