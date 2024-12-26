with open("input.txt") as f:
    inputs_raw, gates_raw = f.read().split("\n\n")

inputs = {}
for line in inputs_raw.splitlines():
    name, value = line.split(": ")
    inputs[name] = int(value)

gates = {}
gates_todo = []
for line in gates_raw.splitlines():
    op, ans = line.split(" -> ")
    gates[op] = ans
    gates_todo.append((op, ans))

# Part 1
ops = {"AND": "&", "OR": "|", "XOR": "^"}
total = 0
while gates_todo:
    for op, ans in gates_todo:
        l, o, r = op.split()
        if l in inputs and r in inputs:
            gates_todo.remove((op, ans))
            inputs[ans] = eval(f"{inputs[l]} {ops[o]} {inputs[r]}")
            if ans[0] == "z":
                total += inputs[ans]*2**int(ans[1:])
print(total)

# Part 2
carry = ""
for k, v in gates.items():
    l, o, r = k.split()
    if l in ["x00", "y00"]:
        if o == "XOR":
            assert v == "z00"
        if o == "AND":
            carry = v

for i in range(1, 45):
    # We first need to determine registers for the XOR and the AND of x, y
    x = ""  # x__ XOR y__
    a = ""  # x__ AND y__
    s = f"{i:02d}"
    print(s)
    for k, v in gates.items():
        l, o, r = k.split()
        if l == "x" + s or l == "y" + s:
            if o == "XOR":
                x = v
            if o == "AND":
                a = v
    print("XOR:", x)
    print("AND:", a)

    # assert carry XOR x should be z__
    # carry AND x store to b
    na = ""
    for k, v in gates.items():
        l, o, r = k.split()
        if {x, carry} == {l, r}:
            if o == "XOR":
                assert v == "z" + s, k + " -> " + v
            if o == "AND":
                na = v
    if not na:
        break
    print("NA:", na)

    carry = ""
    for k, v in gates.items():
        l, o, r = k.split()
        if {a, na} == {l, r}:
            carry = v
            break
    print("Carry:", carry)


    print()

