# grain.py

from Confusion import *
from DataFrame import genDataFrame
from FileIO import writeGraynne
from Process import *

def main():
    # Assumes Target 1

    # commented for testing
    # invalid = True
    # while invalid:
    #     numInput = input("Enter the image number you would like to analyze: ")
    #     try:
    #         num = int(numInput)
    #         if 0 <= num and num < 200:
    #             invalid = False
    #         else:
    #             print("Input must be between 0 and 199 (inclusive)\n")
    #     except:
    #         print("Input must be an integer\n")

    num = 0 # for testing

    # Assumes Target 1
    pics     = 1
    filePath = "../../fake_microstructure/Target_1/image_"
    fileName = "../../fake_microstructure/Target_1/image_" + str(num) + ".png"

    readRGB     = genReadRGB(filePath, pics)
    mask        = genMask(filePath, pics)
    dataFrame   = genDataFrame(readRGB, mask)
    print("have dataFrame")

    x_train, x_test, y_train, y_test = genTrainTest(dataFrame)
    logmodel    = genLogModel(x_train, y_train)
    predictions = genPredictions(fileName, logmodel)
    conMatrix   = genConMatrix(logmodel, x_test, y_test)

    writeGraynne(predictions)

    print(conMatrix)
    print("The accuracy of this run is {:.2%}".format(calcAccuracy(conMatrix)))

main()