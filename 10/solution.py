X = [1, 0, 0]
cycle = 0
signals = []
CRT = "" # list of pixels


def update_CRT(CRT, X, cycle):
    if abs(X[0] - (cycle%40)) <= 1:
        CRT += "#"
    else:
        CRT += "."
    return CRT


def update_X(X, instruction):
    X[0] += X[1]
    X[1] = X[2]
    if instruction == "addx":
        X[2] = int(instructions[1])
    elif instruction == "noop":
        X[2] = 0
    return X


with open("input.txt", "r") as f:
    for line in f:
        instructions = line.split()

        # Begin cycle
        X = update_X(X, instructions[0])
        CRT = update_CRT(CRT, X, cycle)
        cycle += 1

        # Check if magic cycle number
        if (cycle - 20) % 40 == 0:
            signals.append(X[0]*cycle)

        # if addx, continue to 2nd cycle
        if instructions[0] == "addx":
            X = update_X(X, "noop") # since this is second cycle, continue calculating X, but no new instruction
            CRT = update_CRT(CRT, X, cycle)
            cycle += 1

            # Check if magic cycle number
            if (cycle - 20) % 40 == 0:
                signals.append(X[0]*cycle)

print(f"Sum of signals: {sum(signals)}")
print(" CRT ".center(40, "-"))
for i in range(0, len(CRT), 40):
    print(CRT[i:i+40])
