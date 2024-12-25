with open("input.txt") as f:
    schematics = f.read().split("\n\n")

keys = []
locks = []
for scheme in schematics:
    lines = scheme.splitlines()
    heights = [0] * 5
    for line in lines[1:-1]:
        for i, c in enumerate(line):
            heights[i] += (c == "#")
    if lines[0] == "#####":
        locks.append(heights)
        continue
    keys.append(heights)

total = 0
for k in keys:
    for l in locks:
        if all([k[i] + l[i] <= 5 for i in range(5)]):
            total += 1

print(total)
