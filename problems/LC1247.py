# O(n)
# n = len(s1)


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        totalCount = {"x": 0, "y": 0}
        xDifferences = 0
        yDifferences = 0
        for i in range(len(s1)):
            totalCount[s1[i]] += 1
            totalCount[s2[i]] += 1
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    xDifferences += 1
                else:
                    yDifferences += 1

        if totalCount["x"] % 2 != 0 or totalCount["y"] % 2 != 0:
            return -1

        res = (xDifferences // 2) + (yDifferences // 2)
        if xDifferences % 2 > 0:
            res += 2

        return res