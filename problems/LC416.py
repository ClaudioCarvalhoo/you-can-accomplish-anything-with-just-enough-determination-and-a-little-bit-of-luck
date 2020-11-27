# O(n * m)
# n = len(nums) | m = len(subsetSums(nums))


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsSum = sum(nums)
        if numsSum % 2 != 0:
            return False
        midpoint = numsSum // 2

        nums.sort(reverse=True)

        reachable = {}

        for i in range(len(nums)):
            n = nums[i]
            if n == midpoint:
                return True
            for j in list(reachable.keys()):
                if n + j == midpoint:
                    return True
                reachable[n + j] = True
            reachable[n] = True

        return False
