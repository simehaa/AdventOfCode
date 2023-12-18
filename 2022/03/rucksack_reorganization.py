priority = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Part 1
score1 = 0
with open("test.txt") as f:
    for i, line in enumerate(f):
        half_length = (len(line) - 1) // 2 # remove newline, int division
        compartment1 = line[:half_length]
        compartment2 = line[half_length:-1]
        # print(f"Rucksack {i},", compartment1, compartment2, end=", ")
        for l in compartment1:
            if l in compartment2:
                # print(f"common item: {l}, priority: {priority.index(l)}")
                score1 += priority.index(l)
                break

print("Part 1:", score1)


# Part 2
score2 = 0
with open("test.txt") as f:
    all_elves = f.readlines()
    for i in range(0, len(all_elves), 3):
        elf1 = all_elves[i]
        elf2 = all_elves[i + 1]
        elf3 = all_elves[i + 2]
        # print(f"Elf {i+1}-{i+3},", elf1, elf2, elf3, end=", ")
        for l in elf1:
            if l in elf2 and l in elf3:
                # print(f"Common item: {l}, priority: {priority.index(l)}")
                score2 += priority.index(l)
                break

print("Part 2:", score2)