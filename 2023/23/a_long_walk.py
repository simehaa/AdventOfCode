def get_nodes(grid, start, end):
    # Find all nodes (points with more than two connections)
    nodes = [start, end]
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if grid[y][x] != ".":
                continue
            if sum([grid[y + dy][x + dx] != "#" for dy, dx in dirs]) > 2:
                nodes.append((y, x))
    return nodes


if __name__ == "__main__":
    with open("test.txt") as f:
        grid = [list(l) for l in f.read().splitlines()]

    h, w = len(grid), len(grid[0])
    start = (0, 1)  # start y and x
    end = (h - 1, w - 2)  # end y and x
    nodes = get_nodes(grid, start, end)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
    arrows = ["^", ">", "v", "<"]

    for y, x in nodes:
        print("at node", y, x)
        # Try expanding out in all four directions
        for d in range(4):
            dy, dx = dirs[d]
            ny, nx = y + dy, x + dx
            if not (0<=ny<h and 0<=nx<w):
                continue
            if grid[ny][nx] == "#":
                continue
            while True:
                for nd in range(4):

