import os
import argparse
from sortedcontainers import SortedSet


parser = argparse.ArgumentParser()

#Required argument
parser.add_argument("value", help="File or folder to search for", type=str)

#Optional Agruments
parser.add_argument("-l", "--limit", help="Limit the number of matching results", type=int)
parser.add_argument("-o", "--open",help="If this is greater than one then matching value will be open" type=int)
parser.add_argument("-a", "--action",help="Set a customized action in case if there are results" type=str)

args = parser.parse_args()

def check(value: str, compare: str) -> bool:
    """Checks if the file/folder name is the same as the searched value"""
    if len(value) == 0 and value[0] == "*":
        return True
    elif "*" == value[0] and "*" == value[-1] and len(value) != 1 and len(compare) >= len(value):
        return value[1:len(value)-1] in compare
    elif "*" != value[0] and "*" == value[-1] and len(value) != 1 and len(compare) >= len(value):
        return compare[:len(value)-1] == value[:len(value)-1]
    elif "*" != value[-1] and "*" != value[-1] and len(value) != 1  and len(compare) >= len(value):
        return compare[len(compare)-len(value)+1:] == value[1:]
    return value == compare

        

def search(currentPath: str, paths: SortedSet, value: str, limit: int):
    """Goes from the starting directory and then visites every file and directory within"""
    try:
        for x in os.listdir(currentPath):
            if limit and len(paths) >= limit:
                return
            if check(value,x):
                paths.add(currentPath + f"/{x}")
            if os.path.isdir(currentPath + f"/{x}"):
                search(currentPath + f"/{x}", paths, value, limit)
    except:
        pass


if __name__ == "__main__":
    if not args.action:
        args.action = "open"

    if args.limit == 0:
        args.limit = None

    paths = SortedSet()

    search(os.getcwd(), paths, args.value, args.limit)

    for x in paths:
        print(x)
        if args.open and args.open >= 1:
            os.system(f"{args.action} {x}")
