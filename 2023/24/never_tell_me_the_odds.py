def read(filename):
    with open(filename) as f:
        return [eval(l.replace("@", ",")) for l in f.readlines()]


def part1(hails):
    mi, ma = 200_000_000_000_000, 400_000_000_000_000
    n = len(hails)
    counter = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            x1, y1, z1, vx1, vy1, vz1 = hails[i]
            x2, y2, z2, vx2, vy2, vz2 = hails[j]
            det = vy1 * vx2 - vx1 * vy2
            if det == 0:
                continue
            t1 = ((y2 - y1)*vx2 - (x2 - x1)*vy2) / det
            t2 = ((y2 - y1)*vx1 - (x2 - x1)*vy1) / det
            if t1 < 0 or t2 < 0:
                continue
            x = x1 + vx1*t1
            y = y1 + vy1*t1
            if (mi <= x <= ma) and (mi <= y <= ma):
                counter += 1
    return counter


def part2(hails):



if __name__ == "__main__":
    hails = read("input.txt")
    print(part1(hails))
