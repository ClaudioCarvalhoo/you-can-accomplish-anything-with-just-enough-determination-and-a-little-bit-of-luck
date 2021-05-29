# O(n)
# n = len(s)


class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        negative = False
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and (s[i] == "+" or s[i] == "-"):
            negative = s[i] == "-"
            i += 1
        while i < len(s) and s[i].isdigit():
            res *= 10
            res += int(s[i])
            i += 1
        if negative:
            res = max((-2) ** 31, -res)
        else:
            res = min((2 ** 31) - 1, res)
        return res