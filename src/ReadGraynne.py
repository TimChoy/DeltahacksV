## ReadGraynne Module
#  Reads image info for Graynne program
#  Entry for DeltaHacks V
#  Tim Choy, Sam Crawford, Lewis Rafuse, and Cameron Dufault

from numpy import *
from PIL import Image
from copy import *

## Function readGraynne
#  Parameter image_name: string of name of image file
#  Description: Takes a string of the name of image and returns a 2D array of
#  grayscale values of the image. Grayscale pixel value ranges from 0 to 255
def readGraynne(image_name):
    img = Image.open(image_name, 'r').convert('L')
    data = asarray(img)
    return data

def flatten(list2D):
    toFlatten = copy(list2D)
    flattened = []
    for i in range(len(toFlatten)):
        for j in range(len(toFlatten[i])):
            flattened.append(toFlatten[i][j])
    return flattened
