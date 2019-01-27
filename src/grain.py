# grain.py

from numpy import *
import pandas as pd
from PIL import Image
from copy import *
from diffs import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

pixels_dict = {}
readRGB     = []
solvedCat   = []
numOfPics   = 20
def readGraynne(image_name):
    img = Image.open(image_name, 'r').convert('I')
    data = asarray(img)
    return data

for i in range(numOfPics):
    readRGB.append(reshape(readGraynne("../../fake_microstructure/Target_1/image_" + str(i) + ".png"), 1048576))

for i in range(numOfPics):
    solvedCat.append(reshape(readGraynne("../../fake_microstructure/Target_1/p2mask_np_" + str(i) + ".png"), 1048576))
    
readRGB = reshape(readRGB, int(1048576 * numOfPics))
solvedCat = reshape(solvedCat,int(1048576 * numOfPics))
    
pixelsFrame = pd.DataFrame(pixels_dict)

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

count = 0
def category(data):
    if data > 30000:
        return 1
    else:
        count = 1
        return 0
    
def categoryYo(data):
    if (data > -3000 and data < 3000):
        return 2
    elif (data < -3000):
        return 1
    else:
        return 0

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


# pixelsFrame.to_csv("output.csv")

# file = "output.csv"
# chunksize = 10 ** 6
# pixelsFrame = pd.read_csv(file, chunksize=chunksize)

# pixelsFrame = pd.DataFrame()
# with open(file) as fl:
#     chunk_iter = pd.read_csv(fl, chunksize = chunksize)
#     for chunk in chunk_iter:
#         chunk = chunk[chunk['column1'] > 180]
#         pixelsFrame = pd.concat([pixelsFrame,chunk])

# print("We read it good :)")

x = pixelsFrame.drop('solved Cat', axis = 1)
y = pixelsFrame['solved Cat']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)
predictions = logmodel.predict(x_test)

print(confusion_matrix(y_test, predictions))