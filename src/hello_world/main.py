"""CLI entry point for hello_world."""

from hello_world import get_message


def main() -> None:
    """Print the greeting to stdout."""
    print(get_message())


if __name__ == "__main__":
    main()
