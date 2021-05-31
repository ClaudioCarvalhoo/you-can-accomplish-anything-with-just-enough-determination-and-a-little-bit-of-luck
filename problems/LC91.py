# O(n)
# n = len(s)


class Solution:
    def numDecodings(self, s: str) -> int:
        return self.explore(s, 0, {})

    def explore(self, s, i, results):
        if i == len(s):
            return 1
        if i not in results:
            results[i] = self.useOne(s, i, results) + self.useTwo(s, i, results)
        return results[i]

    def useOne(self, s, i, results):
        if s[i] == "0":
            return 0
        else:
            return self.explore(s, i + 1, results)

    def useTwo(self, s, i, results):
        if (
            i + 1 >= len(s)
            or s[i] not in ["1", "2"]
            or (s[i] == "2" and int(s[i + 1]) > 6)
        ):
            return 0
        else:
            return self.explore(s, i + 2, results)
