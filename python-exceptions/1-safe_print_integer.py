#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer using '{:d}'.format().

    Args:
        value: Any type of value.

    Returns:
        True if value is an integer and printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
