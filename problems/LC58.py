# O(n)
# n = len(s)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        firstNonSpace = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                firstNonSpace = i
                break
        if firstNonSpace == -1:
            return 0
        count = 0
        for i in range(firstNonSpace, -1, -1):
            if s[i] == " ":
                break
            count += 1
        return count