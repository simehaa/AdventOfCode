def readfile(filename, part=1):
    springs = []
    groups = []
    for line in open(filename):
        spring, group = line.rstrip().split()
        group = tuple(map(int, group.split(",")))
        if part == 1:
            springs.append(spring + ".")
            groups.append(group)
        elif part == 2:
            springs.append(((spring + "?") * 5)[:-1] + ".")
            groups.append(group * 5)
    return springs, groups


cache = {}


def count_arrangements(spring, group):
    if (spring, group) in cache:
        return cache[(spring, group)]
    if spring == "":
        return group == ()
    if group == ():
        return "#" not in spring
    arrangements = 0
    size = group[0]
    length = len(spring)
    for start in range(length - size):
        stop = start + size
        if any([s == "#" for s in spring[start - 1]]):
            break
        if spring[stop] == "#":
            continue
        if all([s in "?#" for s in spring[start:stop]]):
            arrangements += count_arrangements(spring[stop + 1 :], group[1:])
    cache[(spring, group)] = arrangements
    return arrangements


def solve(springs, groups):
    total_sum_of_arrangements = 0
    for spring, group in zip(springs, groups):
        total_sum_of_arrangements += count_arrangements(spring, group)

    return total_sum_of_arrangements


print("Part 1:", solve(*readfile("test.txt", part=1)))
print("Part 2:", solve(*readfile("test.txt", part=2)))
