import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Open a .csv file and print his dimensions and return his content."""
    try:
        data = pd.read_csv(path)
    except (OSError, ValueError, TypeError, pd.errors.ParserError) as e:
        print(f"Error while opening the file: {e}")
        return None
    return data
