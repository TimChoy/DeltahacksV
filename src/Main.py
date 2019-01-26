## Graynne program
#  Entry for DeltaHacks V
#  Tim Choy, Sam Crawford, Lewis Rafuse, and Cameron Dufault

#import sys
import PySimpleGUI as sg
#from ReadGraynne import *

def main():
    layout = [      
            [sg.Text('Please enter your Name, Address, Phone')],      
            [sg.Text('Name', size=(15, 1)), sg.InputText('name')],      
            [sg.Text('Address', size=(15, 1)), sg.InputText('address')],      
            [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],      
            [sg.Submit(), sg.Cancel()]      
            ]
    
    window = sg.Window('Graynne GUI').Layout(layout)
    button, values = window.Read()

    print(button, values[0])


    # imgDir = sys.argv[1]
    # printList = readGraynne(imgDir)

    # for i in printList:
    #     for j in i:
    #         print(str(j), end=" ")
    #     print("\n")

main()