from numpy import *
import pandas as pd
from PIL import Image
from copy import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# chunksize = 10 ** 6
# chunks = pd.read_table("output.csv", chunksize=chunksize)
# pixelsFrame = pd.DataFrame()

# for chunk in pd.read_csv("output.csv", chunksize=chunksize):
#     process(chunk)
pixelsFrame = pd.read_csv("output.csv")

print("We read it good :)")

x = pixelsFrame.drop('solved Cat', axis = 1)
y = pixelsFrame['solved Cat']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)
predictions = logmodel.predict(x_test)

print(confusion_matrix(y_test, predictions))