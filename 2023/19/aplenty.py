import re

workflows = {}
ratings = []
done_reading_workflows = False
workflow_lines, ratings_lines = open("test.txt").read().split("\n\n")
for line in workflow_lines.splitlines():
    name, conditions = line[:-1].split("{")
    workflows[name] = conditions.split(",")
for line in ratings_lines.splitlines():
    ratings.append([int(d) for d in re.findall(r"\d+", line)])


def execute_workflow(x, m, a, s, name="in"):
    for condition in workflows[name]:
        if ":" not in condition:
            break
        test, condition = condition.split(":")
        if eval(test):
            break
    if condition == "A":
        return True
    if condition == "R":
        return False
    return execute_workflow(x, m, a, s, condition)


def get_combinations(ratings, name="in", step=0):
    if name == "A":
        return len(ratings["x"]) * len(ratings["m"]) * len(ratings["a"]) * len(ratings["s"])
    if name == "R":
        return 0
    condition = workflows[name][step]
    if ":" not in condition:
        return get_combinations(ratings, name=condition, step=0)
    test, next_name = condition.split(":")
    letter = test[0]
    operator = int.__lt__ if test[1] == "<" else int.__gt__
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
    return get_combinations(passed_ratings, name=next_name, step=0) + get_combinations(
        failed_ratings, name=name, step=step + 1
    )


print("Part 1:", sum([sum(r) if execute_workflow(*r) else 0 for r in ratings]))
print(
    "Part 2:",
    get_combinations(
        {
            "x": [i + 1 for i in range(4000)],
            "m": [i + 1 for i in range(4000)],
            "a": [i + 1 for i in range(4000)],
            "s": [i + 1 for i in range(4000)],
        }
    ),
)
