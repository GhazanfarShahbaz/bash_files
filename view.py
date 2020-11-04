import argparse
import os
from sortedcontainers import SortedSet, SortedDict

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--folders", help="Dont include folders", type=int)
parser.add_argument("-c", "--config", help="Dont include configs", type=int)
parser.add_argument("-fl", "--files", help="Dont include files", type=int)

parser.add_argument("-d","--depth", help="Depth of view", type=int)
parser.add_argument("-t","--t", help="Type of files example: txt", type=str, nargs='+')

# parser.add_argument
args = parser.parse_args()


def printFolder(folder, tabs=""):
    if folder:
        print(tabs + "Folder")
        tabs += "\t"
        for x,y in folder.items():
            print(tabs, x)
            for name in y:
                if name  == "Folder":
                    printFolder(y[name], tabs + "\t")
                else:
                    if(y[name]):
                        print(tabs + "\t", name)
                        for k in y[name]:
                            print(tabs + "\t\t", k)  

def printSets(thisType, values, tabs, firstTab ="") -> None:
    if not values:
        return

    if firstTab:
        print(firstTab, thisType)
    else:
        print(thisType)

    for x in values:
        print(tabs, x)

def compareType(file: str, wantedType: str) -> bool:
    if len(file) < len(wantedType):
        return False
    return file[len(file)-1-len(wantedType):] == wantedType

def fill(folder, docs, config, currentDepth, path, includeFolders, includeFiles, includeConfig ):
    for x in os.listdir(path):
        if x[0].isalnum() and os.path.isdir(path + f"/{x}"):
            if includeFolders and currentDepth+1 <= args.depth:
                folder[x] = fill(SortedDict(), SortedSet(), SortedSet(), currentDepth+1, path + f"/{x}",includeFolders, includeFiles, includeConfig  ) 
        else:
            if x[0].isalnum() and (os.path.isfile(path + f"/{x}") or x[len(x)-4:] == ".pdf"):
                if includeFiles:
                    docs.add(x)
            elif includeConfig:
                config.add(x)

    return {"Folder": folder, "Config":config, "Documents":docs}


if __name__ == "__main__":
    folders = SortedDict()
    documents = SortedSet()
    config = SortedSet()
    includeFold = includeCon = includeFl = False

    if args.folders == 0:
        includeFold = True
    if args.config == 0:
        includeCon = True
    if args.files == 0:
        includeFl = True


    fill(folders, documents, config, 0, os.getcwd(), includeFold, includeFl, includeCon)
    
    printFolder(folders)

    printSets("Documents", documents, "\t")
    print()

    printSets("Config FIles", config, '\t')
    print()

