from simple2dimage import Simple2dImage

PIXELS_TO_CROP = 30


def crop_image(filename, n):
    """
    Crops the image by removing an 'n' pixel border from all four sides.
    """
    # 1. Load the input image
    image = Simple2dImage(filename)

    # 2. Create the output image with the new, smaller dimensions
    out = Simple2dImage.blank(image.width - 2 * n, image.height - 2 * n)

    # 3. Fill in the cropped output image    
    


    # Show the cropped image
    out.show()


def main():
    crop_image('karel.png', PIXELS_TO_CROP)


if __name__ == "__main__":
    main()
