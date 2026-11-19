import load_image as li
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(path: str) -> np.ndarray:
    """Take a path of an image to open it with ft_load, then slice
    it. Print its new format and its new pixels
    content. Return an array containing
    the information of the sliced picture.
    Any invalid path will proc an TypeError."""
    try:
        data = li.ft_load(path)
        h, w, _ = data.shape
        im = Image.fromarray(data).convert("L")
        grey_data = np.array(im)
        new_data = grey_data[200:h // 2 + 200, 200:w // 2 + 200, np.newaxis]
        print(f"New shape after slicing: {new_data.shape}")
        print(new_data)
        plt.imshow(new_data[:, :, 0], cmap="gray")
        plt.show()
        return new_data
    except (TypeError, OSError, ValueError) as e:
        print(f"Error: {e}")
        return None


def main():
    """Zoom the image to a 400 : 400 pixels square."""
    ft_zoom("animal.jpeg")


if __name__ == "__main__":
    main()
