import os

for i in range(1, 26):
    if not os.path.exists(str(i)):
        os.mkdir(str(i))
    for path in [
        f"{i}/test.txt",
        f"{i}/input.txt",
        f"{i}/solution.py",
    ]:
        if not os.path.exists(path):
            open(path, "w")
    