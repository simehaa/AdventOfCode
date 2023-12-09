crate_lines = []
instruction_lines = []

with open("input.txt", "r") as f:
    # Read initial crate configuration
    crate_line_active = True
    for line in f:
        if line != "\n":
            if crate_line_active:
                crate_lines.append(line)
            else:
                instruction_lines.append(line)
        else:
            # Start reading instruction lines
            crate_line_active = False


# Create storage dictionaries
storage1 = {}
storage2 = {}
for char in crate_lines[-1].split(" "):
    try:
        digit = int(char)
        storage1[digit] = []
        storage2[digit] = []
    except ValueError:
        pass


# Create initial storage configuration
for line in crate_lines[-2::-1]:
    for index, position in zip(range(1, len(line), 4), storage1.keys()):
        crate = line[index]
        if crate != " ":
            storage1[position].append(crate)
            storage2[position].append(crate)


# Execute instructions
for line in instruction_lines:
    _, quantity, _, source, _, destination = line.split(" ")
    quantity = int(quantity)
    source = int(source)
    destination = int(destination)

    # Execute instructions for CrateMover 9000
    for i in range(quantity):
        storage1[destination].append(storage1[source].pop())

    # Execute instructions for CrateMover 9001
    storage2[destination] += storage2[source][-quantity:]
    storage2[source] = storage2[source][:-quantity]


# Part 1 solution (top crate from each position)
for position in storage1.keys():
    print(storage1[position][-1], end="")
print()


# Part 2 solution (top crate from each position)
for position in storage2.keys():
    print(storage2[position][-1], end="")
print()
