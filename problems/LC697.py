# O(n)
# n = len(nums)


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        numsCount = {}
        firstAppearance = {}
        lastAppearance = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in firstAppearance:
                firstAppearance[num] = i
            lastAppearance[num] = i
            if num not in numsCount:
                numsCount[num] = 0
            numsCount[num] += 1
            degree = max(degree, numsCount[num])

        degreeSetters = [num for num in numsCount if numsCount[num] == degree]
        res = float("inf")
        for num in degreeSetters:
            res = min(res, lastAppearance[num] - firstAppearance[num] + 1)
        return res