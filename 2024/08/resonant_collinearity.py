import math


def solve(filename, part=1):
    with open(filename) as f:
        grid = [list(l.strip()) for l in f.readlines()]

    antennas = {}
    h = len(grid)
    w = len(grid[0])
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c != "." and c != "#":
                if c not in antennas:
                    antennas[c] = [(y, x)]
                else:
                    antennas[c].append((y, x))

    anti_nodes = set()
    for key, coors in antennas.items():
        n = len(coors)
        for i in range(n - 1):
            for j in range(i + 1, n):
                y0, x0 = coors[i]
                y1, x1 = coors[j]
                yn0, xn0 = 2 * y0 - y1, 2 * x0 - x1
                yn1, xn1 = 2 * y1 - y0, 2 * x1 - x0
                if yn0 >= 0 and yn0 < h and xn0 >= 0 and xn0 < w:
                    anti_nodes.add((yn0, xn0))
                if yn1 >= 0 and yn1 < h and xn1 >= 0 and xn1 < w:
                    anti_nodes.add((yn1, xn1))
                if part == 1:
                    continue
                dy = y1 - y0
                dx = x1 - x0
                gcd = abs(math.gcd(dy, dx))
                dy //= gcd
                dx //= gcd
                for dy, dx in [(dy, dx), (-dy, -dx)]:
                    for y, x in [(y0, x0), (y1, x1)]:
                        while 0 <= y < h and 0 <= x < w:
                            anti_nodes.add((y, x))
                            y += dy
                            x += dx
    print(len(anti_nodes))


solve("test.txt", part=1)
solve("test.txt", part=2)
solve("input.txt", part=1)
solve("input.txt", part=2)
