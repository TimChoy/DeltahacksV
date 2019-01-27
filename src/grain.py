# grain.py

from numpy import *
import pandas as pd
from PIL import Image
from copy import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

from DataFrame import *
from Confusion import calcAccuracy
from FileIO import *

readRGB     = []
solvedCat   = []
numOfPics   = 1

for i in range(numOfPics):
    readRGB.append(readGraynne("../../fake_microstructure/Target_1/image_" + str(i) + ".png"))

for i in range(numOfPics):
    solvedCat.append(readGraynne("../../fake_microstructure/Target_1/p2mask_np_" + str(i) + ".png"))

readRGB   = reshape(readRGB,  int(1048576 * numOfPics))
solvedCat = reshape(solvedCat,int(1048576 * numOfPics))

dataFrame = genDataFrame(readRGB, solvedCat)

x = dataFrame.drop('solved Cat', axis = 1)
y = dataFrame['solved Cat']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

##This is for testing
predictionImage = genImageDataFrame(readGraynne("../../fake_microstructure/Target_1/image_0.png"))
logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)
predictions = logmodel.predict(predictionImage)

writeGraynne(predictions)


conMatrix = confusion_matrix(y_test, logmodel.predict(x_test))
print(conMatrix)
print("The accuracy of this run is {:.2%}".format(calcAccuracy(conMatrix)))
