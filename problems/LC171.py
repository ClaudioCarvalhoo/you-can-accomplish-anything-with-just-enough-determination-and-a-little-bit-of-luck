# O(n)
# n = len(columnTitle)


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            charValue = ord(columnTitle[-i - 1]) - ord("A") + 1
            multiplier = 26 ** i
            res += charValue * multiplier
        return res