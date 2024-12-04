def solve(filename):
    left = []
    right = []
    for line in open(filename):
        a, b = line.split()
        left.append((int(a)))
        right.append((int(b)))
    left = sorted(left)
    right = sorted(right)
    s = 0
    p = 0
    for l, r in zip(left, right):
        s += abs(r - l)
        p += l * right.count(l)
    print(s)
    print(p)

if __name__ == "__main__":
    solve("test.txt")