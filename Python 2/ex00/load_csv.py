import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Open a .csv file and print his dimensions and return his content."""
    try:
        data = pd.read_csv(path)
    except (OSError, ValueError, TypeError, pd.errors.ParserError) as e:
        print(f"Error while opening the file: {e}")
        return None
    print(f"Loading dataset of dimensions {data.shape}")
    return data


def main():
    """Test the load function with a valid path then an invalid path."""
    print("Testing a valid path:\n")
    print(load("life_expectancy_years.csv"))
    print("\nTesting an invalid path:\n")
    print(load("notfound"))
    print("\nTesting an invalid type:\n")
    print(load(None))


if __name__ == "__main__":
    main()
