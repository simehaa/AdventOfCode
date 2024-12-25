def solve(filename):
    with open(filename) as f:
        initials, gates = f.read().split("\n\n")
    inputs = {}
    for line in initials.splitlines():
        name, value = line.split(": ")
        inputs[name] = int(value)
    gates = gates.splitlines()
    ops = {"AND": "&", "OR": "|", "XOR": "^"}
    while gates:
        for line in gates:
            left, op, right, _, ans = line.split()
            if left in inputs and right in inputs:
                gates.remove(line)
                left = inputs[left]
                right = inputs[right]
                op = ops[op]
                inputs[ans] = eval(f"{left} {op} {right}")
    ans = 0
    for key, val in inputs.items():
        if key.startswith("z") and val:
            ans += 2**int(key[1:])
    print(ans)


solve("input.txt")
