# O(n*s)
# n = len(nums) | s = sum(nums)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.explore(nums, target, 0, 0, {})

    def explore(self, nums, target, curSum, i, visited):
        if i == len(nums):
            return 1 if curSum == target else 0
        if (i, curSum) in visited:
            return visited[(i, curSum)]

        result = self.explore(
            nums, target, curSum + nums[i], i + 1, visited
        ) + self.explore(nums, target, curSum - nums[i], i + 1, visited)
        visited[(i, curSum)] = result
        return result