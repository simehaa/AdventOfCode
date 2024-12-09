def solve(filename):
    with open(filename) as f:
        grid = [l.strip() for l in f.readlines()]

    h = len(grid)
    w = len(grid[0])
    steps = ((-1, 0), (0, 1), (1, 0), (0, -1))
    d = 0
    for i in range(h):
        if "^" in grid[i]:
            y, x = (i, grid[i].index("^"))
            break

    def simulate(y, x, d, oy=-1, ox=-1):
        """
        y, x, d = start coordinates and direction
        oy, ox = additional obstacle (if -1, -1, then impossible to hit)
        """
        visited = set()
        visited_d = set()
        while True:
            # Check loop condition - exit criteria (won't happen in part 1)
            if (y, x, d) in visited_d:
                return {}

            # Log visits
            visited.add((y, x))
            visited_d.add((y, x, d))

            # Proposed move
            dy, dx = steps[d]
            ny, nx = y + dy, x + dx

            # Out of bounds - exit criteria
            if ny < 0 or ny == h or nx < 0 or nx == w:
                break

            # Hit obstacle - rotate
            if grid[ny][nx] == "#" or (ny == oy and nx == ox):
                d = (d + 1) % 4
                continue

            # No hit - perform move
            y, x = (ny, nx)

        return visited

    # Part 1
    path = simulate(y, x, d, -1, -1)
    print(len(path))

    # Part 2
    # Attempt to place obstacles on all path coordinates from part 1 (except start)
    path.remove((y, x))
    loops = 0
    for (oy, ox) in path:
        loops += not bool(simulate(y, x, d, oy, ox)) # Whenever we hit loop it returns empty set
    print(loops)

solve("test.txt")
solve("input.txt")
