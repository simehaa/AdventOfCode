def solve(filename):
    with open(filename) as f:
        grid = f.read().splitlines()
    h, w = len(grid), len(grid[0])
    visited = set()
    part1 = 0
    part2 = 0
    for y in range(h):
        for x in range(w):
            if (y, x) in visited:
                continue
            # Exploring garden plot
            visited.add((y, x))
            plant = grid[y][x]
            group_coor = [(y, x)]
            facings = [set() for i in range(4)]
            circumference = 0
            for yy, xx in group_coor:
                neighbors = [
                    (yy + 1, xx, 0),  # down
                    (yy - 1, xx, 1),  # up
                    (yy, xx + 1, 2),  # right
                    (yy, xx - 1, 3),  # left
                ]
                circumference += 4
                for yn, xn, face in neighbors:
                    if not (0 <= xn < w and 0 <= yn < h):
                        facings[face].add((yy, xx))
                        continue
                    if grid[yn][xn] == plant:
                        circumference -= 1
                        if (yn, xn) not in visited:
                            group_coor.append((yn, xn))
                            visited.add((yn, xn))
                    else:
                        facings[face].add((yy, xx))
            sides = circumference
            for i, coors in enumerate(facings):
                coors = list(coors)
                n = len(coors)
                for j in range(n - 1):
                    for k in range(j, n):
                        y1, x1 = coors[j]
                        y2, x2 = coors[k]
                        if abs(y2 - y1) + abs(x2 - x1) == 1:
                            sides -= 1
            part1 += len(group_coor) * circumference
            part2 += len(group_coor) * sides
    print(part1, part2)


solve("test.txt")
solve("larger_test.txt")
solve("input.txt")
