"""(C) 2013-2024 Copycat Software, LLC. All Rights Reserved."""

__version__ = "0.3.0"


def enum(**args):
    """Enum."""
    return type("Enum", (), args)
