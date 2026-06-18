"""hello_world package."""

__all__ = ["get_message"]


def get_message(name: str = "world") -> str:
    """Return a greeting message for the provided name."""
    return f"Hello, {name}!"
