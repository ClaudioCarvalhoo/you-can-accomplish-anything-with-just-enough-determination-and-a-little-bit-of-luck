# O(n*m)
# n = len(matrix) | m = len(matrix[0])


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        onesColumnHeight = [[0 for _ in row] for row in matrix]
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == "1":
                    onesColumnHeight[y][x] = 1
                    if y - 1 >= 0:
                        onesColumnHeight[y][x] += onesColumnHeight[y - 1][x]

        res = 0
        for y in range(len(matrix)):
            res = max(res, self.bestRectangle(onesColumnHeight[y]))
        return res

    def bestRectangle(self, heights):
        res = 0
        stack = []
        for i in range(len(heights)):
            start = i
            while len(stack) > 0 and heights[i] < stack[-1][1]:
                start, prevHeight = stack.pop()
                res = max(res, (i - start) * prevHeight)
            stack.append((start, heights[i]))
        while len(stack) > 0:
            start, prevHeight = stack.pop()
            res = max(res, (len(heights) - start) * prevHeight)
        return res
