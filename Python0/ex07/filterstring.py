import string
from sys import argv


def main():
    if len(argv) != 3:
        raise AssertionError("the arguments are bad")

    try:
        length = int(argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    words = argv[1].split()
    result = [
        w for w in filter(
            lambda w: len(w) > length and all(
                c not in string.punctuation and c.isprintable()
                for c in w
            ),
            words
        )
    ]
    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
