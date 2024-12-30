def read(filename):
    with open(filename) as f:
        grid = [list(l) for l in f.read().splitlines()]
    return grid


def get_edge_cost_matrix(grid, part=1):
    h, w = len(grid), len(grid[0])
    start = (0, 1)
    end = (h - 1, w - 2)
    nodes = [start, end]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    arrows = ["^", ">", "v", "<"]
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if grid[y][x] != ".":
                continue
            if sum([grid[y + dy][x + dx] != "#" for dy, dx in dirs]) > 2:
                nodes.append((y, x))
                grid[y][x] = "N"
    n = len(nodes)
    costs = [[0 for i in range(n)] for i in range(n)]
    for y, x in nodes:
        this = nodes.index((y, x))
        # Try expanding out in all four directions
        paths = []
        for d, (dy, dx) in enumerate(dirs):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w) or grid[ny][nx] == "#":
                continue
            if part == 1 and grid[ny][nx] in arrows and grid[ny][nx] != arrows[d]:
                continue
            paths.append([(ny, nx, d)])
        # For each path branch, keep exploring until we reach another node
        for path in paths:
            for ny, nx, d in path:
                # Check if reached another node
                if (ny, nx) in nodes:
                    that = nodes.index((ny, nx))
                    costs[this][that] = len(path)
                    break
                # three options to go further: straight, left, or right
                for nd in [0, 1, 3]:
                    nd = (d + nd) % 4
                    dy, dx = dirs[nd]
                    c = grid[ny + dy][nx + dx]
                    if c == "#":
                        continue
                    if part == 1 and c in arrows and c != arrows[nd]:
                        continue
                    path.append((ny + dy, nx + dx, nd))
                    break
    return costs


if __name__ == "__main__":
    cost_matrix = get_edge_cost_matrix(read("test.txt"), part=2)

    def dfs(node, cost, visited):
        global max_cost
        if node == 1:
            max_cost = max(max_cost, cost)
            return
        for next_node, edge_cost in enumerate(cost_matrix[node]):
            if edge_cost and next_node not in visited:
                dfs(next_node, cost + edge_cost, visited | {next_node})

    max_cost = 0
    dfs(0, 0, {0})
    print(max_cost)
