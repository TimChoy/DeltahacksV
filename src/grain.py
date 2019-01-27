# grain.py

from numpy import *
import pandas as pd
from PIL import Image
from copy import *

pixels_dict = {}
readRGB = []
solvedCat = []
def readGraynne(image_name):
    img = Image.open(image_name, 'r').convert('I')
    data = asarray(img)
    return data


def diffRight(readRGB):
    diff = empty(209715200)
    for index in range(len(readRGB)-1):
        diff[index] = readRGB[index] -  readRGB[index+1]
    diff[209715200-1] = 0
    return diff

def diffUp(readRGB):
    diff = empty(209715200)
    for index in range(1024):
        diff[index] = 0
    for index in range(1024,len(readRGB)):
        diff[index] = readRGB[index] -  readRGB[index-1024]
    return diff

def diffDown(readRGB):
    diff = empty(209715200)
    for index in range(len(readRGB),len(readRGB)-1024):
        diff[index] = readRGB[index] -  readRGB[index+1024]
    for index in range(len(readRGB)-1024,len(readRGB)):
        diff[index] = 0
    return diff


def diffLeft(readRGB):
    diff = empty(209715200)
    diff[0] = 0
    for index in range(1,len(readRGB)):
        diff[index] = readRGB[index] -  readRGB[index-1]
    return diff

for i in range(200):
    readRGB.append(reshape(readGraynne("../../../fake microstructure/Target 1/image_" + str(i) + ".png"),1048576))

for i in range(200):
    solvedCat.append(reshape(readGraynne("../../../fake microstructure/Target 1/p2mask_np_" + str(i) + ".png"),1048576))
    
readRGB = reshape(readRGB, int(209715200))
solvedCat = reshape(solvedCat,int(209715200))
    
pixelsFrame = pd.DataFrame(pixels_dict)
print(size(readRGB))
print(readRGB)

#print(len(solvedCat))
#print(size(solvedCat))
#print(solvedCat)

pixelsFrame['originalRGB'] = readRGB
pixelsFrame['solved Cat'] = solvedCat
pixelsFrame['difRight'] = diffRight(readRGB)
#pixelsFrame['difUpRight'] = diffRight(readRGB, solvedCat)

#pixelsFrame['difUp'] =
#pixelsFrame['difLeftUp'] =
#pixelsFrame['difLeft'] =
#pixelsFrame['difLeftDown'] =
#pixelsFrame['difDown'] =
#pixelsFrame['difRightDown']

#pixelsFrame['difUpRight'].head(5)
pixelsFrame['difRight']
