class calculator:
    """Calculator class contain a vector of int and four method,
    one of each for a scalar."""
    def __init__(self, arg):
        """Init the vector by putting the values passed as argument in it."""
        self.values = arg

    def __add__(self, object) -> None:
        """Operator '+' overload ."""
        self.values = [v + object for v in self.values]
        print(self.values)

    def __mul__(self, object) -> None:
        """Operator '*' overload ."""
        self.values = [v * object for v in self.values]
        print(self.values)

    def __sub__(self, object) -> None:
        """Operator '-' overload ."""
        self.values = [v - object for v in self.values]
        print(self.values)

    def __truediv__(self, object) -> None:
        """Operator '/' overload . Raise ValueError if division by 0."""
        try:
            self.values = [v / object for v in self.values]
            print(self.values)
        except ZeroDivisionError as e:
            print(f"Error: {e}")


def main():
    """Run the program."""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    v3 / 0


if __name__ == "__main__":
    main()
