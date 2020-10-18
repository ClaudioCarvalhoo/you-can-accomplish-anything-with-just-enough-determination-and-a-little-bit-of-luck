class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        table = {}
        for i in range(len(s)):
            if s[i] in table:
                table[s[i]].append(i)
            else:
                table[s[i]] = [i]

        best = -1
        for a in table:
            if len(table[a]) > 1:
                diff = table[a][-1] - table[a][0] - 1
                best = max(best, diff)

        return best
