"""
File: imageexample_2d.py
-------------------------
This program contains several examples of functions that
manipulate an image using the Simple2dImage library and 2D list syntax.
"""


# Assume 'Simple2dImage' is the name of your rewritten class file
from simple2dimage import Simple2dImage


def darker(image):
    """
    Makes image passed in darker by halving red, green, blue values.
    Note: changes are applied directly to the image object.
    """
    # Use len() for dimensions and image[y][x] for access/modification
    height = len(image)
    
    for y in range(height):
        # Using len(image[y]) is equivalent to image.width
        for x in range(len(image[y])):
            
            # Read pixel as an RGB tuple
            red, green, blue = image[y][x]
            
            # Calculate new values
            new_red = red // 2
            new_green = green // 2
            new_blue = blue // 2
            
            # Write new RGB tuple back
            image[y][x] = (new_red, new_green, new_blue)


def red_channel(filename):
    """
    Reads image from file. Sets green and blue values to 0 
    for every pixel, yielding the red channel.
    Returns the changed image.
    """
    image = Simple2dImage(filename)
    height = len(image)
    
    for y in range(height):
        for x in range(len(image[y])):
            
            # Read pixel as an RGB tuple
            red, green, blue = image[y][x]
            
            # Write new RGB tuple back with G and B set to 0
            image[y][x] = (red, 0, 0)
            
    return image


def right_half_darker(filename):
    """
    Reads image from file. Make *right half* of the image to be half as bright.
    (Demonstrates float multiplication and then integer clamping upon write)
    """
    image = Simple2dImage(filename)
    height = len(image)
    width = len(image[0])
    
    half_width = width // 2
    
    for y in range(height):
        # Iterate over the columns, starting from the halfway point
        for x in range(half_width, width):
            
            # Read pixel as an RGB tuple
            red, green, blue = image[y][x]
            
            # Calculate new values using float multiplication
            new_red = red * 0.5
            new_green = green * 0.5
            new_blue = blue * 0.5
            
            # The assignment image[y][x] = (new_red, ...) will automatically 
            # cast to int and clamp to 0-255 inside the Simple2dImageRow class.
            image[y][x] = (new_red, new_green, new_blue)
            
    return image


def compute_luminosity(red, green, blue):
    """
    Calculates the luminosity of a pixel using NTSC formula.
    """
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)


def grayscale(filename):
    """
    Reads image from file. Changes the image to be grayscale using 
    the NTSC luminosity formula and returns it.
    """
    image = Simple2dImage(filename)
    height = len(image)

    for y in range(height):
        for x in range(len(image[y])):
            
            # Read pixel as an RGB tuple
            red, green, blue = image[y][x]
            
            # Compute common luminosity value
            luminosity = compute_luminosity(red, green, blue)
            
            # Write the new RGB tuple back with all channels set to luminosity
            image[y][x] = (luminosity, luminosity, luminosity)
            
    return image


def main():
    """
    Run your desired image manipulation functions here.
    """
    # Assuming 'flower.png' exists
    flower = Simple2dImage('flower.png')
    flower.show()

    # Demonstrates in-place modification
    darker(flower)
    flower.show()

    # Demonstrates modification and return of a new image
    red_flower = red_channel('flower.png')
    red_flower.show()
    
    right_half_darker_flower = right_half_darker('flower.png')
    right_half_darker_flower.show()
    
    grayscale_flower = grayscale('flower.png')
    grayscale_flower.show()


if __name__ == '__main__':
    main()