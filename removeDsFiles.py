import os

def traverse(path, limit = 0):
    if limit == 100:
        return
    for x in os.listdir(path):
        if x[0].isalnum() and os.path.isdir(path+ f"/{x}"):
            traverse(path + f"/{x}", limit+1)
        elif x == ".DS_Store":
            os.remove(path + f"/{x}")


if __name__ == "__main__":
    traverse(os.getcwd())
   