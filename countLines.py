import os 

differentCounts = {
    "Assembly": 0,
    "C++": 0,
    "CSS": 0,
    "HTML": 0,
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
    "html": "HTML",
    "css": "CSS",
    "java": "Java",
    "js": "JavaScript",
    "rb": "Ruby",
    "asm": "Assembly",
    "txt": "Text File",
    "text": "Text File"
}

excludePaths = {
    "/Users/ghazshahbaz/OneDrive - Hunter - CUNY",
    "/Users/ghazshahbaz/Applications",
    "/Users/ghazshahbaz/Agent",
    "/Users/ghazshahbaz/Desktop",			
    "/Users/ghazshahbaz/Library",				
    "/Users/ghazshahbaz/Movies",		
    "/Users/ghazshahbaz/Music",
    "/Users/ghazshahbaz/Pictures",
    "/Users/ghazshahbaz/Public",
    "/Users/ghazshahbaz/eniac",
    "/Users/ghazshahbaz/eniac.pub",
    "/Users/ghazshahbaz/VirtualBox VMs",
    "/Users/ghazshahbaz/login"
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
    try:
        for x in os.listdir(path):
            if x[0] != "." and x != "env":
                thisPath = f"{path}/{x}"
                if os.path.isdir(thisPath) and not thisPath in excludePaths:
                    traverse(thisPath)
                else:
                    endType = x[x.rfind(".")+1:]
                    if endType in formats.keys():
                        countLines(thisPath, formats[endType])
    except:
        pass


if __name__ == "__main__":
    traverse(os.getcwd())
    for x, y in differentCounts.items():
        print(f"{x} Counts: {y}")
