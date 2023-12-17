def read_file(filename):
    grid = []
    with open(filename) as f:
        for l in f:
            grid.append([int(c) for c in l.rstrip()])
    return grid


def path_finding(grid, most=3):
    height = len(grid)
    width = len(grid[0])
    goal = (height-1, width-1)
    cache = {}
    routes = [
        {"path": [(0, 0)], "heat_loss": 0},
    ]
    finished_routes = []
    for route in routes:
        # print("\nConsidering", route)

        # current position
        current_path = route["path"]
        current_heat_loss = route["heat_loss"]
        yp, xp = current_path[-1]
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            y = yp + dy
            x = xp + dx
            # Don't go outside grid, and don't go to a place
            # that we have been on before
            if (
                y < 0 or y == height 
                or x < 0 or x == width
                or (y, x) in current_path
            ):
                continue
            
            new_path = current_path + [(y, x)]
            new_heat_loss = current_heat_loss + grid[y][x]
            # print("\tExtension", new_path)
            
            steps = 0
            for i in range(1, len(new_path)): # -i = -1, -2, ...
                _dy = new_path[-i][0] - new_path[-i-1][0]
                _dx = new_path[-i][1] - new_path[-i-1][1]
                if (_dy, _dx) != (dy, dx):
                    break
                steps += 1
            if steps > most:
                # print("\tRemoved because", steps, "steps in one direction")
                continue

            if (y, x) == goal:
                finished_routes.append({"path": new_path, "heat_loss": new_heat_loss})
                continue

            state = (y, x, dy*steps, dx*steps)
            if (state in cache and new_heat_loss < cache[state]) or state not in cache:
                cache[state] = new_heat_loss
                # print("\tContinuing route")
                routes.append({"path": new_path, "heat_loss": new_heat_loss})

    sorted_routes = sorted(finished_routes, key=lambda d: d["heat_loss"])
    return sorted_routes[0]["heat_loss"]


print("Part 1:", path_finding(read_file("test.txt")))
