from heapq import heappop, heappush


def djikstra(filename):
    with open(filename) as f:
        grid = f.read().splitlines()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "S":
                sy, sx = y, x
            if c == "E":
                ey, ex = y, x

    visited = dict()
    queue = [(0, 0, [(sy, sx)])]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    best_score = 1e9
    best_seats = set()
    while queue:
        score, d, path = heappop(queue)
        y, x = path[-1]

        # Goal
        if (y, x) == (ey, ex):
            if score <= best_score:
                best_score = score
                best_seats.update(path)
                continue
            break

        # Limit visited coordinates with same direction
        key = (y, x, d)
        if key in visited:
            if visited[key] > 10:  # 10 was actually needed for input.txt
                continue
            visited[key] += 1
        else:
            visited[key] = 1

        # Add potential new moves to queue
        for i in [0, 1, 3]:
            nd = (d + i) % 4
            dy, dx = dirs[nd]
            if i == 0:
                new_score = score + 1
                new_path = path + [(y + dy, x + dx)]
            else:
                new_score = score + 1000
                new_path = path
            if grid[y + dy][x + dx] != "#":
                heappush(queue, (new_score, nd, new_path))

    return best_score, len(best_seats)


for fn in ["test.txt", "larger_test.txt", "input.txt"]:
    p1, p2 = djikstra(fn)
    print(f"{fn}:\n\tpart 1: {p1}\n\tpart 2: {p2}")
