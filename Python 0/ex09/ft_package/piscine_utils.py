import time
import datetime as dt
import string
from typing import Any


def Hello():
    """Explain differences between list, tuple, set and dict and how to 
    manipulate it"""
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    ft_list[1] = "World!"
    y = list(ft_tuple)
    y[1] = "France!"
    ft_tuple = tuple(y)
    ft_set.remove("tutu!")
    ft_set.add("Mulhouse!")
    ft_dict["Hello"] = "42Mulhouse!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


def format_ft_time():
    """Print the number of seconds since 1970"""
    second = time.time()
    seconds = f"{second:,.6f}"
    science = f"{second:.2e}"
    print("Seconds since January 1, 1970:", seconds, "or", science,
          "in scientific notation")
    print(dt.datetime.today().strftime('%b %d %Y'))


def NULL_not_found(object: Any) -> int:
    """Print the type of the argument based on a samples of test, 
    return 1 if the type is not found, 0 otherwise"""
    if object is None:
        print("Nothing :", object, type(object))
    elif isinstance(object, float) and object != object:
        print("Cheese :", object, type(object))
    elif isinstance(object, bool) and object is False:
        print("Fake :", object, type(object))
    elif isinstance(object, int) and object == 0:
        print("Zero :", object, type(object))
    elif isinstance(object, str) and object == "":
        print("Empty :", object, type(object))
    else:
        print("Type not found")
        return 1

    return 0


def whatis(num: int):
    """Print if the number is odd or even"""
    if num % 2 == 0:
        print("I'm even")
    else:
        print("I'm odd")


def count_words(arg: str):
    """Print every type of character in the string and how many of
    them is in"""
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


def filterstring(words: str, length: int) -> list:
    """Filter a string by removing words with smaller length than the number
    passed on argument and return the new chain as a list"""
    words = words.split()
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
