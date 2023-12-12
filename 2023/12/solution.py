def readfile(filename, part=1):
    springs = []
    groups = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            spring, group = line.rstrip().split()
            group = tuple(map(int, group.split(",")))
            if part == 1:
                springs.append(spring + ".")
                groups.append(group)
            else:
                springs.append(((spring+"?")*5)[:-1] + ".")
                groups.append(group*5) 
    return springs, groups


cache = {}
def count_arrangements(spring, group):
    if (spring, group) in cache:
        return cache[(spring, group)]
    elif spring == "":
        return group == ()
    elif group == ():
        return "#" not in spring
    arrangements = 0
    size = group[0]
    length = len(spring)
    for start in range(length-size):
        stop = start+size
        if any([s == "#" for s in spring[start-1]]):
            break
        elif spring[stop] == "#":
            continue
        elif all([s in "?#" for s in spring[start:stop]]):
            arrangements += count_arrangements(spring[stop+1:], group[1:])
    cache[(spring, group)] = arrangements
    return arrangements    


if __name__ == "__main__":
    for filename in ["test.txt", "input.txt"]:
        for part in [1, 2]:
            springs, groups = readfile(filename, part=part)
            total_sum_of_arrangements = 0
            for spring, group in zip(springs, groups):
                total_sum_of_arrangements += count_arrangements(spring, group)
            print(filename, f"Part {part}:", total_sum_of_arrangements)
