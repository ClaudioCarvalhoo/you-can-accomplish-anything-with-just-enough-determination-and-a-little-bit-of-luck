# O(n)
# n = len(s)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {"(": ")", "{": "}", "[": "]"}
        opening = set(openToClose.keys())
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack) <= 0 or char != openToClose[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) == 0
