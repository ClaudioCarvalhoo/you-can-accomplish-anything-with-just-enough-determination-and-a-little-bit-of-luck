# O(n)
# n = len(s)


class Solution:
    def minFlips(self, s: str) -> int:
        res = float("inf")
        necessaryFlips1 = 0
        necessaryFlips2 = 0
        for i in range(len(s) * 2):
            necessaryFlips1 += 1 if self.checkPosEquality(s, i, False) else 0
            necessaryFlips2 += 1 if self.checkPosEquality(s, i, True) else 0
            if i >= len(s):
                windowStart = i - len(s)
                necessaryFlips1 -= (
                    1 if self.checkPosEquality(s, windowStart, False) else 0
                )
                necessaryFlips2 -= (
                    1 if self.checkPosEquality(s, windowStart, True) else 0
                )
                res = min(res, necessaryFlips1, necessaryFlips2)
        return res

    # Check comparing to either "01010101" or "10101010"
    def checkPosEquality(self, s, i, startingWithOne):
        elem = "0" if i % 2 == 0 else "1"
        if startingWithOne:
            elem = "1" if i % 2 == 0 else "0"
        return s[i % len(s)] == elem
