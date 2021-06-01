# O(n)
# n = len(s)

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = Counter(s)
        tCount = Counter(t)

        res = 0
        for char in sCount:
            charCountInT = 0
            if char in tCount:
                charCountInT = tCount[char]
            res += max(sCount[char] - charCountInT, 0)
        return res