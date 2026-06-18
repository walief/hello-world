"""CLI entry point for hello_world."""

from argparse import ArgumentParser, Namespace
from collections.abc import Sequence

from hello_world import get_message


def build_parser() -> ArgumentParser:
    """Build the command-line argument parser."""
    parser = ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument(
        "--name",
        default="world",
        help="Name to include in the greeting. Defaults to 'world'.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> None:
    """Print the greeting to stdout."""
    args: Namespace = build_parser().parse_args(argv)
    print(get_message(args.name))


if __name__ == "__main__":
    main()
