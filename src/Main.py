## Graynne program
#  Entry for DeltaHacks V
#  Tim Choy, Sam Crawford, Lewis Rafuse, and Cameron Dufault

#import sys
import PySimpleGUI as sg

from Confusion import *
from DataFrame import genDataFrame
from FileIO import *
from Process import *

def main():

    # # Assumes Target 1
    # pics     = 1
    # fileRRGB = "../../fake_microstructure/Target_1/image_"
    # fileMask = "../../fake_microstructure/Target_1/p2mask_np_"
    # fileName = "../../fake_microstructure/Target_1/image_" + str(num) + ".png"

    # readRGB     = genReadRGB(fileRRGB, pics)
    # mask        = genMask(fileMask, pics)
    # dataFrame   = genDataFrame(readRGB, mask)

    # x_train, x_test, y_train, y_test = genTrainTest(dataFrame)
    # logmodel    = genLogModel(x_train, y_train)
    # predictions = genPredictions(fileName, logmodel)
    # conMatrix   = genConMatrix(logmodel, x_test, y_test)

    # writeGraynne(predictions)

    # print(conMatrix)
    # print("The accuracy of this run is {:.2%}".format(calcAccuracy(conMatrix)))
    # ####################################################################
    # Assumes 
    fileDialogue = [      
        [sg.Text("Choose an Input File", size=(35, 1))], 
        [sg.Text("Input File", size=(15,1), auto_size_text=False, justification="right"),
         sg.InputText("Select File"), sg.FileBrowse()],     
        [sg.CloseButton("Submit"), sg.CloseButton("Cancel")]
    ]
    
    fileWindow = sg.Window('Graynne GUI').Layout(fileDialogue)
    button, values = fileWindow.Read()

    fileName = values[0]
    #print(button, fileName)

    pics = 1

    # gets num
    if fileName[-6] == "_":
        num = int(fileName[-5])
        fileRRGB = fileName[:-5]
        fileMask = fileName[:-11] + "p2mask_np_"
    elif fileName[-7] == "_":
        fileRRGB = fileName[:-6]
        fileMask = fileName[:-12] + "p2mask_np_"
        num = int(fileName[-6:-4])
    elif fileName[-8] == "_":
        fileRRGB = fileName[:-7]
        fileMask = fileName[:-13] + "p2mask_np_"
        num = int(fileName[-7:-4]) 
    else:
        print("BAD") # TODO: raise exception
    
    readRGB     = genReadRGB(fileRRGB, pics)
    mask        = genMask(fileMask, pics)
    dataFrame   = genDataFrame(readRGB, mask)

    x_train, x_test, y_train, y_test = genTrainTest(dataFrame)
    logmodel    = genLogModel(x_train, y_train)
    predictions = genPredictions(fileName, logmodel)
    conMatrix   = genConMatrix(logmodel, x_test, y_test)

    fractionDark = writeGraynne(predictions)

    #print(conMatrix)
    #garbage = input("Press 'Enter' to continue...")
    
    outString = "The fraction of dark phase in the specified image is {:.3}, and the output has been written to: \n".format(fractionDark)
    outFile   = fileRRGB[:-35] + "DeltaHacks V/src/output.png"
    outStringBad = "The accuracy of this run is {:.2%}".format(calcAccuracy(conMatrix))
    outDialogue = [
        [sg.Text(outString + outFile +  "\n\n" + outStringBad)],
        [sg.CloseButton("OK")]
    ]

    outWindow = sg.Window('Graynne GUI').Layout(outDialogue)
    button = outWindow.Read()

main()