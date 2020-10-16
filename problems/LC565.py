# O(n)
# n = len(nums)

from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = {}
        largest = 1
        for i in range(len(nums)):
            if not i in visited:
                count = 1
                visited[i] = True
                j = nums[i]
                while j != i:
                    if j in visited:
                        break
                    visited[j] = True
                    count += 1
                    largest = max(largest, count)
                    j = nums[j]

        return largest