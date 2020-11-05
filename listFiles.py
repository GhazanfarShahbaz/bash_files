import os
from sortedcontainers import SortedSet, SortedDict

# Only using sorted set to keep it sorted, there wouldnt be duplicates in a directory


def printSets(thisType, values, tabs, firstTab =""):
    if not values:
        return

    if firstTab:
        print(firstTab, thisType)
    else:
        print(thisType)

    for x in values:
        print(tabs, x)


if __name__ == "__main__":
    folders = SortedDict()
    documents = SortedSet()
    config = SortedSet()

    for x in os.listdir():
        if x[0].isalnum() and os.path.isdir(os.getcwd() + f"/{x}"):

            folders[x] = {
                "Config Files": SortedSet(),
                "Documents": SortedSet(),
                "Folders": SortedSet()
            }

            newPath = os.getcwd() + f"/{x}"

            for y in os.listdir(newPath):
                if y[0].isalnum() and os.path.isdir(newPath + f"/{y}"):
                    folders[x]["Folders"].add(y)
                elif y[0].isalnum() and (os.path.isfile(newPath + f"/{y}") or y[len(y)-4:] == ".pdf"):
                    folders[x]["Documents"].add(y)
                else:
                    folders[x]["Config Files"].add(y)
        else:
            if x[0].isalnum() and (os.path.isdir(os.getcwd() + f"/{x}") or x[len(x)-4:] == ".pdf"):
                documents.add(x)
            else:
                config.add(x)

    printSets("Config FIles", config, '\t')
    print()

    printSets("Documents", documents, "\t")
    print()

    if folders:
        print("Folders:")
        for x, y in folders.items():
            print("\t", x)
            for fileType, z in y.items():
                printSets(fileType, z, "\t\t\t", "\t\t")