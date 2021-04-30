# O(n)
# n = len(s)


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) <= 0:
            return []
        res = []
        start = 0
        for i in range(0, len(s)):
            endOfGroup = (i + 1 >= len(s)) or (s[i + 1] != s[i])
            if endOfGroup:
                if i - start >= 2:
                    res.append([start, i])
                start = i + 1
        return res
