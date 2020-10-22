# O(n)
# n = len(S)


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        total = 0
        i = 0
        while i < len(S) - 1:
            res = self.calculateScore(S, i)
            total += res[0]
            i = res[1]
        return total

    def calculateScore(self, S, i):
        if S[i] == "(" and S[i + 1] == ")":
            return (1, i + 2)
        elif S[i] == "(" and S[i + 1] == "(":
            total = 0
            i += 1
            while i < len(S) - 1:
                res = self.calculateScore(S, i)
                i = res[1]
                if res[0] == 0:
                    break
                total += res[0]
            return (2 * total, i)
        else:
            return (0, i + 1)
