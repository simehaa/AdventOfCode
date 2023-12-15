def solve(filename):
    written_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    calibration_sum_part_1 = 0
    calibration_sum_part_2 = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            words = line.split()[0]
            digits = []
            written_or_actual_digits = []
            for idx, value in enumerate(words):
                try:
                    digits.append(int(value))
                    written_or_actual_digits.append(int(value))
                except:
                    for digit, written_digit in enumerate(written_digits):
                        if words[idx:].startswith(written_digit):
                            written_or_actual_digits.append(digit)
            calibration_sum_part_1 += int(f"{digits[0]}{digits[-1]}")
            calibration_sum_part_2 += int(f"{written_or_actual_digits[0]}{written_or_actual_digits[-1]}")
    return calibration_sum_part_1, calibration_sum_part_2

part_1, part_2 = solve("part2.txt")
print(f"Part 1:", part_1)
print(f"Part 2:", part_2)