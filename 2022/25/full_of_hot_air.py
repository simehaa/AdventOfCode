class SNAFU:
    def __init__(self, snafu_str):
        self.snafu_str = snafu_str
        self.positive_part = ""
        self.negative_part = ""
        for c in snafu_str:
            if c == "=":
                self.negative_part += "2"
                self.positive_part += "0"
            elif c == "-":
                self.negative_part += "1"
                self.positive_part += "0"
            else:
                self.negative_part += "0"
                self.positive_part += c

        print(self.snafu_str, self.positive_part, self.negative_part)

        self.snafu_list = [i for i in self.snafu_str]
        self.snafu_list.reverse()
        self.snafu_list_digits = []
        for s in self.snafu_list:
            if s == "=":
                self.snafu_list_digits.append(-2)
            elif s == "-":
                self.snafu_list_digits.append(-1)
            else:
                self.snafu_list_digits.append(int(s))
        self.decimal = 0
        for i, s in enumerate(self.snafu_list_digits):
            self.decimal += s * 5**i

    def __add__(self, other):
        resulting_snafu_list_digits = self.snafu_list_digits.copy()
        for i, s in enumerate(other.snafu_list_digits):
            if i < len(resulting_snafu_list_digits):
                resulting_snafu_list_digits[i] += s
            else:
                resulting_snafu_list_digits.append(s)

        for i in range(len(resulting_snafu_list_digits)):
            if resulting_snafu_list_digits[i] > 2:
                resulting_snafu_list_digits[i] -= 5
                if i + 1 < len(resulting_snafu_list_digits):
                    resulting_snafu_list_digits[i + 1] += 1
                else:
                    resulting_snafu_list_digits.append(1)
            elif resulting_snafu_list_digits[i] < -2:
                resulting_snafu_list_digits[i] += 5
                if i + 1 < len(resulting_snafu_list_digits):
                    resulting_snafu_list_digits[i + 1] -= 1
                else:
                    resulting_snafu_list_digits.append(-1)

        resulting_snafu_list_digits.reverse()
        snafu_str = ""
        for s in resulting_snafu_list_digits:
            if s == -2:
                snafu_str += "="
            elif s == -1:
                snafu_str += "-"
            else:
                snafu_str += str(s)

        return SNAFU(snafu_str)

    def __repr__(self):
        return self.snafu_str


total = SNAFU("0")
decimal_total = 0
with open("test.txt") as f:
    for line in f:
        snafu = SNAFU(line.rstrip())

        total += SNAFU(line.rstrip())
        print(total)

SNAFU("0-") + SNAFU
