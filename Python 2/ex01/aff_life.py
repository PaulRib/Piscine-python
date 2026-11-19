import matplotlib.pyplot as plt
import load_csv as lc


def aff_life(path: str):
    """Display the life expectancy of France."""
    data = lc.load(path)
    if data is None:
        return
    try:
        selected = data.set_index("country").loc["France"]
        plt.plot(selected.index.astype(int), selected.values)
        plt.ylabel("Life expectancy")
        plt.xlabel("Year")
        plt.title("France Life expectancy Projections")
        plt.show()
    except (KeyError, ValueError, TypeError) as e:
        print(f"Error: {e}")


def main():
    """Run the program and try different path."""
    print("Testing a valid path:\n")
    aff_life("life_expectancy_years.csv")
    print("\nTesting an invalid path:\n")
    aff_life("load_csv.py")
    print("\nTesting a non-existent path:\n")
    aff_life("null")
    print("\nTesting an invalid type:\n")
    aff_life(None)


if __name__ == "__main__":
    main()
