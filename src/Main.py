## Graynne program
#  Entry for DeltaHacks V
#  Tim Choy, Sam Crawford, Lewis Rafuse, and Cameron Dufault

#import sys
import PySimpleGUI as sg
from ReadGraynne import *

def main():
    fileDialogue = [      
        [sg.Text("Choose an Input File", size=(35, 1))], 
        [sg.Text("Input File", size=(15,1), auto_size_text=False, justification="right"),
         sg.InputText("Select File"), sg.FileBrowse()],     
        [sg.CloseButton("Submit"), sg.CloseButton("Cancel")]
    ]
    
    fileWindow = sg.Window('Graynne GUI').Layout(fileDialogue)
    button, values = fileWindow.Read()

    print(button, values[0])
    
    printList = readGraynne(values[0])

    #garbage = input("Press 'Enter' to continue...")

    darkPhase = 0.2614223074892 # For testing

    outString = "The percentage of dark phase in the specified image is {:.2%}".format(darkPhase)
    outDialogue = [
        [sg.Text(outString)],
        [sg.CloseButton("OK")]
    ]

    outWindow = sg.Window('Graynne GUI').Layout(outDialogue)
    button = outWindow.Read()
    
    writeGraynne(printList)

main()