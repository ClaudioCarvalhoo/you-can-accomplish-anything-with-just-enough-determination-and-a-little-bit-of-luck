# O(n² * m²)
# n = len(s) | m = len(t)


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        total = 0
        for window in range(1, len(s) + 1):
            total += self.check(s, t, window)
        return total

    def check(self, s, t, window):
        total = 0
        for i in range(len(s) - window + 1):
            cur = s[i : i + window]
            for j in range(len(t) - window + 1):
                if self.diffByOne(cur, t[j : j + window]):
                    total += 1
        return total

    def diffByOne(self, s1, s2):
        if len(s1) != len(s2):
            return False
        ok = False
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                if ok:
                    return False
                else:
                    ok = True
        return ok