def solve(filename):
    with open(filename) as f:
        grid = [[int(c) for c in l.strip()] for l in f.readlines()]
    h, w = len(grid), len(grid[0])
    sum_of_scores, sum_of_ratings = 0, 0
    for Y in range(h):
        for X in range(w):
            if grid[Y][X] != 0:
                continue
            paths = [[(Y, X)]]
            scores = set()
            for path in paths:
                elevation = len(path) - 1
                y, x = path[-1]
                if elevation == 9:
                    scores.add((y, x))  # unique peaks
                    sum_of_ratings += 1  # total number of routes to this peak
                    continue
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if not (0 <= ny < h and 0 <= nx < w):
                        continue
                    if grid[ny][nx] == elevation + 1:
                        paths.append(path + [(ny, nx)])
            sum_of_scores += len(scores)
    print("Part 1:", sum_of_scores)
    print("Part 2:", sum_of_ratings)


solve("test.txt")
solve("input.txt")
