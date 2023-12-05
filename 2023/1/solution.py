def day1():
    table = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    calibration_sum = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()[0]
            digits = []
            for j, c in enumerate(words):
                try:
                    digits.append(int(c))
                except:
                    for k, v in table.items():
                        if words[j:].startswith(k):
                            digits.append(v)
            calibration_sum += int(f"{digits[0]}{digits[-1]}")
    print(calibration_sum)