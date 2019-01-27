## ReadGraynne Module
#  Reads image info for Graynne program
#  Entry for DeltaHacks V
#  Tim Choy, Sam Crawford, Lewis Rafuse, and Cameron Dufault

from copy import *
from math import sqrt

from numpy import *
from PIL import Image


## Function readGraynne
#  Parameter image_name: string of name of image file
#  Description: Takes a string of the name of image and returns a 2D array of
#  grayscale values of the image. Grayscale pixel value ranges from 0 to 255
def readGraynne(image_name):
    img = Image.open(image_name, 'r').convert('I')
    data = asarray(img)
    return data

## Function writeGraynne
#  Parameter data: a numpy 1D array
#  Description: Takes in a 1D numpy array and turns it into a 2D array, and
#  outputs a .png file named output.png.
def writeGraynne(data):
    data2D = np.reshape(data, (-1, sqrt(data.size)))
    for i in range(len(data2D)):
        if(data2D[i] == 1):
            data2D[i] = 65536
        else:
            data2D[i] = 0
    img = Image.fromarray(data2D, "I")
    img.save("output.png")

def flatten(list2D):
    return [item for sublist in list2D for item in sublist]
