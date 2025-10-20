
from PIL import Image
from typing import List, Tuple, Any

# Define a type alias for clarity: A 2D list of color tuples
Pixel2DList = List[List[Tuple[int, int, int]]]

def get_2d_editable_image(img: Image.Image) -> Pixel2DList:
    """
    Converts a Pillow Image object into a standard Python list of lists
    where indexing is in the format: pixels[row_y][col_x]

    Args:
        img: The Pillow Image object.

    Returns:
        A list of lists containing RGB tuples.
    """
    width, height = img.size
    # 1. Get the linear (flat) pixel data list
    flat_data = list(img.getdata())

    # 2. Convert the flat list into a standard 2D Python list (list of lists)
    # The list comprehension structures the data by rows (height) then columns (width)
    pixels_2d_list = [
        flat_data[i * width:(i + 1) * width]
        for i in range(height)
    ]

    return pixels_2d_list

def save_2d_edits(img: Image.Image, pixels_2d_list: Pixel2DList):
    """
    Takes the modified 2D list of pixel data, flattens it, and puts the
    data back into the Pillow Image object.

    Args:
        img: The Pillow Image object to modify in place.
        pixels_2d_list: The modified 2D list of RGB tuples.
    """
    # 1. Flatten the 2D list back into a single sequence of tuples for Pillow
    modified_flat_data = [pixel for row in pixels_2d_list for pixel in row]

    # 2. Put the modified data back into the image object
    img.putdata(modified_flat_data)
