def update_CRT(CRT, X, cycle):
    if abs(X[0] - (cycle % 40)) <= 1:
        return CRT + "#"
    return CRT + "."


def update_X(X, instruction):
    X[0] += X[1]
    X[1] = X[2]
    if instruction[0] == "addx":
        X[2] = int(instruction[1])
    elif instruction[0] == "noop":
        X[2] = 0
    return X


def read_input():
    instructions = []
    with open("test.txt") as f:
        for line in f:
            instructions.append(line.split())
    return instructions


if __name__ == "__main__":
    instructions = read_input()

    # loop through instructions, calculate X and draw CRT
    X = [1, 0, 0]
    cycle = 0
    signals = []
    CRT = ""  # list of pixels
    for instruction in instructions:
        # Execute 1st cycle
        X = update_X(X, instruction)
        CRT = update_CRT(CRT, X, cycle)
        cycle += 1

        # Check if magic cycle number
        if (cycle - 20) % 40 == 0:
            signals.append(X[0] * cycle)

        # if addx, execute 2nd cycle
        if instruction[0] == "addx":
            X = update_X(
                X, ["noop"]
            )  # since this is second cycle, continue calculating X, but no new instruction
            CRT = update_CRT(CRT, X, cycle)
            cycle += 1

            # Check if magic cycle number
            if (cycle - 20) % 40 == 0:
                signals.append(X[0] * cycle)

    print(f"Part 1: {sum(signals)}")
    print("Part 2:")
    for i in range(0, len(CRT), 40):
        print(CRT[i : i + 40])
