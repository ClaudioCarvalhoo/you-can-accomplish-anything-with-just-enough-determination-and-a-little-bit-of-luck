# O(n)
# n = len(s)

from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str, start: int = 0) -> str:
        comeAfter = Counter(s)
        stack = []
        used = set()
        for i in range(len(s)):
            cur = s[i]
            if cur not in used:
                while len(stack) > 0 and stack[-1] > cur and comeAfter[stack[-1]] >= 1:
                    used.remove(stack.pop())
                stack.append(cur)
                used.add(cur)
            comeAfter[cur] -= 1
        return "".join(stack)
