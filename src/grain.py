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
def readGraynne(image_name):
    img = Image.open(image_name, 'r').convert('I')
    data = asarray(img)
    return data

for i in range(20):
    readRGB.append(reshape(readGraynne("../../../fake microstructure/Target 1/image_" + str(i) + ".png"),1048576))

for i in range(20):
    solvedCat.append(reshape(readGraynne("../../../fake microstructure/Target 1/p2mask_np_" + str(i) + ".png"),1048576))
    
readRGB = reshape(readRGB, int(20971520))
solvedCat = reshape(solvedCat,int(20971520))
    
pixelsFrame = pd.DataFrame(pixels_dict)

pixelsFrame['originalRGB'] = readRGB
pixelsFrame['solved Cat']  = solvedCat

pixelsFrame['dif5Right'] = fiveRight(readRGB)
pixelsFrame['dif10Right'] = tenRight(readRGB)

pixelsFrame['dif5Up'] = fiveUp(readRGB)
pixelsFrame['dif10Up'] = tenUp(readRGB)

pixelsFrame['dif5Left'] = fiveLeft(readRGB)
pixelsFrame['dif10Left'] = tenLeft(readRGB)

pixelsFrame['dif5down'] = fiveDown(readRGB)
pixelsFrame['dif10down'] = tenDown(readRGB)

pixelsFrame['dif5UpRight'] = fiveUpRight(readRGB)
pixelsFrame['dif10UpRight'] = tenUpRight(readRGB)

pixelsFrame['dif5UpLeft'] = fiveUpLeft(readRGB)
pixelsFrame['dif10UpLeft'] = tenUpLeft(readRGB)

pixelsFrame['dif5Right'].fillna(pixelsFrame['dif5Right'].mean(),inplace = True)
pixelsFrame['dif10Right'].fillna(pixelsFrame['dif10Right'].mean(), inplace = True)
pixelsFrame['dif5Up'].fillna(pixelsFrame['dif5Up'].mean(), inplace = True)
pixelsFrame['dif10Up'].fillna(pixelsFrame['dif10Up'].mean(), inplace = True)
pixelsFrame['dif5Left'].fillna(pixelsFrame['dif5Left'].mean(), inplace = True)
pixelsFrame['dif10Left'].fillna(pixelsFrame['dif10Left'].mean(), inplace = True)

pixelsFrame['dif5down'].fillna(pixelsFrame['dif5down'].mean(), inplace= True)
pixelsFrame['dif10down'].fillna(pixelsFrame['dif10down'].mean(), inplace = True)

pixelsFrame['dif5UpRight'].fillna(pixelsFrame['dif5UpRight'].mean(), inplace= True)
pixelsFrame['dif10UpRight'].fillna(pixelsFrame['dif10UpRight'].mean(), inplace= True)
pixelsFrame['dif5UpLeft'].fillna(pixelsFrame['dif5UpLeft'].mean(), inplace= True)
pixelsFrame['dif10UpLeft'].fillna(pixelsFrame['dif10UpLeft'].mean(), inplace= True)

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

pixelsFrame["dif10Right"] = pixelsFrame["dif10Right"].apply(categoryYo)
pixelsFrame["dif5Right"] = pixelsFrame["dif5Right"].apply(categoryYo)

pixelsFrame["dif10Left"] = pixelsFrame["dif10Left"].apply(categoryYo)
pixelsFrame["dif5Left"] = pixelsFrame["dif5Left"].apply(categoryYo)

pixelsFrame["dif10Up"] = pixelsFrame["dif10Up"].apply(categoryYo)
pixelsFrame["dif5Up"] = pixelsFrame["dif5Up"].apply(categoryYo)

pixelsFrame["dif10down"] = pixelsFrame["dif10down"].apply(categoryYo)
pixelsFrame["dif5down"] = pixelsFrame["dif5down"].apply(categoryYo)

pixelsFrame['dif10UpRight'] = pixelsFrame['dif10UpRight'].apply(categoryYo)
pixelsFrame['dif5UpRight'] = pixelsFrame['dif5UpRight'].apply(categoryYo)

pixelsFrame['dif10UpLeft'] = pixelsFrame['dif10UpLeft'].apply(categoryYo)
pixelsFrame['dif5UpLeft'] = pixelsFrame['dif5UpLeft'].apply(categoryYo)

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