from simple2dimage import Simple2dImage

SQUEEZE_FACTOR = 3


def squeeze_width(filename, n):
    """
    Create a new image with the same height as the original, but
    with a width that is n times smaller than the original's. 
    Copy the original image such that it is squeezed horizontally.
    """
    image = Simple2dImage(filename)

    old_height = len(image)
    old_width = len(image[0])
    
    new_width = old_width // n
    new_height = old_height

    out = Simple2dImage.blank(new_width, new_height)

    # Copy every nth pixel from the original image to the output image


    out.show()


def main():
    squeeze_width('karel.png', SQUEEZE_FACTOR)


if __name__ == "__main__":
    main()
