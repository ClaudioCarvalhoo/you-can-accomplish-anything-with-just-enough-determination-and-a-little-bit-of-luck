# O(n)
# n = len(s)


class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        openParenthesis = 0
        for char in s:
            if char == "(":
                openParenthesis += 1
                res = max(res, openParenthesis)
            elif char == ")":
                openParenthesis -= 1
        return res