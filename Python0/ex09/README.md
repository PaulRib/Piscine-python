# ft_package

A small Python package collecting utility functions developed during the 42 Python Piscine.

**Version:** 0.0.1  
**Author:** pribolzi  
**License:** MIT

## Installation

From the directory containing `setup.py`, run:

```bash
python3 -m pip install .
```

For an editable installation during development:

```bash
python3 -m pip install -e .
```

## Project structure

```text
ft_package/
├── ft_package/
│   ├── __init__.py
│   └── piscine_utils.py
├── setup.py
├── README.md
└── LICENSE
```

The structure above assumes that `setup.py` uses `setuptools.find_packages()` and that `__init__.py` re-exports the functions listed below.

## Available functions

| Function | Description |
| --- | --- |
| `Hello()` | Demonstrates creating and modifying lists, tuples, sets, and dictionaries; prints the results. |
| `format_ft_time()` | Prints the current Unix timestamp in decimal and scientific notation, followed by the current date. |
| `NULL_not_found(object)` | Prints a description of certain special values (`None`, NaN, `False`, `0`, and `""`); returns `1` for other values. |
| `whatis(num)` | Prints whether an integer is even or odd. |
| `count_words(arg)` | Prints counts of uppercase letters, lowercase letters, punctuation, whitespace, and digits in a string. |
| `filterstring(words, length)` | Applies a length and character filter to the elements iterated from `words`, then prints the result.|
| `ft_filter(function, iterable)` | Generator implementing behavior similar to Python's built-in `filter()`. |

## Usage

```python
from ft_package import Hello, whatis, count_words, ft_filter

Hello()
whatis(42)                   # I'm even
count_words("Hello, 42!")

numbers = [1, 2, 3, 4, 5]
evens = list(ft_filter(lambda n: n % 2 == 0, numbers))
print(evens)                 # [2, 4]
```

You can also import a function directly from its module:

```python
from ft_package.piscine_utils import format_ft_time

format_ft_time()
```

## Dependencies

The package uses only Python standard-library modules (`time`, `datetime`, `string`, and `typing`). No third-party runtime dependencies are required.

## Source

[GitHub repository](https://github.com/PaulRib/ft_package)

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
