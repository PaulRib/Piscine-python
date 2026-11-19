import matplotlib.pyplot as plt
import load_csv as lc


def aff_pop(path: str):
    """Show the population of two selected countries."""
    data = lc.load(path)
    if data is None:
        return
    try:
        selected = data.set_index("country")
        selected = selected.replace(
            {"k": "e3", "M": "e6", "B": "e9"},
            regex=True
            ).astype(float)
        years = selected.columns.astype(int)
        plt.plot(years, selected.loc["France"], label="France")
        plt.plot(years, selected.loc["Italy"], label="Italy")
        plt.yticks([20_000_000, 40_000_000, 60_000_000], ["20M", "40M", "60M"])
        plt.ylim(0, 80_000_000)
        plt.xlim(1800, 2050)
        plt.ylabel("Population")
        plt.xlabel("Year")
        plt.title("Population Projections")
        plt.legend(loc='lower right')
        plt.show()
    except (TypeError, ValueError, KeyError) as e:
        print(f"Error: {e}")


def main():
    """Run the program and try different path."""
    print("Testing a valid path:\n")
    aff_pop("population_total.csv")
    print("\nTesting an invalid path:\n")
    aff_pop("load_csv.py")
    print("\nTesting a non-existent path:\n")
    aff_pop("null")
    print("\nTesting an invalid type:\n")
    aff_pop(None)


if __name__ == "__main__":
    main()
