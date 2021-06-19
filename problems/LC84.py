# O(n)
# n = len(heights)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(heights)):
            start = i
            while len(stack) > 0 and stack[-1][1] >= heights[i]:
                start, prevHeight = stack.pop()
                res = max(res, (i - start) * prevHeight)
            stack.append((start, heights[i]))
        while len(stack) > 0:
            start, prevHeight = stack.pop()
            res = max(res, (len(heights) - start) * prevHeight)
        return res