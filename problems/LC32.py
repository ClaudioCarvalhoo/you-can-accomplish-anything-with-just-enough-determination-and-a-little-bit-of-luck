# O(n)
# n = len(s)

# Sol 1 | O(n) Space
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        isValid = [False for _ in s]
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif len(stack) == 0:
                stack = []
            else:
                isValid[stack.pop()] = True
                isValid[i] = True

        res = 0
        windowSize = 0
        for i in range(len(isValid)):
            if isValid[i]:
                windowSize += 1
            else:
                windowSize = 0
            res = max(res, windowSize)
        return res


# Sol 2 | O(1) Space
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        opened = 0
        closed = 0
        for char in s:
            if char == "(":
                opened += 1
            elif opened > closed:
                closed += 1
            else:
                opened = 0
                closed = 0
            if opened == closed:
                res = max(res, opened * 2)

        opened = 0
        closed = 0
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char == ")":
                closed += 1
            elif closed > opened:
                opened += 1
            else:
                opened = 0
                closed = 0
            if opened == closed:
                res = max(res, opened * 2)

        return res