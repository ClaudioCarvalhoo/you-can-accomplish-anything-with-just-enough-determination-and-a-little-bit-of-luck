# O(n)
# n = len(s)


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        i = 0
        for i in range(len(s)):
            if len(stack) > 0 and stack[-1][0] == s[i]:
                stack[-1][1] += 1
            else:
                stack.append([s[i], 1])
            if stack[-1][1] == k:
                stack.pop()
        res = []
        for char, quant in stack:
            res += [char] * quant
        return "".join(res)
