# O(n * m)
# n = len(nums) | m = sum(nums)/2


# Recursive + memo solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums) / 2
        if goal != int(goal):
            return False

        return self.helper(nums, 0, 0, goal, set())

    def helper(self, nums, index, sumSoFar, goal, visited):
        if sumSoFar == goal:
            return True
        if (index, sumSoFar) in visited or index >= len(nums) or sumSoFar > goal:
            return False

        visited.add((index, sumSoFar))
        return self.helper(
            nums, index + 1, sumSoFar + nums[index], goal, visited
        ) or self.helper(nums, index + 1, sumSoFar, goal, visited)


# Knapsack-like solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        goal = total // 2

        dp = [[False for _ in range(goal + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = True

        for i in range(1, len(dp)):
            item = nums[i - 1]
            for j in range(len(dp[i])):
                notUsingItem = dp[i - 1][j]
                usingItem = False
                if j - item >= 0:
                    usingItem = dp[i - 1][j - item]
                dp[i][j] = usingItem or notUsingItem
            if dp[i][-1]:
                return True

        return False