# O(n)
# n = len(height)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 0

        while start < end:
            currentArea = min(height[start], height[end]) * (end - start)
            area = max(area, currentArea)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return area