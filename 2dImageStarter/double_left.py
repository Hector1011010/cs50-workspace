from simple2dimage import Simple2dImage

def double_left(filename):
    """
    Takes the left half of image, and copies it on top of the right half.
    """
    image = Simple2dImage(filename)

    height = len(image)
    width = len(image[0])
    half_width = width // 2

    # Loop over the left half and copy pixels to the right half
    

    image.show()


def main():
    double_left('karel.png')


if __name__ == "__main__":
    main()
