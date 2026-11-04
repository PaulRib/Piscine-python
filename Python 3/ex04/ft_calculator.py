class calculator:
    """Calculator class contain three static methods which manipulate values
    of two vector of float."""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calcul the dot product of two vector of float and print it."""
        new = 0
        for i in range(len(V1)):
            new += V1[i] * V2[i]
        print(f"Dot product is: {new}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add the values of two vector of float and print it."""
        new = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Add Vector is : {new}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substract the values of two vector of float and print it."""
        new = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Sous vec is: {new}")


def main():
    """Run the program."""
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
