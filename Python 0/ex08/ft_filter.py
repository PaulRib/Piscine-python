def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable for which function
    (item) is true. If function is None, return the items that are true.
    """
    if function is None:
        for i in iterable:
            if i:
                yield i
    else:
        for i in iterable:
            if function(i):
                yield i


def main():
    """Test ft_filter with different functions and iterables."""
    try:
        numbers = [0, 1, 2, 3, 4, 5, 6]

        print("Test 1: Keep even numbers")
        print(list(ft_filter(lambda x: x % 2 == 0, numbers)))
        # [0, 2, 4, 6]

        print("\nTest 2: Keep numbers greater than 3")
        print(list(ft_filter(lambda x: x > 3, numbers)))
        # [4, 5, 6]

        print("\nTest 3: Function is None")
        print(list(ft_filter(None, numbers)))
        # [1, 2, 3, 4, 5, 6]

        print("\nTest 4: Filter strings")
        words = ["hello", "", "Python", "", "42"]
        print(list(ft_filter(None, words)))
        # ['hello', 'Python', '42']

        print("\nTest 5: Empty iterable")
        print(list(ft_filter(lambda x: x > 0, [])))
        # []

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
