from typing import Any


def calcul_mean(num: list[float]) -> float:
    """Calcul the mean of a list of float and return it."""
    return sum(num) / len(num)


def calcul_median(num: list[float]) -> float:
    """Calcul the median of a list of float and return it."""
    if len(num) % 2 == 0:
        first = num[len(num) // 2 - 1]
        second = num[len(num) // 2]
        median = (first + second) / 2
    else:
        median = num[len(num) // 2]
    return median


def calcul_quartile(num: list[float]) -> list[float]:
    """Calcul the quartile of a list of float and return it."""
    n = len(num)
    q1 = (n + 3) // 4
    q3 = (3 * n + 3) // 4
    return [num[q1 - 1], num[q3 - 1]]


def calcul_variance(num: list[float]) -> float:
    """Calcul the variance of a list of float and return it."""
    mean = sum(num) / len(num)
    var = [(v - mean) ** 2 for v in num]
    return sum(var) / len(num)


def calcul_std(num: list[float]) -> float:
    """Calcul the standard deviation of a list of float and return it."""
    var = calcul_variance(num)
    return var ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Put the numbers in a list of float and read the values of the tuple
    to redirect in the good function. Handle errors."""
    try:
        numbers = [float(args[i]) for i in range(len(args))]
        numbers.sort()
    except (TypeError, ValueError):
        numbers = None
    operations = {
        "mean": calcul_mean,
        "median": calcul_median,
        "quartile": calcul_quartile,
        "var": calcul_variance,
        "std": calcul_std
    }
    for operation in kwargs.values():
        if operation in operations:
            if not numbers:
                print("ERROR")
            else:
                print(f"{operation} : {operations[operation](numbers)}")


def main():
    """Run the program"""
    ft_statistics(1, 42, 360, 11, 64, fi="mean", se="median", th="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, fi="heheh", se="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
