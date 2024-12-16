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
        # If either are not parallel with P, no solution:
        if px * by != py * bx:
            return 0
        # With positive integers requirement
        # There can be a finite set of solutions or no solution
        # We search forward for any solution starting with
        a = 0
        while True:
            b = (px - a * ax) // bx
            # Check if this is an integer solution
            if (px - a * ax) % bx == 0:
                return 3 * a + b
            # If we overstepped, and still haven't found solution,
            # then there is no solution
            if b < 0:
                break
            a += 1
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
    machines = read("input.txt")
    part1, part2 = 0, 0
    for machine in machines.values():
        part1 += solve(*machine)
        machine[4] += 10_000_000_000_000
        machine[5] += 10_000_000_000_000
        part2 += solve(*machine)
    print(part1, part2)
