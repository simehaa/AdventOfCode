def read_input():
    monkeys = {}
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            words = line.split()
            n = i % 7
            monkey = i // 7
            if n == 0:
                monkeys[monkey] = {"inspections": 0}
            elif n == 1:
                monkeys[monkey]["items"] = [int(j.strip(",")) for j in words[2:]]
            elif n == 2:
                monkeys[monkey]["operation"] = words[3:]
            elif n == 3:
                monkeys[monkey]["condition"] = int(words[-1])
            elif n == 4:
                monkeys[monkey]["if_true"] = int(words[-1])
            elif n == 5:
                monkeys[monkey]["if_false"] = int(words[-1])

    return monkeys


def shenanigans(rounds=1, integer_divide_by=3, verbose=False):
    monkeys = read_input()

    # A worry_level can always be reduced by the lowest common multiple of all conditions
    # Since the conditions are prime, reduce_by is the product of all conditions
    reduce_by = 1
    for key, monkey in monkeys.items():
        reduce_by *= monkey["condition"]

    # Start throwing items around...
    for rounds in range(rounds):
        for key, monkey in monkeys.items():
            if verbose:
                print(f"Monkey {key}:")

            # Any monkey will throw all items it has
            items = monkey["items"]
            monkey["items"] = []
            for item in items:
                # The monkey has inspected this item
                monkey["inspections"] += 1
                if verbose:
                    print(f"\tMonkey inspects an item with a worry level of {item}")
                
                # Perform operation (a <op> b)
                if monkey["operation"][0] == "old":
                    a = item
                else:
                    a = int(monkey["operation"][0])
                if monkey["operation"][-1] == "old":
                    b = item
                else:
                    b = int(monkey["operation"][-1])
                if monkey["operation"][1] == "+":
                    worry_level = a + b
                elif monkey["operation"][1] == "*":
                    worry_level = a * b
                if verbose:
                    print(f"\t\tWorry level increased to {worry_level}")

                # If integer_divide_by is set, worry_level is int divided by it
                if integer_divide_by:
                    worry_level //= integer_divide_by
                    if verbose:
                        print(f"\t\tWorry level decreased to {worry_level}")

                # Reduce worry_level to avoid divergence
                worry_level %= reduce_by
                if verbose:
                    print(f"\t\tWorry level decreased to {worry_level}")
                
                # Monkey will now check the condition, before throwing the item to another monkey
                if worry_level % monkey["condition"] == 0:
                    monkeys[monkey["if_true"]]["items"].append(worry_level)       
                    if verbose:
                        print(f"\t\tItem with worry level {worry_level} is thrown to monkey {monkey['if_true']}")
                else:
                    monkeys[monkey["if_false"]]["items"].append(worry_level)
                    if verbose:
                        print(f"\t\tItem with worry level {worry_level} is thrown to monkey {monkey['if_false']}")

    # Monkey business is the produce of the two most active monkeys
    inspections = [monkey["inspections"] for key, monkey in monkeys.items()]
    most_active_monkey = max(inspections)
    inspections.remove(most_active_monkey)
    second_most_active_monkey = max(inspections)

    return most_active_monkey * second_most_active_monkey

if __name__ == "__main__":
    rounds = 20
    print(f"Monkey business after {rounds} rounds (with integer division by 3): {shenanigans(rounds, integer_divide_by=3)}")
    rounds = 10000
    print(f"Monkey business after {rounds} rounds (no division): {shenanigans(rounds, integer_divide_by=False)}")
    