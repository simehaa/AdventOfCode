from collections import deque

import numpy as np

# Square garden, start center, equal distance to each edge
# at each equivalent step in the repeating pattern n=0, 1, 2
# where 0 for example is right before a border crossing
# 1 is then right before the next border crossings (exactly side_length steps later)
# total number of garden plots must be a polynomial f(n) = a*n**2 + b*n + c
# Luckily 26501365 is right before a border crossing, so answer
# is f(26501365//side_length)
garden = [l.rstrip() for l in open("input.txt")]
side = len(garden)
half = side // 2
repetitions = 26_501_365 // side
visited = set()
even_odd_totals = [0, 0]
queue = deque([(half, half)])
steps_at_0_1_2 = []
for step in range(1, 2 * side + half + 1):
    for _ in range(len(queue)):
        y, x = queue.popleft()
        for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            if (ny, nx) not in visited and garden[ny % side][nx % side] in ".S":
                visited.add((ny, nx))
                queue.append((ny, nx))
                even_odd_totals[step % 2] += 1
    if step == 64:
        print("Part 1:", even_odd_totals[step % 2])
    if (step - half) % side == 0:
        steps_at_0_1_2.append(even_odd_totals[step % 2])

garden_plots = int(np.polyval(np.polyfit([0, 1, 2], steps_at_0_1_2, deg=2), repetitions).round())
print("Part 2:", garden_plots)
