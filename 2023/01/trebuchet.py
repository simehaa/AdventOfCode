def solve(filename, part=1):
    written_digits = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    calibration_sum = 0
    for line in open(filename):
        digits = []
        for idx, value in enumerate(line):
            if value.isdigit():
                digits.append(int(value))
            elif part == 2:
                for digit, spelled in enumerate(written_digits):
                    if line[idx:].startswith(spelled):
                        digits.append(digit)
        calibration_sum += int(f"{digits[0]}{digits[-1]}")
    return calibration_sum


print("Part 1:", solve("test_1.txt", part=1))
print("Part 2:", solve("test_2.txt", part=2))
