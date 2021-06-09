# O(n)
# n = len(nums)


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minSeen = float("inf")
        minSeenWithLower = float("inf")
        for i in range(len(nums)):
            if nums[i] > minSeen:
                if nums[i] > minSeenWithLower:
                    return True
                minSeenWithLower = min(minSeenWithLower, nums[i])
            minSeen = min(minSeen, nums[i])
        return False