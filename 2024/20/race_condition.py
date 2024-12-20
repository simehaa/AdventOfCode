def solve(filename, seconds=2):
    grid = []
    with open(filename) as f:
        for y, line in enumerate(f.readlines()):
            row = list(line)
            grid.append(row)
            for x, c in enumerate(row):
                if c == "S":
                    start = (y, x)
                if c == "E":
                    end = (y, x)

    # Create a very handy lookup table 'path' where each coordinate along the
    # path is a key, and its value is the distance from the start
    path = {start: 0}
    distance = 0
    y, x = start
    while (y, x) != end:
        distance += 1
        for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            if (ny, nx) in path:
                continue
            if grid[ny][nx] != "#":
                path[(ny, nx)] = distance
                y, x = ny, nx
                break

    # Check all possible cheats
    cheats = 0
    for (y, x), distance in path.items():
        # Loop over all possible dy, dx so that
        # abs(dy) + abs(dx) <= seconds (Manhattan distance)
        for dy in range(-seconds, seconds + 1):
            for dx in range(abs(dy) - seconds, -abs(dy) + seconds + 1):
                ny, nx = y + dy, x + dx
                if (ny, nx) not in path:
                    continue
                if path[(ny, nx)] - distance - abs(dy) - abs(dx) >= 100:
                    cheats += 1
    print(cheats)


solve("input.txt", 2)
solve("input.txt", 20)
