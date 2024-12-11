from functools import cache


@cache
def count(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return count(1, blinks - 1)
    if len(str(stone)) % 2 == 0:
        l = len(str(stone)) // 2
        left = int(str(stone)[:l])
        right = int(str(stone)[l:])
        return count(left, blinks - 1) + count(right, blinks - 1)
    return count(int(stone) * 2024, blinks - 1)


def count_all_stones(stones, blinks):
    return sum([count(s, blinks) for s in stones])


test = [125, 17]
print("Test (6 blinks):", count_all_stones(test, 6))
print("Test (25 blinks):", count_all_stones(test, 25))
puzzle = [0, 7, 6618216, 26481, 885, 42, 202642, 8791]
print("Part 1 (25 blinks):", count_all_stones(puzzle, 25))
print("Part 2 (75 blinks):", count_all_stones(puzzle, 75))
