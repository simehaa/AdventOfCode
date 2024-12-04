import re


def solve(filename):
    with open(filename) as f:
        input_str = f.read()
    mul_pattern = r"mul\(\d+,\d+\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don\'t\(\)"
    full_pattern = "|".join([mul_pattern, do_pattern, dont_pattern])
    all_muls = []
    enabled_muls = []
    enabled = True
    for match in re.findall(full_pattern, input_str):
        if match == "do()":
            enabled = True
            continue
        if match == "don't()":
            enabled = False
            continue
        product = 1
        for num in re.findall(r"\d+", match):
            product *= int(num)
        all_muls.append(product)
        if enabled:
            enabled_muls.append(product)
    print(sum(all_muls), sum(enabled_muls))


solve("test.txt")
solve("input.txt")
