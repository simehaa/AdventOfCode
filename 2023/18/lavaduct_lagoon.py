def area_of_trench(filename, part=1):
    area = 0
    y, x = 0, 0
    for l in open(filename).readlines():
        d, s, c = l.split()
        if part == 1:
            dy, dx = [(0, 1), (1, 0), (0, -1), (-1, 0)][["R", "D", "L", "U"].index(d)]
            steps = int(s)
        elif part == 2:
            steps = int(c[2:-2], 16)
            d = int(c[-2], 16)
            dy, dx = [(0, 1), (1, 0), (0, -1), (-1, 0)][d]
        ny = y + steps*dy
        nx = x + steps*dx
        area += (y + ny)*(x - nx) + steps
        y, x = ny, nx
    return int(area/2) + 1


print("Part 1:", area_of_trench("test.txt", part=1))
print("Part 2:", area_of_trench("test.txt", part=2))
