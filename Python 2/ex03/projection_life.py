import matplotlib.pyplot as plt
import load_csv as lc


def projection(incomepath: str, lifepath: str):
    """Show the relation between life expetancy and income per person."""
    income = lc.load(incomepath)
    life = lc.load(lifepath)

    if income is None or life is None:
        return
    try:
        income = income.set_index("country")
        life = life.set_index("country")
        income = income["1900"]
        life = life["1900"]
        income = income.replace(
            {"k": "e3"}, regex=True)
        income, life = income.align(life, join="inner")
        plt.title("1900")
        plt.scatter(income, life)
        plt.ylabel("Life Expectancy")
        plt.xlabel("Gross domestic product")
        plt.xticks([300, 1_000, 10_000], ["300", "1K", "10K"])
        plt.xscale("log")
        plt.show()
    except (TypeError, ValueError, KeyError) as e:
        print(f"Error: {e}")


def main():
    """Run the program and handle errors."""
    projection("income_per_person_gdppercapita_inflation_adjusted.csv",
               "life_expectancy_years.csv")
    print("\nTesting an invalid path:\n")
    projection("life_expectancy_years.csv", "load_csv.py")
    print("\nTesting a non-existent path:\n")
    projection("null", "null")
    print("\nTesting an invalid type:\n")
    projection("life_expectancy_years.csv", None)


if __name__ == "__main__":
    main()
