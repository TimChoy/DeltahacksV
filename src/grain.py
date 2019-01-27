# grain.py

from numpy import *
import pandas as pd
from PIL import Image
from copy import *
from diffs import *

pixels_dict = {}
readRGB     = []
solvedCat   = []
def readGraynne(image_name):
    img = Image.open(image_name, 'r').convert('I')
    data = asarray(img)
    return data

for i in range(200):
    readRGB.append(reshape(readGraynne("../../../fake microstructure/Target 1/image_" + str(i) + ".png"),1048576))

for i in range(200):
    solvedCat.append(reshape(readGraynne("../../../fake microstructure/Target 1/p2mask_np_" + str(i) + ".png"),1048576))
    
readRGB = reshape(readRGB, int(209715200))
solvedCat = reshape(solvedCat,int(209715200))
    
pixelsFrame = pd.DataFrame(pixels_dict)

pixelsFrame['originalRGB'] = readRGB
pixelsFrame['solved Cat']  = solvedCat

pixelsFrame['diffFiveUp']    = fiveUp(readRGB)
pixelsFrame['diffFiveLeft']  = fiveLeft(readRGB)
pixelsFrame['diffFiveRight'] = fiveRight(readRGB)
pixelsFrame['diffFiveDown']  = fiveDown(readRGB)
pixelsFrame['diffTenUp']     = tenUp(readRGB)
pixelsFrame['diffTenLeft']   = tenLeft(readRGB)
pixelsFrame['diffTenRight']  = tenRight(readRGB)
pixelsFrame['diffTenDown']   = tenDown(readRGB)

pixelsFrame.to_csv("output.csv")
