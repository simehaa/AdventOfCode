def checksum(arr):
    t = 0
    for i, c in enumerate(arr):
        if c == ".":
            continue
        t += i * int(c)
    return t


def part1(s):
    arr = list()
    for i, c in enumerate(s):
        if i % 2 == 0:
            arr += [i // 2] * int(c)  # i//2 is the ID
        else:
            arr += ["."] * int(c)

    arr = arr.copy()
    j = -1
    for i, c in enumerate(arr):
        if c == ".":
            while arr[j] == ".":
                j -= 1
            if i >= len(arr) + j:
                break
            arr[i], arr[j] = arr[j], arr[i]
    return checksum(arr)


def part2(s):
    arr = list()
    for i, c in enumerate(s):
        if i % 2 == 0:
            arr.append([i // 2] * int(c))  # i//2 is the ID
        else:
            arr.append(["."] * int(c))

    moved_ids = {".", 0}
    for block_idx_r, block in enumerate(reversed(arr)):
        if not len(block) or not all(x == block[0] for x in block):
            continue
        id_ = block[0]
        if id_ in moved_ids:
            continue

        len_ = len(block)
        i = len(arr) - block_idx_r - 1
        for j in range(1, i):
            start = 0
            for k, c in enumerate(arr[j]):
                if c != ".":
                    start = k + 1
                    continue
                stop = k + 1
                if stop - start == len_:
                    # This means there is space to insert file here
                    arr[j][start:stop], arr[i] = arr[i], arr[j][start:stop]
                    break
    combined = []
    for block in arr:
        combined += block
    return checksum(combined)


print("test part 1:", part1("2333133121414131402"))
print("test part 2:", part2("2333133121414131402"))
with open("input.txt") as f:
    input_str = f.read().rstrip()
    print("part 1:", part1(input_str))
    print("part 2:", part2(input_str))
