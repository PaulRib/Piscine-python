import matplotlib.pyplot as plt
import load_csv as lc


def projection(incomepath: str, lifepath: str):
    income = lc.load(incomepath)
    life = lc.load(lifepath)

    income = income.set_index("country")
    life = life.set_index("country")
    income = income["1900"]
    life = life["1900"]
    income = income.replace(
        {"k": "e3"}, regex=True).astype(float)
    income, life = income.align(life, join="inner")
    plt.title("1900")
    plt.scatter(income, life)
    plt.ylabel("Life Expectancy")
    plt.xlabel("Gross domestic product")
    plt.xticks([300, 1_000, 10_000],
               ["300", "1K", "10K"])
    plt.xscale("log")
    plt.show()


def main():
    try:
        projection("income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
                "life_expectancy_years.csv")
    except (TypeError, ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
