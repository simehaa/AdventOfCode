from heapq import heappop, heappush


def djikstra(grid, least=1, most=3):
    height = len(grid)
    width = len(grid[0])
    goal = (height - 1, width - 1)
    priority_queue = [(0, 0, 0, 0, 1, 0), (0, 0, 0, 1, 0, 0)]  # (heat_loss, y, x, dy, dx, steps)
    visited = set()
    while priority_queue:
        # Check the highest priority path (by lowest heat loss)
        heat_loss, y, x, dy, dx, steps = heappop(priority_queue)

        # Check if we're reached the end
        if (y, x) == goal:
            return heat_loss

        # Check if we've visited this exact state
        if (y, x, dy, dx, steps) in visited:
            continue
        visited.add((y, x, dy, dx, steps))

        # continue in same direction
        if steps < most and 0 <= y + dy < height and 0 <= x + dx < width:
            heappush(
                priority_queue,
                (heat_loss + grid[y + dy][x + dx], y + dy, x + dx, dy, dx, steps + 1),
            )

        # turn right and left
        if steps >= least:
            for new_dy, new_dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if (
                    (new_dy, new_dx) != (dy, dx)  # same direction already added to queue
                    and (new_dy, new_dx) != (-dy, -dx)  # not allowed to go back
                    and 0 <= y + new_dy < height
                    and 0 <= x + new_dx < width
                ):
                    heappush(
                        priority_queue,
                        (
                            heat_loss + grid[y + new_dy][x + new_dx],
                            y + new_dy,
                            x + new_dx,
                            new_dy,
                            new_dx,
                            1,
                        ),
                    )


grid = [[int(c) for c in l.rstrip()] for l in open("test.txt")]
print("Part 1:", djikstra(grid, most=3))
print("Part 2:", djikstra(grid, least=4, most=10))
