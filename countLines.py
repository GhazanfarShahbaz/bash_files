import os 
from stringcolor import * 

differentCounts = {
    "Assembly": 0,
    "C++": 0,
    "CSS": 0,
    "HTML": 0,
    "Java": 0,
    "JavaScript": 0,
    "Latex": 0,
    "Python": 0,
    "Ruby": 0,
    "Text File": 0,
    "Total Lines": 0
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
    "tex": "Latex",
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
        differentCounts["Total Lines"] += count

        File.close()
    except UnicodeDecodeError:
        pass


def traverse(path: str) -> None:
    try:
        for x in os.listdir(path):
            if x[0] != "." and x != "env":
                thisPath = f"{path}/{x}"
                if os.path.isdir(thisPath) and not thisPath in excludePaths and x != "node_modules":
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
        if x != "Total Lines":
            currentString = f"{cs(x + ' Counts', 'DodgerBlue').bold()}: {y}"
            while len(currentString) < 50:
                currentString += " "
            print(currentString, f"\t\t{cs(str(int((y/differentCounts['Total Lines'])*10000)/100), 'grey').bold()}%")
        else:
            print(f"{cs(x, 'DodgerBlue').bold()}: {y}")