with open("input.txt") as f:
    inputs_raw, gates_raw = f.read().split("\n\n")

inputs = {}
for line in inputs_raw.splitlines():
    name, value = line.split(": ")
    inputs[name] = int(value)

gates = {}
for line in gates_raw.splitlines():
    op, ans = line.split(" -> ")
    gates[ans] = op


def part1(inputs, gates):
    gates_todo = [(ans, op) for ans, op in gates.items()]
    ops = {"AND": "&", "OR": "|", "XOR": "^"}
    total = 0
    while gates_todo:
        for ans, op in gates_todo:
            l, o, r = op.split()
            if l in inputs and r in inputs:
                gates_todo.remove((ans, op))
                inputs[ans] = eval(f"{inputs[l]} {ops[o]} {inputs[r]}")
                if ans[0] == "z":
                    total += inputs[ans]*2**int(ans[1:])
    print("part 1:", total)


def find_wrong_wires(gates):
    # First gate x00 + y00 = z00 and potential carry bit
    carry = ""
    for k, v in gates.items():
        l, o, r = v.split()
        if l in ["x00", "y00"]:
            if o == "XOR" and k != "z00":
                return [k, "z00"]
            if o == "AND":
                carry = k

    # Ensure logic
    # x XOR y -> xor_val
    # x AND y -> and_val
    # carry XOR xor_val -> z
    # carry AND xor_val -> na
    # na OR and_val -> carry (for next bit)
    for i in range(1, 45):
        xor_val = ""  # x XOR y
        and_val = ""  # x AND y
        s = f"{i:02d}"
        for k, v in gates.items():
            l, o, r = v.split()
            if l == "x" + s or l == "y" + s:
                if o == "XOR":
                    xor_val = k
                if o == "AND":
                    and_val = k

        # Assuming carry is correct, we can evaluate xor_val and z
        for k, v in gates.items():
            l, o, r = v.split()

            # Check whether xor_val is correct, it should only be involved
            # with operations with the carry register:
            if carry in {l, r} and xor_val not in {l, r}:
                other = l if carry == r else r
                return [xor_val, other]

            # Check that writing to the z is correct, the operation
            # carry XOR xor_val -> z (is expected to write to z)
            if {xor_val, "XOR", carry} == {l, o, r} and k != "z" + s:
                return [k, "z" + s]

        na = ""
        for k, v in gates.items():
            l, o, r = v.split()
            if {xor_val, "AND", carry} == {l, o, r}:
                na = k

        # If both and_val and na are wrong, we have a problem,
        # but we can easily detect if ONLY ONE of them are wrong
        # because they should only be used in a single OR operation
        # with each other
        for k, v in gates.items():
            l, o, r = v.split()
            if and_val in {l, r} and not na in {l, r}:
                other = l if and_val == r else r
                return [na, other]
            if na in {l, r} and not and_val in {l, r}:
                other = l if na == r else r
                return [and_val, other]

        # Write carry-bit for next iteration, if this is wrong
        # then we would have had to cross-check with two operations
        # in the next iteration. We don't do this, we just assume this
        # operation always writes correctly
        carry = ""
        for k, v in gates.items():
            l, o, r = v.split()
            if {and_val, "OR", na} == {l, o, r}:
                carry = k
                break
    return None


def part2(gates):
    wires = []
    while len(wires) < 8:
        a, b = find_wrong_wires(gates)
        gates[a], gates[b] = gates[b], gates[a]
        wires += [a, b]
    print("part 2:", ",".join(sorted(wires)))

# Warning: not fully generalized
# There are two cases my algorithm will not pick up on
# Case 1:
# if BOTH of these operations writes wrong for the same bit
# (x XOR y) AND carry -> register_a
# (x AND y) AND carry -> register_b
# Case 2:
# if register_a OR register_b -> carry (for the next bit)
# writes to the wrong register
part1(inputs, gates)
part2(gates)
