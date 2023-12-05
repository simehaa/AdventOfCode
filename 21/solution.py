monkeys = {}
with open("input.txt", "r") as f:
    for line in f:
        monkey, expr = line.rstrip().split(": ")
        if expr.isnumeric():
            globals()[monkey] = eval(expr)
        elif monkey == "root":
            root_a, root_op, root_b  = expr.split(" ")
        else:
            monkeys[monkey] = expr

# while monkeys: 
#     new_monkeys = []
#     for monkey, expr in monkeys.items():
#         try:
#             globals()[monkey] = eval(expr)
#             new_monkeys.append(monkey)
#         except NameError:
#             pass

#     for monkey in new_monkeys:
#         del monkeys[monkey]

# print(int(eval(root_a + root_op + root_b)))

monkeys_depend_on_humn = ["humn"]
new_dependent_monkeys_added = True
while new_dependent_monkeys_added:
    new_dependent_monkeys_added = False
    for monkey, expr in monkeys.items():
        a, op, b = expr.split()
        if (monkey not in monkeys_depend_on_humn) and (a in monkeys_depend_on_humn or b in monkeys_depend_on_humn):
            monkeys_depend_on_humn.append(monkey)
            new_dependent_monkeys_added = True


new_expressions_evaluated = True
while new_expressions_evaluated:
    new_expressions_evaluated = False
    new_monkeys = []
    for monkey, expr in monkeys.items():
        if monkey not in monkeys_depend_on_humn:
            try:
                globals()[monkey] = eval(expr)
                new_monkeys.append(monkey)
                new_expressions_evaluated = True
            except NameError:
                pass

    for monkey in new_monkeys:
        del monkeys[monkey]


def test_new_number(humn, root_a, root_b, monkeys):
    while monkeys:
        new_monkeys = []
        for monkey, expr in monkeys.items():
            try:
                locals()[monkey] = eval(expr)
                new_monkeys.append(monkey)
            except NameError:
                pass
        
        for monkey in new_monkeys:
           del monkeys[monkey]

    if eval(root_a) == eval(root_b):
        print(f"humn = {int(humn)} gave the CORRECT result")
        exit()
    else:
        return eval(root_a)/eval(root_b)

# Found these two numbers which resulted in 2.29 and -2.01,
# We want to converge towards 1, and I here use the "half-step method"
lower_in = 0
upper_in = 10_000_000_000_000
lower_out = test_new_number(lower_in, root_a, root_b, monkeys.copy())
upper_out = test_new_number(upper_in, root_a, root_b, monkeys.copy())
while True:
    middle_in = int(lower_in + (upper_in - lower_in) / 2)
    print(f"Checking midway between {lower_in} and {upper_in}")
    middle_out = test_new_number(middle_in, root_a, root_b, monkeys.copy())
    if middle_out < 1:
        # Went to far, thus answer must lie in the bottom half
        upper_in = middle_in
    else:
        # Didn't go far enough, thus answer must lie in the upper half
        lower_in = middle_in        