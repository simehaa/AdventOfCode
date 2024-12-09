def equal(s, nums, third=False):
    add = nums[0] + nums[1]
    mul = nums[0] * nums[1]
    con = int(f"{nums[0]}{nums[1]}")
    if len(nums) == 2:
        if s in (add, mul) or (third and s == con):
            return s
        return 0
    return (
        equal(s, (add,) + nums[2:], third)
        or equal(s, (mul,) + nums[2:], third)
        or (third and equal(s, (con,) + nums[2:], third))
    )

def solve(filename):
    t1, t2 = 0, 0
    with open(filename) as f:
        for l in f.readlines():
            s, nums = l.split(":")
            s = int(s)
            nums = eval(nums.strip().replace(" ", ","))
            t1 += equal(s, nums, False)
            t2 += equal(s, nums, True)
    print(t1, t2)

solve("test.txt")
solve("input.txt")
