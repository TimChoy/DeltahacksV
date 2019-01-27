from numpy import *
import pandas as pd
from PIL import Image
from copy import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

X = pixelsFrame.drop('solved Cat', axis = 1)
y = pixelsFrame['solved Cat']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

pixelsFrame = pd.read_csv("output.csv")

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

print(confusion_matrix(y_test, predictions))