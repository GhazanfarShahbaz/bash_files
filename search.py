import os
import argparse
from sortedcontainers import SortedSet


parser = argparse.ArgumentParser()
parser.add_argument("value", help="File or folder to search for", type=str)
parser.add_argument("-l", "--limit", type=int)
parser.add_argument("-o", "--open", type=int)
args = parser.parse_args()

def check(value, compare):
    if len(value) == 0 and value[0] == "*":
        return True
    elif "*" == value[0] and "*" == value[-1] and len(value) != 1 and len(compare) >= len(value):
        return value[1:len(value)-1] in compare
    elif "*" == value[0] and "*" != value[-1] and len(value) != 1 and len(compare) >= len(value):
        return compare[:len(value)-1] == value[1:]
    elif "*" != value[0] and "*" == value[-1] and len(value) != 1  and len(compare) >= len(value):
        return compare[len(compare)-len(value)+1:] == value[:len(value)-1]
    return value == compare

        

def search(currentPath, paths, value, limit):
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
    if args.limit == 0:
        args.limit = None

    paths = SortedSet()
    value = args.value
    search(os.getcwd(), paths, args.value, args.limit)
    for x in paths:
        print(x)
        if args.open and args.open >= 1:
            os.system(f"open {x}")