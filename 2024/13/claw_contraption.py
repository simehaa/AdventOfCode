import re


def read(filename):
    machines = {}
    with open(filename) as f:
        for i, l in enumerate(f.readlines()):
            if i // 4 not in machines:
                machines[i // 4] = []
            machines[i // 4] += [int(n) for n in re.findall(r"\d+", l)]
    return machines


def solve(ax, ay, bx, by, px, py):
    determinant = ax * by - ay * bx
    if determinant == 0:
        # A and B vectors are parallel:
        # either no solution or if solution, then go for just B
        if px % bx and py % by:
            return px / bx
        return 0
    # Not linearly dependent: exactly one solution
    a = (px * by - py * bx) / determinant
    b = (ax * py - ay * px) / determinant
    # However, that one solution could have either negative a or b
    # or non-integer numbers, which we want to disregard
    if a < 0 or b < 0 or int(a) != a or int(b) != b:
        return 0
    return int(3 * a + b)


if __name__ == "__main__":
    machines = read("test.txt")
    part1, part2 = 0, 0
    for machine in machines.values():
        part1 += solve(*machine)
        machine[4] += 10_000_000_000_000
        machine[5] += 10_000_000_000_000
        part2 += solve(*machine)
    print(part1, part2)
