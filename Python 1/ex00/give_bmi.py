
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Take two list of int or float and return a list of int or float
    representing the imc. If len of lists are different or if one value is
    negative, raise a ValueError. If one item is not an int or a float,
    raise a TypeError."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Height and weight must be lists!")

    if len(height) != len(weight):
        raise ValueError("Both lists have to be the same size!")

    if not all(isinstance(value, (int, float)) for value in height):
        raise TypeError("Height must contain only int or float!")

    if not all(isinstance(value, (int, float)) for value in weight):
        raise TypeError("Weight must contain only int or float!")

    if not all(value > 0 for value in height):
        raise ValueError("Height values must be positive!")

    if not all(value > 0 for value in weight):
        raise ValueError("Weight values must be positive!")

    combined = zip(height, weight)
    bmi = list(w / (h * h) for h, w in combined)
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Take a list of int or float and an int. Compare each item of the
    list to the int and return a list of bool depending if each item are
    below or beyond the limit. If one item is not an int or a float,
    raise a TypeError."""
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list!")

    if not all(isinstance(value, (int, float)) for value in bmi):
        raise TypeError("BMI must contain only int or float!")

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer!")

    result = list(value > limit for value in bmi)
    return result


def main():
    """Calcul the bmi with two differents values then test a limit
    fix to 26."""
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
