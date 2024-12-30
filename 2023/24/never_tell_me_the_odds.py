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
            t1 = ((y2 - y1) * vx2 - (x2 - x1) * vy2) / det
            t2 = ((y2 - y1) * vx1 - (x2 - x1) * vy1) / det
            if t1 < 0 or t2 < 0:
                continue
            x = x1 + vx1 * t1
            y = y1 + vy1 * t1
            if (mi <= x <= ma) and (mi <= y <= ma):
                counter += 1
    print("part 1:", counter)


def part2(hails):
    # consider hail 0, 1, ..., h vs. stone s
    # set times t0, t1, ..., th as the collision times
    # This gives us many equations with 6 unknowns (xs, ys, zs, vxs, vys, vzs)
    # 1) (x0 - xs)(vys - vy0) - (y0 - ys)(vxs - vx0) = 0
    # 2) (x0 - xs)(vzs - vz0) - (z0 - zs)(vxs - vx0) = 0
    # 3) (x1 - xs)(vys - vy1) - (y1 - ys)(vxs - vx1) = 0
    # 4) (x1 - xs)(vzs - vz1) - (z1 - zs)(vxs - vx1) = 0
    # ...
    # 5) (xh - xs)(vys - vyh) - (yh - ys)(vxs - vxh) = 0
    # 6) (xh - xs)(vzs - vzh) - (zh - zs)(vxs - vxh) = 0
    import sympy

    xs, ys, zs, vxs, vys, vzs = sympy.symbols("xs, ys, zs, vxs, vys, vzs")
    equations = []
    for xh, yh, zh, vxh, vyh, vzh in hails[:5]:
        equations.append((xh - xs) * (vys - vyh) - (yh - ys) * (vxs - vxh))
        equations.append((xh - xs) * (vzs - vzh) - (zh - zs) * (vxs - vxh))
    ans = sympy.solve(equations)[0]
    print("part 2:", ans[xs] + ans[ys] + ans[zs])


if __name__ == "__main__":
    hails = read("input.txt")
    part1(hails)
    part2(hails)
