import os 
from datetime import datetime

def extend(value: int) -> str or int:
    if value < 10:
        value = f"0{value}"

    return value


def createFile() -> None:
    currentDate = datetime.now()
    path = os.getcwd()
    os.system(f'code {path}/{extend(currentDate.month)},{extend(currentDate.day)}.py')


if __name__ == '__main__': 
    createFile()