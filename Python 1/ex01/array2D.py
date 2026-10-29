import numpy as np


def verify_array(family: list) -> bool:
    """Verify all error in the list passed on argument and return true
    if an error appear, otherwise return false."""
    if not family:
        return True
    if (np.ndim(family) != 2):
        return True
    if not all(isinstance(row, list) for row in family):
        return True
    if any(len(i) != len(family[0]) for i in family):
        return True
    if any(not i for i in family):
        return True
    return False


def slice_me(family: list, start: int, end: int) -> list:
    """Take a 2D list and two iterator passed as an int, print the shape of
    the list then slice the list based on the two iterators.
    Print the new shape of the sliced list and return it. """
    if not (isinstance(family, list) and isinstance(start, int)
            and isinstance(end, int)):
        raise TypeError("First argument must be a list and others must be \
                        integers!")
    if verify_array(family):
        raise TypeError("First argument must be a valid 2D list!")
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    trimmed = family[start:end]
    if any(not i for i in trimmed):
        raise ValueError("Slicing result can not be empty")
    print(f"My new shape is : ({len(trimmed)}, {len(trimmed[0])})")
    return trimmed


def main():
    """Slice a 2D list from two different test."""
    try:
        family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
