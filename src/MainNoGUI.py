# MainNoGUI.py

import warnings 
warnings.filterwarnings("ignore", category=UserWarning)
# Ignores Warning from higher version of pickle

from Confusion import *
from DataFrame import genDataFrame
from FileIO import writeGraynne
from Process import *

def main():
    invalid = True
    while invalid:
        print("Which kind of image would you like to measure?")
        print("\t 1) Standard")
        print("\t 2) With Particles")
        print("\t 3) Poor Lighting + Particles\n")
        tarInput = input("Enter selection: ")
        try:
            target = int(tarInput)
            if 0 < target and target < 4:
                invalid = False
            else:
                print("Input must be between 1 and 3 (inclusive)\n")
        except:
            print("Input must be an integer\n")

    invalid = True
    while invalid:
        numInput = input("Enter the image number you would like to analyze: ")
        try:
            num = int(numInput)
            if 0 <= num and num < 200:
                invalid = False
            else:
                print("Input must be between 0 and 199 (inclusive)\n")
        except:
            print("Input must be an integer\n")

    fileName = "../../fake_microstructure/Target_" + str(target) + "/image_" + str(num) + ".png"

    logmodel    = genLogModel()
    predictions = genPredictions(fileName, logmodel)

    fractionDark = writeGraynne(predictions)

    print("\nThe fraction of dark phase in the specified image is {:.3}, and the output has been written to: ".format(fractionDark))
    print("\t../../DeltaHacks V/src/output.png")

main()