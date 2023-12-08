def solve(part, test=False):
    filename = f"part{part}.txt" if test else "input.txt"
    written_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    calibration_sum = 0
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()[0]
            digits = []
            for idx, value in enumerate(words):
                try:
                    digits.append(int(value))
                except:
                    if part == 2:
                        for digit, written_digit in enumerate(written_digits):
                            if words[idx:].startswith(written_digit):
                                digits.append(digit)
            calibration_sum += int(f"{digits[0]}{digits[-1]}")
    return calibration_sum

print(f"Part 1 (test): {solve(1, test=True)}")
print(f"Part 2 (test): {solve(2, test=True)}")
print(f"Part 1: {solve(1)}")
print(f"Part 2: {solve(2)}")
