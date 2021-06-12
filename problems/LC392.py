# O(n)
# n = len(t)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        ps = 0
        for i in range(len(t)):
            if s[ps] == t[i]:
                ps += 1
            if ps == len(s):
                return True
        return False
