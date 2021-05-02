# O(n)
# n = len(s)


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        res = []
        curGroupSize = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "-":
                if curGroupSize == k:
                    res.append("-")
                    curGroupSize = 0
                res.append(s[i])
                curGroupSize += 1

        for i in range(len(res) // 2):
            res[i], res[-i - 1] = res[-i - 1], res[i]

        return "".join(res)
