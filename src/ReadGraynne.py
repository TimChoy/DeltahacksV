## ReadGraynne Module
#  Reads image info for Graynne program
#  Entry for DeltaHacks V
#  Tim Choy, Sam Crawford, Lewis Rafuse, and Cameron Dufault

from PIL import Image

## Function readGraynne
#  Parameter image_name: string of name of image file
#  Description: Takes a string of the name of image and returns a 2D array of 
#  grayscale values of the image.
def readGraynne(image_name):
    img = Image.open("the/path/to/image")