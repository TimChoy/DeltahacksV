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

def writeGraynne(data):
    data2D = np.reshape(data, (-1, sqrt(data.size)))
    img = Image.fromarray(data2D, "I")
    img.save("output.png")
    
def flatten(list2D):
    return [item for sublist in list2D for item in sublist]
