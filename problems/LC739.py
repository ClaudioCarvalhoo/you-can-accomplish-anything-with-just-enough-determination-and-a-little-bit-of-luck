# O(n)
# n = len(T)


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in T]
        for i in range(len(T) - 1, -1, -1):
            while len(stack) > 0 and stack[-1][0] <= T[i]:
                stack.pop()
            if len(stack) > 0:
                res[i] = stack[-1][1] - i
            stack.append((T[i], i))
        return res