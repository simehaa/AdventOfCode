with open("test.txt") as f:
    signal = f.readline()
    for j, part in zip([4, 14], [1, 2]):
        for i in range(j, len(signal)):
            if len(set(signal[i - j : i])) == j:
                print(f"Part {part}: {i}")
                break
