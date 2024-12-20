def get_nodes(grid, part1=True):
    h, w = len(grid), len(grid[0])
    start = (0, 1)
    end = (h - 1, w - 2)
    nodes = [start, end]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
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
            if not (0<=ny<h and 0<=nx<w) or grid[ny][nx] == "#":
                continue
            if part1 and grid[ny][nx] in arrows and grid[ny][nx] != arrows[d]:
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
                    nd = (d+nd)%4
                    dy, dx = dirs[nd]
                    c = grid[ny+dy][nx+dx]
                    if c == "#":
                        continue
                    if part1 and c in arrows and c != arrows[nd]:
                        continue
                    path.append((ny+dy, nx+dx, nd))
                    break
    return costs


if __name__ == "__main__":
    with open("input.txt") as f:
        grid = [list(l) for l in f.read().splitlines()]
    cost_matrix = get_nodes(grid, part1=False)
    for row in cost_matrix:
        print(row)
    # Using the costs matrix, we start at node 0, and can then jump
    # from node to node, sometimes we have multiple choices, but
    # we're never allowed to visit the same node twice, until we
    # reach the end
    hikes = []
    print("Simulating node jump")

    from functools import cache
    @cache
    def dfs(nodes, total_cost):
        print(len(nodes))
        current = nodes[-1]
        if current == 1:
            hikes.append(total_cost)
            return
        for other, cost in enumerate(cost_matrix[current]):
            if cost == 0 or other in nodes:
                continue
            dfs((*nodes, other), total_cost + cost)
        return

    dfs((0,), 0)
    print(max(hikes))


