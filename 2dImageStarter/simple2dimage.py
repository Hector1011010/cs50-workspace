"""
This is the Simple2dImage class, an altered version of the SimpleImage class
from Stanford CS106A that supports 2D list syntax for getting and setting pixel data.

YOU SHOULD NOT MODIFY THIS FILE.

Originally written by Nick Parlante, Sonja Johnson-Yu, and Nick Bowman.
Altered to support 2D list syntax by Baker Sharp

SimpleImage Features:
Create image:
  image = SimpleImage.blank(400, 200)   # create new image of size
  image = SimpleImage('foo.jpg')        # create from file

Show image on screen
  image.show()

The main() function below demonstrates the above functions as a test.
"""

import sys
from PIL import Image

def clamp(num):
    """
    Return a "clamped" version of the given num,
    converted to be an int limited to the range 0..255 for 1 byte.
    """
    num = int(num)
    if num < 0:
        return 0
    if num >= 256:
        return 255
    return num


# color tuples for background color names 'red' 'white' etc.
BACK_COLORS = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
}


class Simple2dImageRow(object):
    """
    A helper class to represent a single row (y-coordinate) of the Simple2dImage.
    This enables the my_image[y][x] syntax for getting and setting pixel data.
    """
    def __init__(self, image, y):
        self.image = image
        self._y = y

    # Enables len(image[y]) to return the row length (width)
    def __len__(self):
        """Returns the width of the image (the number of pixels in this row)."""
        return self.image.width

    def __getitem__(self, x):
        """Handles my_image[y][x] access (getting the pixel tuple)."""
        if x < 0 or x >= self.image.width:
            raise IndexError('x index out of range')
        # Pillow's px map is indexed as (x, y)
        return self.image.px[x, self._y]

    def __setitem__(self, x, value):
        """
        Handles my_image[y][x] = (r, g, b) assignment (setting the pixel tuple).
        The value must be a tuple of (red, green, blue).
        """
        if x < 0 or x >= self.image.width:
            raise IndexError('x index out of range')

        # Ensure values are clamped before writing to the image
        r, g, b = value
        clamped_value = (clamp(r), clamp(g), clamp(b))
        
        # Pillow's px map is indexed as (x, y)
        self.image.px[x, self._y] = clamped_value


class Simple2dImage(object):
    def __init__(self, filename, width=0, height=0, back_color=None):
        # ... (unchanged initialization logic) ...
        
        if filename:
            self.pil_image = Image.open(filename).convert("RGB")
            if self.pil_image.mode != 'RGB':
                raise Exception('Image file is not RGB')
            self._filename = filename
        else:
            if not back_color:
                back_color = 'white'
            color_tuple = BACK_COLORS[back_color]
            if width == 0 or height == 0:
                raise Exception('Creating blank image requires width/height but got {} {}'.format(width, height))
            self.pil_image = Image.new('RGB', (width, height), color_tuple)
            
        self.px = self.pil_image.load()
        size = self.pil_image.size
        self._width = size[0]
        self._height = size[1]
        self.curr_x = 0
        self.curr_y = 0

    # Enables len(image) to return the number of rows (height)
    def __len__(self):
        """Returns the height of the image (the number of rows)."""
        return self.height

    def __getitem__(self, y):
        """
        Handles my_image[y] access.
        Returns a Simple2dImageRow object, allowing the second [x] access.
        """
        if y < 0 or y >= self.height:
            raise IndexError('y index out of range')
        return Simple2dImageRow(self, y)

    def __iter__(self):
        self.curr_x = 0
        self.curr_y = 0
        return self

    def __next__(self):
        if self.curr_y < self.height:
            x = self.curr_x
            y = self.curr_y
            pixel_tuple = self.px[x, y]
            self._increment_curr_counters()
            return pixel_tuple
        else:
            raise StopIteration()

    def _increment_curr_counters(self):
        self.curr_x += 1
        if self.curr_x == self.width:
            self.curr_x = 0
            self.curr_y += 1
            
    # ... (rest of Simple2dImage methods like blank, file, width/height properties, etc., are unchanged) ...
    @classmethod
    def blank(cls, width, height, back_color=None):
        return Simple2dImage('', width, height, back_color=back_color)

    @classmethod
    def file(cls, filename):
        return Simple2dImage(filename)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def get_rgb(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
             raise Exception('get_rgb bad coordinate x %d y %d (vs. image width %d height %d)' %
                            (x, y, self._width, self.height))
        return self.px[x, y]
        
    def set_rgb(self, x, y, red, green, blue):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
             raise Exception('set_rgb bad coordinate x %d y %d (vs. image width %d height %d)' %
                            (x, y, self._width, self.height))
        self.px[x, y] = (clamp(red), clamp(green), clamp(blue))

    def show(self):
        self.pil_image.show()


if __name__ == '__main__':
    # Original main for testing Simple2dImage features
    args = sys.argv[1:]
    if len(args) == 1:
        image = Simple2dImage.file(args[0])
        image.show()
        sys.exit() # Use sys.exit() instead of return in main

    # Create yellow rectangle (400x200)
    image = Simple2dImage.blank(400, 200)
    
    # Demonstrate the use of len()
    print(f"Image height (len(image)): {len(image)}") 
    print(f"Image width (len(image[0])): {len(image[0])}") 

    # Set the top 10 rows to red
    for y in range(len(image) // 2): # Example using len() for height
        for x in range(len(image[y]) // 2): # Example using len() for width
            image[y][x] = (255, 0, 0) # Set to RED

    image.show()