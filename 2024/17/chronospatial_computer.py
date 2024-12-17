def run(a):
    """Specific for my input program"""
    b = (a & 7) ^ 7
    b ^= (a >> b) ^ 7
    return b & 7


def solve(a):
    out = []
    while True:
        out.append(run(a))
        a >>= 3
        if a == 0:
            return out


def find(program, ans):
    if len(program) == 0:
        solutions.add(ans)
        return
    for i in range(8):
        a = (ans << 3) + i
        if run(a) == program[-1]:
            find(program[:-1], a)
    return


program = [2, 4, 1, 7, 7, 5, 1, 7, 4, 6, 0, 3, 5, 5, 3, 0]
print(",".join(str(s) for s in solve(66245665)))
solutions = set()
find(program, 0)
print(min(solutions))
