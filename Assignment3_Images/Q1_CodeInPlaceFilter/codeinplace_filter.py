"""
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/mt-rainier.jpg'

def main():
    # Get file name from user input
    filename = get_file()
    
    # Load image and show image before the transform
    image = SimpleImage(filename)
    CID_filter(image)
    image.show()

    # Apply the filter

    return image

    # TODO: your code here

    # Show the image after the transform
    image.show()

def CID_filter(image):
    for px in image:
        px.red = px.red * 1.5
        px.green = px.green * 0.7
        px.blue = px.blue * 1.5

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

if __name__ == '__main__':
    main()
