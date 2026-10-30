import matplotlib.pyplot as plt
import load_csv as lc


def aff_pop(path: str):
    data = lc.load(path)
    if data is None:
        return

    selected = data.set_index("country")
    selected = selected.replace(
        {"k": "e3", "M": "e6", "B": "e9"},
        regex=True
        ).astype(float)
    years = selected.columns.astype(int)
    plt.plot(years, selected.loc["France"], label="France")
    plt.plot(years, selected.loc["Italy"], label="Italy")
    plt.yticks([20_000_000, 40_000_000, 60_000_000],
               ["20M", "40M", "60M"])
    plt.ylim(0, 80_000_000)
    plt.xlim(1800, 2050)
    plt.ylabel("Population")
    plt.xlabel("Year")
    plt.title("Population Projections")
    plt.legend(loc='lower right')
    plt.show()


def main():
    try:
        aff_pop("population_total.csv")
    except (TypeError, ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
