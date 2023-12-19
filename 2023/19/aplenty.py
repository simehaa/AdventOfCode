import re
from operator import lt, gt


workflows = {}
ratings = []
done_reading_workflows = False
for line in open("test.txt") :
    if line == "\n":
        done_reading_workflows = True
        continue
    elif done_reading_workflows:
        ratings.append([int(d) for d in re.findall(r"\d+", line)])
    else:
        name, conditions = line[:-2].split("{")
        workflows[name] = conditions.split(",")


def execute_workflow(x, m, a, s, name="in"):
    for condition in workflows[name]:
        if ":" in condition:
            test, next_name = condition.split(":")
            if eval(test):
                break
        else:
            next_name = condition
            break
    if next_name == "A":
        return True
    elif next_name == "R":
        return False
    else:
        return execute_workflow(x, m, a, s, next_name)


def permutations(ratings):
    perm = 1
    for l in "xmas":
        perm *= len(ratings[l])
    return perm


def get_combinations(ratings, name="in", step=0):
    condition = workflows[name][step]
    if ":" in condition:
        test, pass_name = condition.split(":")
        letter = test[0]
        operator = lt if test[1] == "<" else gt
        comparison_value = int(test[2:])
        passed_ratings = {letter: []}
        failed_ratings = {letter: []}
        for c in "xmas":
            if c != letter:
                passed_ratings[c] = ratings[c].copy()
                failed_ratings[c] = ratings[c].copy()
        for our_value in ratings[letter]:
            if operator(our_value, comparison_value):
                passed_ratings[letter].append(our_value)
            else:
                failed_ratings[letter].append(our_value)
        if pass_name == "A":
            accepted_combinations = permutations(passed_ratings)
        elif pass_name == "R":
            accepted_combinations = 0
        else:
            accepted_combinations = get_combinations(passed_ratings, name=pass_name, step=0)
        return accepted_combinations + get_combinations(failed_ratings, name=name, step=step+1)
    else:
        if condition == "A":
            return permutations(ratings)
        elif condition == "R":
            return 0
        else:
            return get_combinations(ratings, name=condition, step=0)
        

print("Part 1:", sum([sum(r) if execute_workflow(*r) else 0 for r in ratings]))
print("Part 2:", get_combinations({
    "x": [i+1 for i in range(4000)],
    "m": [i+1 for i in range(4000)],
    "a": [i+1 for i in range(4000)],
    "s": [i+1 for i in range(4000)],
}))
