from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Take a path of an image to load it, then print its format and
    its pixels content in RGB format.
    Any invalid path will proc an TypeError"""
    if not isinstance(path, str) or not path:
        raise TypeError("Argument must be a valid path!")
    with Image.open(path) as im:
        data = np.array(im.convert("RGB"))
        print(f"The shape of image is: {data.shape}")
        print(data)
        return data


def main():
    """Load the image."""
    ft_load("landscape.jpg")


if __name__ == "__main__":
    try:
        main()
    except (TypeError, OSError, ValueError) as e:
        print(f"Error: {e}")
