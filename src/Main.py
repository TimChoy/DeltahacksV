## Graynne program
#  Entry for DeltaHacks V
#  Tim Choy, Sam Crawford, Lewis Rafuse, and Cameron Dufault

import sys
from ReadGraynne import *

def main():
    imgDir = sys.argv[1]
    printList = readGraynne(imgDir)

    for i in printList:
        for j in i:
            print(str(j), end=" ")
        print("\n")

main()