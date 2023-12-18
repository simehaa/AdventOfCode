from heapq import heappush, heappop


def read_file(filename):
    grid = []
    with open(filename) as f:
        for l in f:
            grid.append([int(c) for c in l.rstrip()])
    return grid


def djikstra(grid, least=1, most=3):
    height = len(grid)
    width = len(grid[0])
    goal = (height-1, width-1)
    priority_queue = [(0, 0, 0, 0, 0, 0)] # (heat_loss, y, x, dy, dx, steps)
    visited = {}
    while priority_queue:
        # Check the highest priority path (by lowest heat loss)
        heat_loss, y, x, dy, dx, steps = heappop(priority_queue)

        # Check if we're reached the end
        if (y, x) == goal:
            return heat_loss

        # Check if we've visited coordinate
        # with same direction and same no. of steps
        # If so, then that must have had lower heat loss
        # since it was cached earlier in the priority queue
        if (y, x, dy, dx, steps) in visited:
            continue
        visited[(y, x, dy, dx, steps)] = heat_loss

        # continue in same direction
        if (
            steps < most 
            and (dy, dx) != (0, 0)
            and 0 <= y+dy < height 
            and 0 <= x+dx < width
        ):
            heappush(
                priority_queue,
                (heat_loss + grid[y+dy][x+dx], y+dy, x+dx, dy, dx, steps+1)
            )

        # turn
        if steps >= least or (dy, dx) == (0, 0):
            for new_dy, new_dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if (
                    (new_dy, new_dx) != (dy, dx) 
                    and (new_dy, new_dx) != (-dy, -dx)
                    and 0 <= y+new_dy < height
                    and 0 <= x+new_dx < width
                ):
                    heappush(
                        priority_queue,
                        (heat_loss + grid[y+new_dy][x+new_dx], y+new_dy, x+new_dx, new_dy, new_dx, 1)
                    )


print("Part 1:", djikstra(read_file("test.txt"), most=3))
print("Part 2:", djikstra(read_file("test.txt"), least=4, most=10))
