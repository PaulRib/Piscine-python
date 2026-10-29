import load_image as li
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ft_transpose(data: np.ndarray) -> np.ndarray:
    """Transpose the width and height of the image received."""
    if not isinstance(data, np.ndarray):
        raise TypeError("Argument must be a NumPy array!")
    if data.size == 0:
        raise ValueError("Array cannot be empty!")
    if data.ndim != 2:
        raise ValueError("Array must have exactly 2 dimensions!")
    return np.array([[data[row][col] for row in range(len(data))]
                     for col in range(len(data[0]))])


def ft_rotate(path: str) -> np.ndarray:
    """Rotate the image received by transposing it."""
    data = li.ft_load(path)
    im = Image.fromarray(data).convert("L")
    grey_data = np.array(im)
    zoomed_data = grey_data[80:480, 420:820, np.newaxis]
    print(f"The shape of image is: {zoomed_data.shape}")
    print(zoomed_data)
    transposed_data = ft_transpose(zoomed_data[:, :, 0])
    print(f"New shape after Transpose: {transposed_data.shape}")
    print(transposed_data)
    plt.imshow(transposed_data, cmap="gray")
    plt.show()
    return transposed_data


def main():
    """Rotate the image by transposing it."""
    try:
        ft_rotate("animal.jpeg")
    except (TypeError, OSError, ValueError, IndexError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
