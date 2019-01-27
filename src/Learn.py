from numpy import *
import pandas as pd
from PIL import Image
from copy import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# chunks = pd.read_table("output.csv", chunksize=chunksize)
# pixelsFrame = pd.DataFrame()

# for chunk in pd.read_csv("output.csv", chunksize=chunksize):
#     process(chunk)

file = "output.csv"
chunksize = 10 ** 6
#pixelsFrame = pd.read_csv(file, chunksize=chunksize)

pixelsFrame = pd.DataFrame()
with open(file) as fl:
    chunk_iter = pd.read_csv(fl, chunksize = chunksize)
    for chunk in chunk_iter:
        #chunk = chunk[chunk['column1'] > 180]
        pixelsFrame = pd.concat([pixelsFrame,chunk])

print("We read it good :)")

x = pixelsFrame.drop('solved Cat', axis = 1)
y = pixelsFrame['solved Cat']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)
predictions = logmodel.predict(x_test)

print(confusion_matrix(y_test, predictions))