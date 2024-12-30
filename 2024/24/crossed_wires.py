with open("input.txt") as f:
    inputs_raw, gates_raw = f.read().split("\n\n")

inputs = {}
for line in inputs_raw.splitlines():
    and_bme, value = line.split(": ")
    inputs[and_bme] = int(value)

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
                    total += inputs[ans] * 2 ** int(ans[1:])
    print("part 1:", total)


def find_wrong_wires(gates):
    # First gate:
    # x00 XOR y00 -> z00
    # x00 AND y00 -> carry
    carry = ""
    for k, v in gates.items():
        l, o, r = v.split()
        if l in ["x00", "y00"]:
            if o == "XOR" and k != "z00":
                return [k, "z00"]
            if o == "AND":
                carry = k

    # For bits (x01, y01, z01), ..., (x44, y44, z44)
    # (Finally z45 is simply the carry bit after bit 44)
    for i in range(1, 45):
        xor_a, and_a, xor_b, and_b = "", "", "", ""
        s = f"{i:02d}"

        # Bit-by-bit, ensure logic
        # 1) x XOR y -> xor_a
        # 2) x AND y -> and_a
        # 3) carry XOR xor_a -> xor_b (z)
        # 4) carry AND xor_a -> and_b
        # 5) and_b OR and_a -> carry (for next bit)

        # Evaluate 1) and 2)
        for k, v in gates.items():
            l, o, r = v.split()
            if {l, o, r} == {"x" + s, "XOR", "y" + s}:
                xor_a = k
            if {l, o, r} == {"x" + s, "AND", "y" + s}:
                and_a = k

        # Assuming 5) carry for the previous bit is correct
        for k, v in gates.items():
            l, o, r = v.split()

            # Check 1), assuming 5) from previous bit is correct
            if carry in {l, r} and xor_a not in {l, r}:
                return [xor_a, l if carry == r else r]

            # Potential detection of wrong carry (not implemented)
            # if xor_a is involved in two operations (one XOR and one AND), with
            # the same register, and this register is not the carry, then carry
            # is probably wrong.

            # Check 3) that writing to the z is correct, the operation
            # carry XOR xor_a -> z (is expected to write to z)
            if {xor_a, "XOR", carry} == {l, o, r} and k != "z" + s:
                return [k, "z" + s]

            # Evaluate 4); Set and_b
            if {xor_a, "AND", carry} == {l, o, r}:
                and_b = k

        # If both and_a and and_b are wrong, we have a problem,
        # but we can easily detect if ONLY ONE of them are wrong
        # because they should only be used in a single OR operation
        # with each other, and that will be the carry for the next bit
        for k, v in gates.items():
            l, o, r = v.split()

            # Evaluate 5); Set carry
            if {and_a, "OR", and_b} == {l, o, r}:
                carry = k

            # Check 2), assuming 4) is correct
            if and_a in {l, r} and and_b not in {l, r}:
                return [and_b, l if and_a == r else r]

            # Check 4), assuming 2) is correct
            if and_b in {l, r} and and_a not in {l, r}:
                return [and_a, l if and_b == r else r]


def part2(gates):
    wires = []
    while len(wires) < 8:
        a, b = find_wrong_wires(gates)
        gates[a], gates[b] = gates[b], gates[a]
        wires += [a, b]
    print("part 2:", ",".join(sorted(wires)))


# Warning:
# My algorithm is not fully generalized.
# There are two cases my algorithm will not pick up on:

# Case 1:
# if BOTH of these operations writes wrong in the same iteration (same bit)
# (x XOR y) AND carry -> and_b
# x AND y -> and_a

# Case 2:
# if and_a OR and_b -> carry (for the next bit)
# writes to the wrong register

part1(inputs, gates)
part2(gates)
