# grain.py

from numpy import *
import pandas as pd
from PIL import Image
from copy import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

from DataFrame import genDataFrame

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

dataFrame = genDataFrame(readRGB, solvedCat)

x = dataFrame.drop('solved Cat', axis = 1)
y = dataFrame['solved Cat']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)
predictions = logmodel.predict(x_test)

print(confusion_matrix(y_test, predictions))

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
