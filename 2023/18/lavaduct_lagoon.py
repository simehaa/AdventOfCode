import random, re

instructions = []
for l in open("input.txt").readlines():
    d, s, c = l.split()
    instructions.append({
        "direction": [(0, 1), (1, 0), (0, -1), (-1, 0)][["R", "D", "L", "U"].index(d)],
        "steps": int(s),
        "color": c[1:-1],
    })


# dig trench
y, x = 0, 0
dug_out = [(y, x)]
for ins in instructions:
    dy, dx = ins["direction"]
    for s in range(ins["steps"]):
        y += dy
        x += dx
        if (y, x) not in dug_out:
            dug_out.append((y, x))

min_y = 1e10
min_x = 1e10
max_y = -1e10
max_x = -1e10
for y, x in dug_out:
    min_y = min(min_y, y)
    min_x = min(min_x, x)
    max_y = max(max_y, y)
    max_x = max(max_x, x)

# find one coordinate on the inside
while True:
    y = random.randint(min_y+1, max_y)
    x = random.randint(min_x+1, max_x)
    if (y, x) in dug_out:
        continue
    row = ""
    for i in range(x, max_x+1):
        if (y, i) in dug_out:
            row += "#"
        else:
            row += "."
    matches = re.findall(r"\#+", row)
    if len(matches) % 2 == 1:
        inside = (y, x)
        break

# flood fill from inside
inner_coordinates = [inside]
for y, x in inner_coordinates:
    for ny, nx in [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]:
        if (ny, nx) not in dug_out and (ny, nx) not in inner_coordinates:
            inner_coordinates.append((ny, nx))

# for y in range(min_y, max_y+1):
#     for x in range(min_x, max_x+1):
#         if (y, x) in inner_coordinates:
#             print("O", end="")
#         elif (y, x) in dug_out:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()
    
print(len(dug_out) + len(inner_coordinates))