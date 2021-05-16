# O(n)
# n = len(s)

import collections


class Solution:
    def minSwaps(self, s: str) -> int:
        if len(s) == 1:
            return 0
        if len(s) == 2:
            return 0 if s[0] != s[1] else -1

        counter = collections.Counter(s)
        if abs(counter["0"] - counter["1"]) > 1:
            return -1

        startAtZero = 0
        startAtOne = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    startAtOne += 1
                else:
                    startAtZero += 1

        if counter["0"] == counter["1"]:
            return min(startAtZero, startAtOne)
        elif counter["0"] > counter["1"]:
            return startAtZero
        else:
            return startAtOne