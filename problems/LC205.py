# O(n)
# n = len(s)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapper = {}
        used = set()
        for i in range(len(s)):
            charS = s[i]
            charT = t[i]
            if charS not in mapper:
                if charT in used:
                    return False
                mapper[charS] = charT
                used.add(charT)
            elif mapper[charS] != charT:
                return False
        return True