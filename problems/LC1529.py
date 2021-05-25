# O(n)
# n = len(target)


class Solution:
    def minFlips(self, target: str) -> int:
        res = 0
        for i in range(len(target) - 1, 0, -1):
            if target[i] != target[i - 1]:
                res += 1
        if target[0] == "1":
            res += 1
        return res