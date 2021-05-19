# O(n)
# n = len(s)


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack) <= 0:
                stack.append(s[i])
            elif abs(ord(stack[-1]) - ord(s[i])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
