def check_safety(report):
    inc = True
    dec = True
    for i in range(1, len(report)):
        if report[i] == report[i - 1] or abs(report[i] - report[i - 1]) > 3:
            return False
        if report[i] > report[i - 1]:
            dec = False
        elif report[i] < report[i - 1]:
            inc = False
    return inc or dec


def solve(filename):
    with open(filename) as f:
        lines = f.readlines()
    safe_reports = 0
    dampened = 0
    for line in lines:
        report = [int(n) for n in line.split()]
        safe_report = check_safety(report)
        safe_reports += safe_report
        if not safe_report:
            for i in range(len(report)):
                reduced_report = report[:i] + report[i+1:]
                if check_safety(reduced_report):
                    dampened += 1
                    break
    print(safe_reports)
    print(dampened+safe_reports)


solve("test.txt")
solve("input.txt")
