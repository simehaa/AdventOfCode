from functools import cache


@cache
def decipher(secret):
    mask = 2**24 - 1
    secret ^= (secret << 6)
    secret &= mask
    secret ^= (secret >> 5)
    secret &= mask
    secret ^= (secret << 11)
    secret &= mask
    return secret


def solve(nums):
    total = 0
    sequences = {}
    for secret in nums:
        prev = int(str(secret)[-1])
        seen = set()
        sequence = []
        for i in range(2000):
            secret = decipher(secret)
            price = int(str(secret)[-1])
            sequence.append(price - prev)
            prev = price
            if len(sequence) < 4:
                continue
            key = tuple(sequence[-4:])
            if key in seen:
                continue
            seen.add(key)
            if key in sequences:
                sequences[key] += price
                continue
            sequences[key] = price
        total += secret
    print("part 1:", total)
    print("part 2:", max(sequences.values()))


with open("input.txt") as f:
    nums = [int(l) for l in f.read().splitlines()]

solve([1, 10, 100, 2024])
solve([1, 2, 3, 2024])
solve(nums)
