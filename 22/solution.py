grid = []
with open("test.txt", "r") as f:
    for line in f:
        if "." in line or "#" in line:
            grid.append(line.rstrip())
        else:
            directions = f.readline()

print(directions)
for l in grid:
    print(l)