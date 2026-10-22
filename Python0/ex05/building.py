import sys
import string


def count_words(arg: str):
    """Function used to count every type of character in the string"""
    upper = 0
    lower = 0
    space = 0
    digit = 0
    punct = 0

    for c in arg:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        elif c in string.punctuation:
            punct += 1

    print(f"The text contains {len(arg)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    if len(sys.argv) == 2:
        arg = sys.argv[1]
    else:
        try:
            print("What is the text to count?")
            arg = sys.stdin.read()
        except (KeyboardInterrupt, EOFError):
            return

    count_words(arg)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
