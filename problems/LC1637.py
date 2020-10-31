# O(n * log(n))
# n = len(points)


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = [p[0] for p in points]
        xs.sort()
        largest = 0
        for i in range(len(xs) - 1):
            largest = max(largest, xs[i + 1] - xs[i])
        return largest