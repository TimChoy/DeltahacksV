# DataFrame.py
# Work for handling DataFrames

from pandas import DataFrame

from diffs import *

def genDataFrame(readRGB, solvedCat):
    pixels_dict = {}
    pixelsFrame = DataFrame(pixels_dict)

    pixelsFrame['originalRGB'] = readRGB
    pixelsFrame['solved Cat']  = solvedCat

    # Convention for order: up, left, right, down

    pixelsFrame['diffFiveUp']    = fiveUp(readRGB)
    pixelsFrame['diffTenUp']     = tenUp(readRGB)
    pixelsFrame['diffFiveLeft']  = fiveLeft(readRGB)
    pixelsFrame['diffTenLeft']   = tenLeft(readRGB)
    pixelsFrame['diffFiveRight'] = fiveRight(readRGB)
    pixelsFrame['diffTenRight']  = tenRight(readRGB)
    pixelsFrame['diffFiveDown']  = fiveDown(readRGB)
    pixelsFrame['diffTenDown']   = tenDown(readRGB)

    pixelsFrame['diffFiveUpLeft']  = fiveUpLeft(readRGB)
    pixelsFrame['diffTenUpLeft']   = tenUpLeft(readRGB)
    pixelsFrame['diffFiveUpRight'] = fiveUpRight(readRGB)
    pixelsFrame['diffTenUpRight']  = tenUpRight(readRGB)

    pixelsFrame['diffFiveUp'].fillna(pixelsFrame['diffFiveUp'].mean(), inplace = True)
    pixelsFrame['diffTenUp'].fillna(pixelsFrame['diffTenUp'].mean(), inplace = True)
    pixelsFrame['diffFiveLeft'].fillna(pixelsFrame['diffFiveLeft'].mean(), inplace = True)
    pixelsFrame['diffTenLeft'].fillna(pixelsFrame['diffTenLeft'].mean(), inplace = True)
    pixelsFrame['diffFiveRight'].fillna(pixelsFrame['diffFiveRight'].mean(),inplace = True)
    pixelsFrame['diffTenRight'].fillna(pixelsFrame['diffTenRight'].mean(), inplace = True)
    pixelsFrame['diffFiveDown'].fillna(pixelsFrame['diffFiveDown'].mean(), inplace= True)
    pixelsFrame['diffTenDown'].fillna(pixelsFrame['diffTenDown'].mean(), inplace = True)

    pixelsFrame['diffFiveUpLeft'].fillna(pixelsFrame['diffFiveUpLeft'].mean(), inplace= True)
    pixelsFrame['diffTenUpLeft'].fillna(pixelsFrame['diffTenUpLeft'].mean(), inplace= True)
    pixelsFrame['diffFiveUpRight'].fillna(pixelsFrame['diffFiveUpRight'].mean(), inplace= True)
    pixelsFrame['diffTenUpRight'].fillna(pixelsFrame['diffTenUpRight'].mean(), inplace= True)

    pixelsFrame["solved Cat"] = pixelsFrame["solved Cat"].apply(category)

    pixelsFrame["diffFiveUp"]    = pixelsFrame["diffFiveUp"].apply(categoryYo)
    pixelsFrame["diffTenUp"]     = pixelsFrame["diffTenUp"].apply(categoryYo)
    pixelsFrame["diffFiveLeft"]  = pixelsFrame["diffFiveLeft"].apply(categoryYo)
    pixelsFrame["diffTenLeft"]   = pixelsFrame["diffTenLeft"].apply(categoryYo)
    pixelsFrame["diffFiveRight"] = pixelsFrame["diffFiveRight"].apply(categoryYo)
    pixelsFrame["diffTenRight"]  = pixelsFrame["diffTenRight"].apply(categoryYo)
    pixelsFrame["diffFiveDown"]  = pixelsFrame["diffFiveDown"].apply(categoryYo)
    pixelsFrame["diffTenDown"]   = pixelsFrame["diffTenDown"].apply(categoryYo)

    pixelsFrame['diffFiveUpLeft']  = pixelsFrame['diffFiveUpLeft'].apply(categoryYo)
    pixelsFrame['diffTenUpLeft']   = pixelsFrame['diffTenUpLeft'].apply(categoryYo)
    pixelsFrame['diffFiveUpRight'] = pixelsFrame['diffFiveUpRight'].apply(categoryYo)
    pixelsFrame['diffTenUpRight']  = pixelsFrame['diffTenUpRight'].apply(categoryYo)

    return pixelsFrame

def genImageDataFrame(readRGB):
    pixels_dict = {}
    pixelsFrame = DataFrame(pixels_dict)

    pixelsFrame['originalRGB'] = readRGB
    pixelsFrame['diffFiveUp']    = fiveUp(readRGB)
    pixelsFrame['diffTenUp']     = tenUp(readRGB)
    pixelsFrame['diffFiveLeft']  = fiveLeft(readRGB)
    pixelsFrame['diffTenLeft']   = tenLeft(readRGB)
    pixelsFrame['diffFiveRight'] = fiveRight(readRGB)
    pixelsFrame['diffTenRight']  = tenRight(readRGB)
    pixelsFrame['diffFiveDown']  = fiveDown(readRGB)
    pixelsFrame['diffTenDown']   = tenDown(readRGB)
    pixelsFrame['diffFiveUpLeft']  = fiveUpLeft(readRGB)
    pixelsFrame['diffTenUpLeft']   = tenUpLeft(readRGB)
    pixelsFrame['diffFiveUpRight'] = fiveUpRight(readRGB)
    pixelsFrame['diffTenUpRight']  = tenUpRight(readRGB)

    pixelsFrame['diffFiveUp'].fillna(pixelsFrame['diffFiveUp'].mean(), inplace = True)
    pixelsFrame['diffTenUp'].fillna(pixelsFrame['diffTenUp'].mean(), inplace = True)
    pixelsFrame['diffFiveLeft'].fillna(pixelsFrame['diffFiveLeft'].mean(), inplace = True)
    pixelsFrame['diffTenLeft'].fillna(pixelsFrame['diffTenLeft'].mean(), inplace = True)
    pixelsFrame['diffFiveRight'].fillna(pixelsFrame['diffFiveRight'].mean(),inplace = True)
    pixelsFrame['diffTenRight'].fillna(pixelsFrame['diffTenRight'].mean(), inplace = True)
    pixelsFrame['diffFiveDown'].fillna(pixelsFrame['diffFiveDown'].mean(), inplace= True)
    pixelsFrame['diffTenDown'].fillna(pixelsFrame['diffTenDown'].mean(), inplace = True)

    pixelsFrame['diffFiveUpLeft'].fillna(pixelsFrame['diffFiveUpLeft'].mean(), inplace= True)
    pixelsFrame['diffTenUpLeft'].fillna(pixelsFrame['diffTenUpLeft'].mean(), inplace= True)
    pixelsFrame['diffFiveUpRight'].fillna(pixelsFrame['diffFiveUpRight'].mean(), inplace= True)
    pixelsFrame['diffTenUpRight'].fillna(pixelsFrame['diffTenUpRight'].mean(), inplace= True)

    pixelsFrame["diffFiveUp"]    = pixelsFrame["diffFiveUp"].apply(categoryYo)
    pixelsFrame["diffTenUp"]     = pixelsFrame["diffTenUp"].apply(categoryYo)
    pixelsFrame["diffFiveLeft"]  = pixelsFrame["diffFiveLeft"].apply(categoryYo)
    pixelsFrame["diffTenLeft"]   = pixelsFrame["diffTenLeft"].apply(categoryYo)
    pixelsFrame["diffFiveRight"] = pixelsFrame["diffFiveRight"].apply(categoryYo)
    pixelsFrame["diffTenRight"]  = pixelsFrame["diffTenRight"].apply(categoryYo)
    pixelsFrame["diffFiveDown"]  = pixelsFrame["diffFiveDown"].apply(categoryYo)
    pixelsFrame["diffTenDown"]   = pixelsFrame["diffTenDown"].apply(categoryYo)

    pixelsFrame['diffFiveUpLeft']  = pixelsFrame['diffFiveUpLeft'].apply(categoryYo)
    pixelsFrame['diffTenUpLeft']   = pixelsFrame['diffTenUpLeft'].apply(categoryYo)
    pixelsFrame['diffFiveUpRight'] = pixelsFrame['diffFiveUpRight'].apply(categoryYo)
    pixelsFrame['diffTenUpRight']  = pixelsFrame['diffTenUpRight'].apply(categoryYo)

    return pixelsFrame

def category(data):
    if data > 30000:
        return 1
    else:
        return 0

def categoryYo(data):
    if (data > -3000 and data < 3000):
        return 2
    elif (data < -3000):
        return 1
    else:
        return 0
