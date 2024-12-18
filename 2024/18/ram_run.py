from heapq import heappop, heappush


def djikstra(side, bytes):
    queue = [(0, 0, 0)]  # steps, x, y
    visited = set(bytes)
    while queue:
        steps, x, y = heappop(queue)
        if (x, y) == (side, side):
            return steps
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if not 0 <= nx <= side or not 0 <= ny <= side:
                continue
            heappush(queue, (steps + 1, nx, ny))
    return None


def solve(filename, side, byte):
    with open(filename) as f:
        bytes = [eval(line) for line in f.read().splitlines()]
    print("Part 1:", djikstra(side, bytes[:byte]))
    lower, upper = byte, len(bytes)
    failed = set()
    while upper - lower > 1:
        mid = lower + (upper - lower) // 2
        if djikstra(side, bytes[: mid + 1]):
            lower = mid
        else:
            upper = mid
            failed.add(mid)
    x, y = bytes[min(failed)]
    print(f"Part 2: {x},{y}")


solve("test.txt", 6, 12)
solve("input.txt", 70, 1024)
