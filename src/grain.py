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
    diff = empty(20971520)
    for index in range(len(readRGB)-1):
        diff[index] = readRGB[index] - readRGB[index+1]
    diff[20971520-1] = 0
    return diff

def diffUp(readRGB):
    diff = empty(20971520)
    for index in range(1024):
        diff[index] = 0
    for index in range(1024, len(readRGB)):
        diff[index] = readRGB[index] - readRGB[index-1024]
    return diff

def diffDown(readRGB):
    diff = empty(20971520)
    for index in range(len(readRGB),len(readRGB)-1024):
        diff[index] = readRGB[index] - readRGB[index+1024]
    for index in range(len(readRGB)-1024, len(readRGB)):
        diff[index] = 0
    return diff

def diffLeft(readRGB):
    diff = empty(20971520)
    diff[0] = 0
    for index in range(1, len(readRGB)):
        diff[index] = readRGB[index] - readRGB[index-1]
    return diff

for i in range(20):
    readRGB.append(reshape(readGraynne("../../../fake microstructure/Target 1/image_" + str(i) + ".png"),1048576))

for i in range(20):
    solvedCat.append(reshape(readGraynne("../../../fake microstructure/Target 1/p2mask_np_" + str(i) + ".png"),1048576))
    
readRGB = reshape(readRGB, int(20971520))
solvedCat = reshape(solvedCat,int(20971520))
    
pixelsFrame = pd.DataFrame(pixels_dict)
print(size(readRGB))
print(readRGB)

#print(len(solvedCat))
#print(size(solvedCat))
#print(solvedCat)

pixelsFrame['originalRGB'] = readRGB
pixelsFrame['solved Cat'] = solvedCat

pixelsFrame['difUp']    = diffUp(readRGB)
pixelsFrame['difLeft']  = diffLeft(readRGB)
pixelsFrame['difRight'] = diffRight(readRGB)
pixelsFrame['difDown']  = diffDown(readRGB)

#pixelsFrame['difLeftUp']   =
#pixelsFrame['difRightUp']  = diffRight(readRGB, solvedCat)
#pixelsFrame['difLeftDown'] =
#pixelsFrame['difRightDown']

#pixelsFrame['difUpRight'].head(5)
#pixelsFrame['difRight']

pixelsFrame.to_csv("output.csv")

data = pd.read_csv("output.csv")
