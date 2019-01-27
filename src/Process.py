# Process.py

from numpy import *
#import pandas as pd
from PIL import Image
from copy import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from DataFrame import genImageDataFrame
from FileIO import readGraynne

def genReadRGB(filePath, pics):
    readRGB = []
    for i in range(pics):
        readRGB.append(readGraynne(filePath + str(i) + ".png"))
    readRGB = reshape(readRGB, int(1048576 * pics))
    return readRGB

def genMask(filePath, pics):
    mask = []
    for i in range(pics):
        mask.append(readGraynne(filePath + str(i) + ".png"))
    mask = reshape(mask,int(1048576 * pics))
    return mask

def genTrainTest(dataFrame):
    x = dataFrame.drop('solved Cat', axis = 1)
    y = dataFrame['solved Cat']

    return train_test_split(x, y, test_size=0.33, random_state=42)

def genLogModel(x_train, y_train):
    ##This is for testing
    logmodel = LogisticRegression()
    logmodel.fit(x_train, y_train)

    return logmodel

def genPredictions(fileName, logmodel):
    predictionImage = genImageDataFrame(readGraynne(fileName))
    predictions = logmodel.predict(predictionImage)

    return predictions
