import os 

differentCounts = {
    "Assembly": 0,
    "C++": 0,
    "Java": 0,
    "JavaScript": 0,
    "Python": 0,
    "Ruby": 0,
    "Text File": 0
}

formats = {
    "py": "Python",
    "cpp": "C++",
    "hpp": "C++",
    "h": "C++",
    "java": "Java",
    "js": "JavaScript",
    "rb": "Ruby",
    "asm": "Assembly",
    "txt": "Text File",
    "text": "Text File"
}


def countLines(filePath: str, countType: str) -> None:
    try:
        File = open(filePath, "r")
        count = 0
        for line in File:
            line = line.strip()
            if line != "":
                count += 1
        differentCounts[countType] += count

        File.close()
    except UnicodeDecodeError:
        pass


def traverse(path: str) -> None:
    for x in os.listdir(path):
        if os.path.isdir(f"{path}/{x}"):
            traverse(f"{path}/{x}")
        else:
            endType = x[x.rfind(".")+1:]
            if endType in formats.keys():
                countLines(f"{path}/{x}", formats[endType])


if __name__ == "__main__":
    traverse(os.getcwd())
    for x, y in differentCounts.items():
        print(f"{x} Counts: {y}")
