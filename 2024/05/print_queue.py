def solve(filename):
    rules = {}
    prints = []
    with open(filename) as f:
        second_part = False
        for line in f.readlines():
            line = line.strip()
            if line == "":
                second_part = True
                continue
            if second_part:
                prints.append(list(eval(line)))
            else:
                a, b = line.split("|")
                a, b = int(a), int(b)
                if a in rules:
                    rules[a].append(b)
                else:
                    rules[a] = [b]

    def middle_number(p, fix=False):
        for i in range(len(p)):
            if p[i] not in rules:
                continue
            for j in range(i):
                if p[j] in rules[p[i]]:
                    if not fix:
                        return 0
                    p[i], p[j] = p[j], p[i]
                    return middle_number(p, fix=fix)
        return p[len(p) // 2]

    s = [0, 0]
    for p in prints:
        m = middle_number(p, fix=False)
        s[0] += m
        if m == 0:
            s[1] += middle_number(p, fix=True)
    print(s)


solve("test.txt")
solve("input.txt")
