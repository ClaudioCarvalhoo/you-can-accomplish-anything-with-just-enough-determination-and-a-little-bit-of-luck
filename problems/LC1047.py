# O(n)
# n = len(S)


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            if len(stack) > 0 and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
