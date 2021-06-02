# O(n)
# n = len(nums)

# Sol 1
# O(n) Space
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = nums[:2]
        dp.append(nums[2] + nums[0])
        for i in range(3, len(nums)):
            bestPreviousHouse = max(dp[i - 2], dp[i - 3])
            dp.append(bestPreviousHouse + nums[i])
        return max(dp[-1], dp[-2])


# Sol 2
# O(1) Space
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        threeDown, twoDown, oneDown = nums[0], nums[1], nums[0] + nums[2]
        for i in range(3, len(nums)):
            bestPreviousHouse = max(twoDown, threeDown)
            threeDown = twoDown
            twoDown = oneDown
            oneDown = bestPreviousHouse + nums[i]
        return max(oneDown, twoDown)


# Sol 3
# O(1) Space modifying input
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        nums[2] = nums[2] + nums[0]
        for i in range(3, len(nums)):
            bestPreviousHouse = max(nums[i - 2], nums[i - 3])
            nums[i] = bestPreviousHouse + nums[i]
        return max(nums[-1], nums[-2])