from PIL import Image
from image_utils import get_2d_editable_image, save_2d_edits

def create_and_set_pixels(filename):
    width, height = 3, 3
    img = Image.new('RGB', (width, height), color='white')

    # Get the pixel access object. This object acts like a 2D list.
    pixels = get_2d_editable_image(img)

    pixels[0][0] = (0, 0, 255)

    pixels[2][0] = (255, 0, 0)

    pixels[0][2] = (0, 255, 0)

    pixels[1][1] = (0, 0, 0)

    # First, draw out on your piece of paper what you think this
    # image will look like!

    # Then, uncomment the lines below and run the code.

    try:
        save_2d_edits(img, pixels)
        img.save(filename)
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    # Note: To run this script, you must have the Pillow library installed:
    # pip install Pillow
    create_and_set_pixels("mystery-image.ppm")

    # Change .png to .ppm then run this command:
    # xxd -s 11 mystery-image.ppm
    # To see the raw pixel data!
