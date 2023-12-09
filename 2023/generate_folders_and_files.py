import os

for i in range(1, 26):
    folder = f"{i:02d}"
    if not os.path.exists(folder):
        os.mkdir(folder)
    for path in [
        f"{folder}/test.txt",
        f"{folder}/input.txt",
        f"{folder}/solution.py",
    ]:
        if not os.path.exists(path):
            open(path, "w")
    