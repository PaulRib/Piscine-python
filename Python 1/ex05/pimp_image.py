import load_image as li
import numpy as np
import matplotlib.pyplot as plt


def ft_check_array(array):
    """Check the validity of the image passed to
    the others functions"""
    if not isinstance(array, np.ndarray):
        raise TypeError("Argument must be a NumPy array!")

    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("Array must be a 3D RGB image!")

    if array.size == 0:
        raise ValueError("Array cannot be empty!")

    if array.dtype != np.uint8:
        raise TypeError("Array must contain uint8 pixels!")


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    ft_check_array(array)
    new_array = array.copy()
    for row in new_array:
        for pixel in row:
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
    plt.imshow(new_array)
    plt.show()
    return new_array


def ft_red(array) -> np.ndarray:
    """Convert the color of the image in red by putting other
    colors' value at 0."""
    ft_check_array(array)
    new_array = array.copy()
    for row in new_array:
        for pixel in row:
            pixel[1] = 0
            pixel[2] = 0
    plt.imshow(new_array)
    plt.show()
    return new_array


def ft_green(array) -> np.ndarray:
    """Convert the color of the image in green by putting other
    colors' value at 0."""
    ft_check_array(array)
    new_array = array.copy()
    for row in new_array:
        for pixel in row:
            pixel[0] = 0
            pixel[2] = 0
    plt.imshow(new_array)
    plt.show()
    return new_array


def ft_blue(array) -> np.ndarray:
    """Convert the color of the image in blue by putting other
    colors' value at 0."""
    ft_check_array(array)
    new_array = array.copy()
    for row in new_array:
        for pixel in row:
            pixel[0] = 0
            pixel[1] = 0
    plt.imshow(new_array)
    plt.show()
    return new_array


def ft_grey(array) -> np.ndarray:
    """Convert the color of the image in grey by getting the value of
    the green and putting it in the red and blue value."""
    ft_check_array(array)
    new_array = array.copy()
    for row in new_array:
        for pixel in row:
            pixel[0] = pixel[1]
            pixel[2] = pixel[1]
    plt.imshow(new_array)
    plt.show()
    return new_array


def main():
    """Change the image by putting it in inverted colors, red, green,
    blue then grey."""
    try:
        array = li.ft_load("landscape.jpg")
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)
    except (TypeError, OSError, ValueError, IndexError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
