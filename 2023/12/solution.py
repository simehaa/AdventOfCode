import itertools


def readfile(filename, part=1):
    springs = []
    groups = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            spring, group = line.rstrip().split()
            group = eval(group)
            if isinstance(group, int):
                group = (group)
            if part == 1:
                springs.append([s for s in spring])
                groups.append(group)
            else:
                spring = (spring+"?")*5
                springs.append([s for s in spring[:-1]])
                groups.append(group*5)
    return springs, groups


def _solve(springs, groups):
    arrangements = []
    for spring, its_group in zip(springs, groups):
        combinations = []
        for i, c in enumerate(spring):
            if c == "?":
                combinations.append(spring[:i] + ["#"] + spring[i+1:])
                combinations.append(spring[:i] + ["."] + spring[i+1:])
                break

        done_substituting = False
        while not done_substituting:
            new_combinations = []
            done_substituting = True
            for s in combinations:
                for i, c in enumerate(s):
                    if c == "?":
                        new_combinations.append(s[:i] + ["#"] + s[i+1:])
                        new_combinations.append(s[:i] + ["."] + s[i+1:])
                        done_substituting = False
                        break
            if not done_substituting:
                combinations = new_combinations

        arrangements_for_this_spring = 0
        for c in combinations:
            this_group = []
            group_begun = 0
            for i, s in enumerate(c):
                if s == "#":
                    group_begun += 1
                elif group_begun != 0:
                    this_group.append(group_begun)
                    group_begun = 0
            if group_begun != 0:
                this_group.append(group_begun)

            if len(its_group) == len(this_group):
                equal = True
                for i, j in zip(its_group, this_group):
                    if i != j:
                        equal = False
                if equal:
                    arrangements_for_this_spring += 1
        arrangements.append(arrangements_for_this_spring)
        
    return sum(arrangements)


def solve(springs, groups):
    arrangements_per_spring = []
    for spring, its_group in zip(springs, groups):

        combinations = []
        possible_groups = []
        group_begun = 0
        for i, char in enumerate(spring):
            if char in ["#", "?"]:
                group_begun += 1
            elif group_begun != 0:
                possible_groups.append(group_begun)
                group_begun = 0
        if group_begun != 0:
            possible_groups.append(group_begun)
        print(possible_groups, its_group)

        for left, right in zip(its_group[:-1], its_group[1:]):
            pass
    return sum(arrangements_per_spring)


if __name__ == "__main__":
    springs, groups = readfile("test.txt", part=1)

    print("Part 1:", solve(springs, groups))
    # print("Part 2:", solve(grid, part=2))
