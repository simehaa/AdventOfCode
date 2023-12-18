area = 0
y, x = 0, 0
for l in open("input.txt").readlines():
    d, s, c = l.split()
    dy, dx = [(0, 1), (1, 0), (0, -1), (-1, 0)][["R", "D", "L", "U"].index(d)]
    steps = int(s)
    color = c[1:-1]
    ny = y + steps*dy
    nx = x + steps*dx
    area += (y + ny)*(x - nx) + steps
    y, x = ny, nx

print(int(area/2) + 1)