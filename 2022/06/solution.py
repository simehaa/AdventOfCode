with open("input.txt", "r") as f:
    signal = f.readline()
    for j in [4, 14]:
        for i in range(j, len(signal)):
            if len(set(signal[i-j:i])) == j:
                print(f"start-of-packet marker ({j}): {i}")
                break
