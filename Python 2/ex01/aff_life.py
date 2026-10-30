import matplotlib.pyplot as plt
import load_csv as lc


def aff_life(path: str):
    """Display the life expectancy of France."""
    data = lc.load(path)
    if data is None:
        return
    selected = data.set_index("country").loc["France"]
    plt.plot(selected.index.astype(int), selected.values)
    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.title("France Life expectancy Projections")
    plt.show()


def main():
    """Run the program and handle errors."""
    try:
        aff_life("life_expectancy_years.csv")
    except (KeyError, ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
