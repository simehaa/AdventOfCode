from functools import cache


def solve(filename):
    with open(filename) as f:
        patterns, designs = f.read().split("\n\n")
    patterns = tuple(patterns.split(", "))

    @cache
    def dfs(target):
        if target == "":
            return 1
        matches = 0
        for pattern in patterns:
            p = len(pattern)
            if p > len(target):
                continue
            if target[:p] == pattern:
                matches += dfs(target[p:])
        return matches

    possible, combinations = 0, 0
    for design in designs.splitlines():
        c = dfs(design)
        possible += bool(c)
        combinations += c

    print("part 1:", possible)
    print("part 2:", combinations)


solve("test.txt")
solve("input.txt")
