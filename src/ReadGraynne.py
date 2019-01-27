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
    data = reshape(data, 1024*1024)
    return data

## Function writeGraynne
#  Parameter data: a numpy 1D array
#  Description: Takes in a 1D numpy array and turns it into a 2D array, and
#  outputs a .png file named output.png.
def writeGraynne(data):
    tmp = empty(1024*1024)
    for i in range(len(data)):
        if(data[i] == 1):
            tmp[i] = 65535
        else:
            tmp[i] = 0
    data2D = reshape(tmp, (-1, int(sqrt(data.size))))
    #print(data2D)
    img = Image.fromarray(data2D, "I")
    img.save("output.png")
