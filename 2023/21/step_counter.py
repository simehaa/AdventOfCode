garden = [l.rstrip() for l in open("input.txt")]
height = len(garden)
width = len(garden[0])


for y, row in enumerate(garden):
    if "S" in row:
        start = (y, row.index("S"))
        break


positions = [(start)]
steps = 64
for i in range(steps):
    new_positions = []
    for y, x in positions:
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y+dy, x+dx
            if garden[ny][nx] in ".S" and (ny, nx) not in new_positions:
                new_positions.append((ny, nx))
    positions = new_positions


print("Part 1:", len(positions))