## Graynne program
#  Entry for DeltaHacks V
#  Tim Choy, Sam Crawford, Lewis Rafuse, and Cameron Dufault

#import sys
import PySimpleGUI as sg
from ReadGraynne import *

def main():
    layout = [      
             [sg.Text("Choose an Input File", size=(35, 1))], 
             [sg.Text("Input File", size=(15,1), auto_size_text=False, justification="right"),
              sg.InputText("Select File"), sg.FileBrowse()],     
             [sg.Submit(), sg.Cancel()]    
             ]
    
    window = sg.Window('Graynne GUI').Layout(layout)
    button, values = window.Read()

    print(button, values[0])
    
    printList = readGraynne(values[0])

    for i in printList:
        for j in i:
            print(str(j), end=" ")
        print("\n")

main()